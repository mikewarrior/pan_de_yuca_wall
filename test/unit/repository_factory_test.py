from nose.tools import *
from app.repository_factory import RepositoryFactory
from pymongo import MongoClient

class TestRepositoryFactory:

    def test_should_return_selected_database(self):

        expected_test_database = MongoClient().test_yuca
        expected_prod_database = MongoClient().prod_yuca

        actual_test_database = RepositoryFactory.create_repository('test')
        actual_prod_database = RepositoryFactory.create_repository('prod')

        assert_equal(expected_test_database, actual_test_database.database)
        assert_equal(expected_prod_database, actual_prod_database.database)

    def test_returns_exception_if_database_is_not_found(self):

        with assert_raises(KeyError) as context:
            RepositoryFactory.create_repository('')

        assert_equal('Database not found', context.exception.message)
