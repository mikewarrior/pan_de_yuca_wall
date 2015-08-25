from nose.tools import *
from pymongo import MongoClient
from app.team_member import TeamMember
from app.repository_factory import RepositoryFactory

class TestRepository:

    def setUp(self):
        self.repository = RepositoryFactory.create_repository('test')

    def test_persists_team_member(self):
        team_member = TeamMember('Cris')

        self.repository.insert(team_member)
        persisted = self.repository.database.team_members.find().next()

        assert_equal('Cris', persisted['name'])
        assert_equal(0, persisted['late_days'])

    def test_returns_team_members(self):
        mike = TeamMember('Mike')
        cris = TeamMember('Cris')
        self.repository.insert(mike)
        self.repository.insert(cris)

        team_members = self.repository.get_members()

        assert_equal(2, len(team_members))
        assert_equal('TeamMember', team_members[0].__class__.__name__)

    def test_returns_persisted_data(self):
        pao = TeamMember('Pao', 10)
        self.repository.insert(pao)

        persisted_pao = self.repository.get_members()[0]

        assert_equal('Pao', persisted_pao.name)
        assert_equal(10, persisted_pao.late_days)

    def test_deletes_all_data(self):
        mike = TeamMember('Mike')
        cris = TeamMember('Cris')
        self.repository.insert(mike)
        self.repository.insert(cris)

        self.repository.delete_all()
        team_members = self.repository.get_members()

        assert_equal([], team_members)

    def tearDown(self):
        self.repository.database.team_members.drop()
