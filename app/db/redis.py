import redis.asyncio as redis
import json


class RedisFeed:
    def __init__(self):
        self.redis = None

    async def connect(self):
        self.redis = await redis.from_url(
            "redis://127.0.0.1:6379", decode_responses=True
        )

    async def close(self):
        if self.redis:
            await self.redis.close()

    async def publish(self, channel, message):
        if self.redis:
            await self.redis.publish(channel, json.dumps(message))


redisFeed = RedisFeed()


async def stream_messages(channel):
    try:
        async with redisFeed.redis.pubsub() as pubsub:
            await pubsub.subscribe(channel)
            async for message in pubsub.listen():
                if message["type"] == "subscribe":
                    continue

                print("New Message: ")
                print(message)
                yield json.dumps(message)
    except Exception as e:
        # print(e)
        return
