import asyncio
import motor.motor_asyncio
from app.core.config import settings

MONGO_DETAILS = f"mongodb://{settings.DATABASE_URL}"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.portfolio_blog


async def check_mongo_connection():
    try:
        # Send a command to the admin database to check the connection
        result = await client.admin.command("ping")
        print("Connected to MongoDB:", result)
    except Exception as e:
        print("Failed to connect to MongoDB:", e)


# Run the function to check the connection
asyncio.run(check_mongo_connection())
