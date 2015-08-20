from nose.tools import *
from test.helpers import *
from app.team_member import TeamMember

class TestTeamMember:

    def setUp(self):
        self.name = random_word(10)

    def test_should_have_team_member_name(self):
        team_member = TeamMember(self.name)
        actual_name = team_member.name
        assert_equal(self.name, actual_name)

    def test_should_have_cero_late_days_by_default(self):
        team_member = TeamMember(self.name)
        late_days = team_member.late_days
        assert_equal(0, late_days)

    def test_should_have_specified_late_days(self):
        late_days = 10
        team_member = TeamMember(self.name, late_days)
        actual_late_days = team_member.late_days
        assert_equal(late_days, actual_late_days)

    def test_should_increase_late_days(self):
        team_member = TeamMember(self.name)
        team_member.late_again()
        assert_equal(1, team_member.late_days)
