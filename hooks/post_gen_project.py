#!/usr/bin/env python
import os
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

if __name__ == '__main__':

    # Deleting files
    print("Creating first commit (needed for PBR to fully work)")
    # Git add all & commit
    msg_commit = "First commit thx to cookiecutter."

    subprocess.call(["git", "init", "."], cwd=PROJECT_DIRECTORY)
    subprocess.call(["git", "add", "."], cwd=PROJECT_DIRECTORY)
    subprocess.call(["git", "commit", "-m", msg_commit], cwd=PROJECT_DIRECTORY)
    print("{} created.".format(PROJECT_DIRECTORY))
