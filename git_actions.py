import subprocess
from os import chdir

def clone_repo(git_path, path=None):
    if path != None: subprocess.run(["git", "clone", git_path, path])
    else: subprocess.run(["git", "clone", git_path])

def commit(message="Updated Repo"):
    subprocess.run(["git", "add", "*"])
    subprocess.run(["git", "commit", "-a", "-m", message])

def push():
    subprocess.run(["git", "push"])

clone_repo("https://github.com/Razboinicul/TestRepo", "TestRepo")
chdir("TestRepo")
file = open("test1", "w").close()
commit("Test Commit 1")
push()