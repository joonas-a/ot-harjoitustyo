from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/game_loop.py", pty=True)

@task
def windows(ctx):
    ctx.run("python src/game_loop.py", pty=False)