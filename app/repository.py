

class Repository:
    def __init__(self, database):
        self.database = database

    def insert(self, _team_member):
        team_member = {
            'name': _team_member.name,
            'late_days': _team_member.late_days
            }

        self.database.team_members.insert(team_member)
