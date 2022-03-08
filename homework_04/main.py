import asyncio
from models import (
    User,
    Post,
    inittables,
    AsyncScopedSession,
)
from jsonplaceholder_requests import (
    USERS_DATA_URL,
    POSTS_DATA_URL,
    send_request,
)

async def async_main():
    await inittables()
    users = await send_request(USERS_DATA_URL)
    posts = await send_request(POSTS_DATA_URL)
    async with AsyncScopedSession() as session:
        async with session.begin():
            for i in users:
                session.add(User(id=i["id"], name=i["name"], username=i["username"], email=i["email"]))
            for i in posts:
                session.add(Post(id=i["id"], user_id=i["userId"], title=i["title"], body=i["body"]))

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_main())