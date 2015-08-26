from nose.tools import *
from app.repository_factory import RepositoryFactory


class TestRepositoryFactory:

    def test_creates_repository_instance(self):
        repository = RepositoryFactory.create_repository()
        assert_equal('TeamMemberRepository', repository.__class__.__name__)
