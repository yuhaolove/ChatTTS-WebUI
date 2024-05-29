
# ChatTTS-WebUI

[**English**](./README.md) | [**中文简体**](./README_CN.md)

## 项目介绍
这是一个依赖于[ChatTTS](https://github.com/2noise/ChatTTS)项目的人工智能项目。该项目包括一个Web用户界面，用户可以通过该界面与模型进行交互。

觉得好用 记得给个star哦

## 项目结构
```plaintext
my_ai_project/
│
├── ChatTTS               # ChatTTS项目的克隆目录
│  └── ChatTTS            
│      ├── experimental   
│      ├── infer          
│      ├── model          
│      └── utils          
├── environment           # 虚拟环境目录，包含所有依赖包
├── models                # 模型文件目录
│  ├── asset              
│  └── config             
├── outputs               # 输出文件目录（如日志、结果等）
├── webui                 # Web用户界面代码目录
│  ├── main.py            # Web用户界面的主入口文件
│  └── ...                # 其他Web用户界面相关文件
├── install.bat           # 一键安装脚本，用于安装和配置项目
├── run_webui.bat         # 启动Web用户界面的脚本
├── update.bat            # 更新ChatTTS项目的脚本
├── update_chatts.py      # 更新ChatTTS项目的Python脚本
└── requirements.txt      # 项目依赖文件

```

## 安装方式

### 手动安装
1. **安装Conda**：
   前往[Conda官网](https://docs.conda.io/en/latest/miniconda.html)下载并安装Miniconda或Anaconda。


2. **克隆本项目**：
   ```sh
   git clone https://github.com/yuhaolove/ChatTTS-WebUI.git
   ```

3. **创建并激活虚拟环境**：
   ```sh
   cd ChatTTS-WebUI
   conda create -n chattts_webui python=3.12.3
   conda activate chattts_webui
   ```

4. **克隆ChatTTS仓库**：
   ```sh
   cd ChatTTS-WebUI
   git clone https://github.com/2noise/ChatTTS.git
   ```

5. **安装ChatTTS依赖**：
   ```sh
   cd ChatTTS
   pip install -r requirements.txt
   cd ..
   ```

5. **安装本项目WebUI的依赖**：
   ```sh
   pip install -r requirements.txt
   ```

### Windows下一键安装包模式
1. **下载并运行安装脚本**：
   点击此处下载 一键安装包
   首次使用请双击或在命令行中运行`install.bat`。安装完成后将直接启动webui
   后续的使用直接双击run_webui.bat即可


## 启动方式

### Windows下
双击或在命令行中运行`run_webui.bat`启动Web用户界面：
```sh
run_webui.bat
```

### 其他系统
暂未测试，可以直接使用Conda的Python启动：
```sh
python webui/main.py
```

## 手动安装模型文件
如果无法顺利下载HF的模型文件，可以手动下载并放置在对应的目录中。

1. **下载模型文件**：
   前往[模型下载地址](https://www.modelscope.cn/models/pzc163/chatTTS/files)下载模型文件。

2. **将文件放置到对应目录**：
   ```plaintext
   ├─models
   │  ├─asset
   │  └─config
   ```

## 注意事项
- 确保你具有稳定的网络连接，以便下载依赖和克隆仓库。

## 联系方式
如果你有任何问题或需要帮助，请联系[浩哥聊AI]。
![支付宝二维码](assets/haogeai.png)

## 赞赏

如果你觉得这个项目对你有帮助，欢迎考虑给予一些支持。你的赞赏将帮助我继续开发和维护这个项目，并带来更多有用的功能和改进。

你也可以扫描以下二维码进行赞赏：

#### 支付宝
![支付宝二维码](assets/alipay.png)

#### 微信支付
![微信支付二维码](assets/wechat.png)

### 感谢名单

所有赞赏者的名字（如愿意公开）将会被记录在项目的感谢名单中。感谢你的支持！

