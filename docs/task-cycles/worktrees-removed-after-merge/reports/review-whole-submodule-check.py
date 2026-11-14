"""Throwaway check by the reviewer: a populated submodule whose changes git is configured to ignore."""
import os
import shutil
import subprocess
import sys

BASE = ".runs/review-whole/sm"
SCRIPT = "task-cycle/remove_merged_worktrees.py"
ENV = {**os.environ, "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1",
       "GIT_AUTHOR_NAME": "T", "GIT_AUTHOR_EMAIL": "t@e.x", "GIT_COMMITTER_NAME": "T",
       "GIT_COMMITTER_EMAIL": "t@e.x"}


def git(cwd, *args, check=True):
    done = subprocess.run(["git", "-c", "protocol.file.allow=always", "-C", cwd, *args],
                          capture_output=True, text=True, env=ENV, stdin=subprocess.DEVNULL)
    if check and done.returncode:
        raise SystemExit(f"git {args} failed: {done.stdout} {done.stderr}")
    return done


def put(path, text="x\n"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


def onerror(func, path, exc):
    os.chmod(path, 0o777)
    func(path)


if os.path.exists(BASE):
    shutil.rmtree(BASE, onerror=onerror)
os.makedirs(BASE)
sub = BASE + "/sub"
git(BASE, "init", "-q", "-b", "main", sub)
put(sub + "/s.txt")
git(sub, "add", "s.txt")
git(sub, "commit", "-q", "-m", "sub")
origin = BASE + "/origin.git"
git(BASE, "init", "-q", "--bare", "-b", "main", origin)
main = BASE + "/main"
git(BASE, "init", "-q", "-b", "main", main)
git(main, "remote", "add", "origin", origin)
put(main + "/.gitignore", ".runs/\n")
put(main + "/a.txt")
git(main, "add", ".gitignore", "a.txt")
git(main, "submodule", "add", sub, ".the-way")
put(main + "/.gitmodules", open(main + "/.gitmodules", encoding="utf-8").read().rstrip("\n") + "\n\tignore = all\n")
git(main, "add", ".gitmodules")
git(main, "commit", "-q", "-m", "root")
git(main, "push", "-q", "-u", "origin", "main")
task = BASE + "/wt/fix-task"
git(main, "worktree", "add", "-q", "-b", "task/fix-task", task)
git(task, "submodule", "update", "--init", "-q")
put(task + "/b.txt")
git(task, "add", "b.txt")
git(task, "commit", "-q", "-m", "work")
git(task, "push", "-q", "origin", "task/fix-task")
git(main, "merge", "--no-ff", "-q", "-m", "Merge pull request", "task/fix-task")
git(main, "push", "-q", "origin", "main")
# an uncommitted change inside the populated submodule, which `ignore = all` hides from status
put(task + "/.the-way/s.txt", "UNCOMMITTED WORK\n")
put(task + "/.the-way/new.txt", "UNCOMMITTED NEW\n")
print("status default :", repr(git(task, "status", "--porcelain").stdout))
print("status none    :", repr(git(task, "status", "--porcelain", "--ignore-submodules=none").stdout))
done = subprocess.run([sys.executable, "-B", SCRIPT, "--repository", main, "--no-fetch", "--apply"],
                      capture_output=True, text=True, env=ENV, cwd=BASE, encoding="utf-8")
print("exit", done.returncode)
for line in done.stdout.splitlines():
    if "fix-task" in line:
        print(line.replace(BASE, "<base>"))
print("task dir exists after:", os.path.exists(task))
