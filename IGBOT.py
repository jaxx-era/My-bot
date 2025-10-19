import os
from instagrapi import Client
import time

USERNAME = os.getenv("IG_USERNAME")
PASSWORD = os.getenv("IG_PASSWORD")

cl = Client()
cl.login(USERNAME, PASSWORD)

REPLIED_USERS = set()

while True:
    inbox = cl.direct_threads()
    for thread in inbox:
        user_id = thread.users[0].pk
        username = thread.users[0].username

        if user_id not in REPLIED_USERS:
            message = f"WELCOME TO GROUP 🥰🖐🏼\n@{username}\n\nTHIS BOT OWNER IS MR_JAXX"
            cl.direct_send(message, [user_id])
            REPLIED_USERS.add(user_id)
            time.sleep(300)

    time.sleep(10)
