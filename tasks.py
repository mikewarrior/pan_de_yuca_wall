from task.test import test_collection
from task.db import db_collection
from invoke import Collection


ns = Collection()
ns.add_collection(test_collection)
ns.add_collection(db_collection)
