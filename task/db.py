from invoke import task, Collection
from app.repository_factory import RepositoryFactory


@task
def clean():
    print 'Test database cleaned'
    repository = RepositoryFactory.create_repository('test')
    repository.delete_all()


db_collection = Collection('db')
db_collection.add_task(clean)
