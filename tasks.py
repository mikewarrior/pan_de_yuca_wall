from invoke import task
from invoke import Collection
import subprocess


@task
def test_unit():
    print 'Running unit tests'
    subprocess.call(['nosetests', 'test/unit'])

@task
def test_integration():
    print 'Running integration tests'
    subprocess.call(['nosetests', 'test/integration'])
