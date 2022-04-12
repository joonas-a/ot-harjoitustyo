from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def windows(ctx):
    ctx.run("python src/game_loop.py", pty=False)
