import gradio as gr
import numpy as np
import soundfile as sf

import sys
import os
import random
import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../ChatTTS')))

import ChatTTS
chat = ChatTTS.Chat()

# load models from local path or snapshot

required_files = [
    'models/asset/Decoder.pt',
    'models/asset/DVAE.pt',
    'models/asset/GPT.pt',
    'models/asset/spk_stat.pt',
    'models/asset/tokenizer.pt',
    'models/asset/Vocos.pt',
    'models/config/decoder.yaml',
    'models/config/dvae.yaml',
    'models/config/gpt.yaml',
    'models/config/path.yaml',
    'models/config/vocos.yaml'
]

# 检查所有文件是否存在
all_files_exist = all(os.path.exists(file_path) for file_path in required_files)

if all_files_exist:
    print('Load models from local path.')
    chat.load_models(source='local', local_path='models')
else:
    print('Load models from snapshot.')
    chat.load_models()

def text_to_speech(text):

    wavs = chat.infer([text], use_decoder=True)
    audio_data = np.array(wavs[0])
    if audio_data.ndim == 1:
        audio_data = np.expand_dims(audio_data, axis=0)
    if not os.path.exists('outputs'):
        os.makedirs('outputs')
    output_file = f'outputs/{datetime.datetime.now().strftime("%Y%m%d%H%M%S")} - {random.randint(1000, 9999)}.wav'
    sf.write(output_file, audio_data.T, 24000)
    return output_file

# examples
examples = [
    ["你先去做，哪怕做成屎一样，在慢慢改[laugh]，不要整天犹犹豫豫[uv_break]，一个粗糙的开始，就是最好的开始，什么也别管，先去做，然后你就会发现，用不了多久，你几十万就没了[laugh]"],
    ["生活就像一盒巧克力，你永远不知道你会得到什么。"],
    ["每一天都是新的开始，每一个梦想都值得被追寻。"]
]

# create a block
block = gr.Blocks(css="footer.svelte-mpyp5e {display: none !important;}", title='文本转语音').queue()

with block:
    with gr.Row():
        gr.Markdown("## ChatTTS-WebUI     【浩哥聊AI】")
    
    with gr.Row():
        gr.Markdown(
            """
            ### 说明
            - 输入一段文本，点击“生成”按钮。
            - 程序会生成对应的语音文件并显示在右侧。
            - 你可以下载生成的音频文件。
            - 也可以选择一些示例文本进行测试。
            - 作者：浩哥聊AI
            - 欢迎关注我的抖音号：浩哥聊AI。或者加我微信聊一些商业项目：yuhao1029
            """
        )
    
    
    with gr.Row():
        with gr.Column():
            input_text = gr.Textbox(label='输入文本', lines=2, placeholder='请输入文本...')
            example = gr.Examples(
                label="示例文本",
                inputs=input_text,
                examples=examples,
                examples_per_page=3,
            )
        
        with gr.Column():
            output_audio = gr.Audio(label='生成的音频', type='filepath', show_download_button=True)
        
    with gr.Column():
        run_button = gr.Button(value="生成")
    
    

    run_button.click(fn=text_to_speech, inputs=input_text, outputs=output_audio)

# launch
block.launch(server_name='127.0.0.1', server_port=9527, share=True)
