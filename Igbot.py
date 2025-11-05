from instagrapi import Client
import os
import time

#Credentials ko environment variables me store karna safe hai
USERNAME = os.getenv("INSTA_USERNAME")
PASSWORD = os.getenv("INSTA_PASSWORD")
SESSION_FILE = "insta_session.json"

#Instagram client initialize karo
cl = Client()

#Pehle session load karne ki koshish karo
if os.path.exists(SESSION_FILE):
    cl.load_settings(SESSION_FILE)
    cl.login(USERNAME, PASSWORD)
else:
    cl.login(USERNAME, PASSWORD)
    cl.dump_settings(SESSION_FILE)

#Auto-reply function
def send_auto_reply(target_username, message):
    try:
        user_id = cl.user_id_from_username(target_username)
        cl.direct_send(message, [user_id])
        print(f"Sent message to {target_username}")
    except Exception as e:
        print(f"Error sending message: {e}")

#Example target user and message
TARGET_USER = os.getenv("TARGET_USERNAME")
MESSAGE = os.getenv("AUTO_REPLY_MESSAGE", "WELCOME TO GROUP 🥰🖐🏼\nTHIS BOT OWNER IS MR_JAXX")

#Loop for periodic messages (5 min interval)
while True:
    send_auto_reply(TARGET_USER, MESSAGE)
    time.sleep(300)
