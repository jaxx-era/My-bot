from instagrapi import Client
import os
import time

USERNAME = os.getenv("INSTA_USERNAME")
PASSWORD = os.getenv("INSTA_PASSWORD")
SESSION_FILE = "insta_session.json"

cl = Client()

if os.path.exists(SESSION_FILE):
    cl.load_settings(SESSION_FILE)
    cl.login(USERNAME, PASSWORD)
else:
    cl.login(USERNAME, PASSWORD)
    cl.dump_settings(SESSION_FILE)

REPLIES = {
    ("hii", "hello", "hey", "hy", "hoi", "hiya", "sup", "yo"): "Hlw",
    ("how are you", "hry", "hru", "kaise ho", "kese ho", "kya haal hai"): "I'm good 😊, how are you?",
    ("wryd", "what are you doing", "kkrh", "kya kar rahe ho", "kya kr rahe ho", "kya kar rahe ho aaj"): "Nothing! What are you doing?",
    ("khana khaya", "khana kha liya", "khana ho gaya", "kha liya?", "food khaya?"): "Ha ho gaya! Apka hua?",
    ("kaha se ho", "where are you from", "kaha rehete ho", "kaha rehte ho", "tum kaha se ho"): "Mumbai se hu! Aur aap kaha se ho?",
    ("so rahe ho", "tired", "thak gaye", "so rahe ho kya"): "Nahi abhi jag raha hu 😎, tum?",
    ("bored", "bore ho raha hu", "udaas", "sad"): "Chill karo, sab theek hoga 😌",
    ("miss you", "love you", "luv u", "i love you"): "Aww 😊, miss you too!"
}

def check_and_reply(thread):
    last_msg = thread.items[-1].text.lower()
sender_username = thread.items[-1].user.username
    for keys, reply in REPLIES.items():
        if any(word in last_msg for word in keys):
            cl.direct_send(f"@{sender_username} {reply}", [thread.id])
            print(f"Replied to {sender_username} with: {reply}")
            break

while True:
    threads = cl.direct_threads()
    for thread in threads:
        check_and_reply(thread)
    time.sleep(10)


