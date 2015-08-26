from app.team_member import TeamMember


class TeamMemberRepository:
    def __init__(self, database):
        self.database = database

    def insert(self, _team_member):
        team_member = {
            'name': _team_member.name,
            'late_days': _team_member.late_days
            }

        self.database.team_members.insert(team_member)

    def get_members(self):
        cursor = self.database.team_members.find()
        return [TeamMember(member['name'], member['late_days']) for member in cursor]

    def delete_all(self):
        self.database.team_members.drop()
