import motor.motor_asyncio
from app.core.config import settings

MONGO_DETAILS = f"mongodb://{settings.DATABASE_URL}"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.portfolio_blog
