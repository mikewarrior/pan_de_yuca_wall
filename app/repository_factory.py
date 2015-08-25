from pymongo import MongoClient
from app.repository import Repository

class RepositoryFactory:

    DATABASE = {
        'test': 'test_yuca',
        'prod': 'prod_yuca'
    }

    @staticmethod
    def create_repository(database):
        database_name = RepositoryFactory.__get_database_name(database)
        uri = 'mongodb://localhost:27017/' + database_name
        database = MongoClient(uri).get_default_database()
        return Repository(database)

    @staticmethod
    def __get_database_name(database):
        try:
            return RepositoryFactory.DATABASE[database]
        except KeyError:
            raise KeyError('Database not found')
