import json
from application import yuca_wall
from app.repository_factory import RepositoryFactory
from nose.tools import *
from test.helpers import *
from app.team_member import TeamMember

class TestTeamMemberApi:

    def setUp(self):
        self.repository = RepositoryFactory.create_repository()
        self.test_client = yuca_wall.test_client()

    def test_persists_team_member(self):
        member_name = random_word(10)
        team_member = {
            'name': member_name
        }

        response = self.test_client.post('/api/team_members', data=json.dumps(team_member))

        persisted_team_member = self.repository.get_members()[0]

        assert_equal(201, response.status_code)
        expected_response = '{"late_days": 0, "name": "%s"}' % member_name
        assert_equal(expected_response, response.data)
        assert_equal(member_name, persisted_team_member.name)
        assert_equal(0, persisted_team_member.late_days)

    def test_returns_persisted_team_members(self):
        member_name = random_word(10)
        team_member = TeamMember(member_name)
        self.repository.insert(team_member)

        response = self.test_client.get('/api/team_members')

        assert_equal(200, response.status_code)
        assert_equal('[{"late_days": 0, "name": "%s"}]' % member_name, response.data)

    def tearDown(self):
        self.repository.delete_all()
