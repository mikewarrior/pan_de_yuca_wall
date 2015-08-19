class TeamMember:

    def __init__(self, name, late_days=0):
        self.name = name
        self.late_days = late_days

    def late_again(self):
        self.late_days += 1
