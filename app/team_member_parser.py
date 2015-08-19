from team_member import TeamMember

class TeamMemberParser:

    def __init__(self, file):
        self.file = file

    def get_members(self):
        return [TeamMember(name) for name in self.file]
