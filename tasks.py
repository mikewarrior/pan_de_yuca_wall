from task.test import test_collection
from invoke import Collection


ns = Collection()
ns.add_collection(test_collection)
