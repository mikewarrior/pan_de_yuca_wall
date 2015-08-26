from pymongo import MongoClient
from pymongo.database import Database
from app.team_member_repository import TeamMemberRepository
from env import config

class RepositoryFactory:

    @staticmethod
    def create_repository():
        db = Database(MongoClient(config.MONGO_HOSTS), config.DB_NAME)
        return TeamMemberRepository(db)
