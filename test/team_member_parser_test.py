from nose.tools import *
from app.team_member_parser import TeamMemberParser

class TestTeamMemberParser:

    def test_should_return_list_of_team_members(self):
        team_member_file = ['member1']
        parser = TeamMemberParser(team_member_file)
        team_members = parser.get_members()

        assert_equal('member1', team_members[0].name)
