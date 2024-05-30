import os
import sys
import subprocess
import pygit2
from datetime import datetime

def pull(repo, remote_name='origin', branch='main'):
    for remote in repo.remotes:
        if remote.name == remote_name:
            remote.fetch()
            remote_master_id = repo.lookup_reference('refs/remotes/origin/%s' % (branch)).target
            merge_result, _ = repo.merge_analysis(remote_master_id)
            if merge_result & pygit2.GIT_MERGE_ANALYSIS_UP_TO_DATE:
                return
            elif merge_result & pygit2.GIT_MERGE_ANALYSIS_FASTFORWARD:
                repo.checkout_tree(repo.get(remote_master_id))
                try:
                    master_ref = repo.lookup_reference('refs/heads/%s' % (branch))
                    master_ref.set_target(remote_master_id)
                except KeyError:
                    repo.create_branch(branch, repo.get(remote_master_id))
                repo.head.set_target(remote_master_id)
            elif merge_result & pygit2.GIT_MERGE_ANALYSIS_NORMAL:
                repo.merge(remote_master_id)
                if repo.index.conflicts is not None:
                    for conflict in repo.index.conflicts:
                        print('Conflicts found in:', conflict[0].path)
                    raise AssertionError('Conflicts, ahhhhh!!')
                user = repo.default_signature
                tree = repo.index.write_tree()
                commit = repo.create_commit('HEAD',
                                            user,
                                            user,
                                            'Merge!',
                                            tree,
                                            [repo.head.target, remote_master_id])
                repo.state_cleanup()
            else:
                raise AssertionError('Unknown merge analysis result')

def update_repo(repo_url, repo_path):
    pygit2.option(pygit2.GIT_OPT_SET_OWNER_VALIDATION, 0)

    if not os.path.exists(repo_path):
        print(f"Cloning {repo_url} repository...")
        pygit2.clone_repository(repo_url, repo_path)

    repo = pygit2.Repository(repo_path)
    ident = pygit2.Signature('chattts_updater', 'chattts@updater.com')
    try:
        print("Stashing current changes...")
        repo.stash(ident)
    except KeyError:
        print("Nothing to stash.")
    backup_branch_name = 'backup_branch_{}'.format(datetime.today().strftime('%Y-%m-%d_%H_%M_%S'))
    print(f"Creating backup branch: {backup_branch_name}")
    try:
        repo.branches.local.create(backup_branch_name, repo.head.peel())
    except:
        pass

    print("Checking out main branch...")
    branch = repo.lookup_branch('main')
    ref = repo.lookup_reference(branch.name)
    repo.checkout(ref)

    print("Pulling latest changes...")
    pull(repo)

    print("Installing dependencies...")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', os.path.join(repo_path, 'requirements.txt')])

    print("Done!")

# 更新ChatTTS仓库
update_repo("https://github.com/2noise/ChatTTS.git", "ChatTTS")

# 更新ChatTTS-WebUI仓库
update_repo("https://github.com/yuhaolove/ChatTTS-WebUI.git", "ChatTTS-WebUI")
