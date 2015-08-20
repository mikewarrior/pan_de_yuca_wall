from nose.tools import *
from pymongo import MongoClient
from app.team_member import TeamMember
from app.repository import Repository

class TestRepository:

    def setUp(self):
        self.database = MongoClient().test_yuca

    def test_persists_team_member(self):
        repository = Repository(self.database)

        team_member = TeamMember('Cris')

        repository.insert(team_member)

        persisted = self.database.team_members.find().next()

        assert_equal('Cris', persisted['name'])
        assert_equal(0, persisted['late_days'])

    def tearDown(self):
        self.database.team_members.drop()
