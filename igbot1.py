from instagrapi import Client
import os
import time

USERNAME = os.getenv("INSTA_USERNAME")
PASSWORD = os.getenv("INSTA_PASSWORD")
SESSION_FILE = "insta_session.json"
IGNORE_USERS = ["user_to_skip1", "user_to_skip2"]

cl = Client()

if os.path.exists(SESSION_FILE):
    cl.load_settings(SESSION_FILE)
    cl.login(USERNAME, PASSWORD)
else:
    cl.login(USERNAME, PASSWORD)
    cl.dump_settings(SESSION_FILE)

def send_auto_reply_to_last_message():
    threads = cl.direct_threads()
    if not threads:
        return
    last_thread = threads[0]
    last_message = last_thread.items[-1]
    last_sender = last_message.user.username
    if last_sender not in IGNORE_USERS:
        user_id = cl.user_id_from_username(last_sender)
        reply_text = f"@{last_sender} WELCOME TO GROUP 🥰🖐🏼\nTHIS BOT OWNER IS MR_JAXX"
        cl.direct_send(reply_text, [user_id])

while True:
    send_auto_reply_to_last_message()
    time.sleep(300)
