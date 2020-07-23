from logging import getLogger
from invoke import task


logger = getLogger(__name__)


@task
def tests(context, coverage=True, pycodestyle=True, verbose=True):
    """Run test suit."""
    logger.info("Running test suit")
    context.run("nosetests -v --with-coverage")
    context.run("pycodestyle --benchmark")


@task
def docs(context, docs=False):
    """Generate documentation."""
    logger.info("Building documentation")
    if docs:
        context.run("echo sphinx-build")


@task
def clean(context, bytecode=False, extra=''):
    """Clean up ignored files and cache."""
    logger.info("Cleaning cache files")
    context.run("find . -type f -name \"*.py[co]\" -delete")
    context.run("find . -type d -name \"__pycache__\" -exec rm -r {} +")
    context.run("git clean -f -d")  # remove directories
    context.run("git clean -f -X")  # remove ignored filesi


@task
def server(context):
    """Start server"""
    logger.info("Starting server")
    context.run(
        "python dockerboard/manage.py runserver 0.0.0.0:8000",
        pty=True,
    )


@task
def worker(context):
    """Start workers"""
    logger.info("Starting worker")
    context.run(
        "celery worker -A dockerboard.api.tasks -l info",
        pty=True,
    )


