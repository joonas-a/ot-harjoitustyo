from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def start2(ctx):
    ctx.run("python src/index.py", pty=False) #tasks ending with a '2' are meant to be run on a windows 11 machine

@task
def test(ctx):
    ctx.run("pytest src", pty=True)

@task
def test2(ctx):
    ctx.run("pytest src", pty=False)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)


@task
def coverage2(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=False)

@task(coverage2)
def coverage_report2(ctx):
    ctx.run("coverage html", pty=False)

@task
def pylint(ctx):
    ctx.run("pylint src", pty=True)

@task
def pylint2(ctx):
    ctx.run("pylint src", pty=False)

@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src", pty=True)

@task
def build(ctx):
    ctx.run("python src/initialize_database.py")
