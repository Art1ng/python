"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

import asyncio
from models import User, Post, Session
from jsonplaceholder_requests import fetch_users_data, fetch_posts_data

async def create_users_and_posts(users_data, posts_data):
    async with Session() as session:
        async with session.begin():
            for user_data in users_data:
                user = User(id=user_data["id"], name=user_data["name"], username=user_data["username"], email=user_data["email"])
                session.add(user)

            for post_data in posts_data:
                post = Post(id=post_data["id"], user_id=post_data["userId"], title=post_data["title"], body=post_data["body"])
                session.add(post)

        await session.commit()

async def async_main():
    users_data, posts_data = await asyncio.gather(fetch_users_data(), fetch_posts_data())
    await create_users_and_posts(users_data, posts_data)

def main():
    asyncio.run(async_main())

if __name__ == "__main__":
    main()
