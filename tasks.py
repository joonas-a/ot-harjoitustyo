from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def start2(ctx):
    ctx.run("python src/index.py", pty=False) #tasks ending with a '2' are meant to be run on a windows 11 machine

@task
def tests(ctx):
    ctx.run("pytest src", pty=True)

@task
def tests2(ctx):
    ctx.run("pytest src", pty=False)