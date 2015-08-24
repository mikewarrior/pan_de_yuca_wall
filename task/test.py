from invoke import task, Collection
import subprocess


@task
def unit():
    print 'Running unit tests'
    subprocess.call(['nosetests', 'test/unit'])

@task
def integration():
    print 'Running integration tests'
    subprocess.call(['nosetests', 'test/integration'])

@task(pre=[unit, integration], default=True)
def all_tests():
    pass

test_collection = Collection('test')
test_collection.add_task(unit)
test_collection.add_task(integration)
test_collection.add_task(all_tests, 'all')
