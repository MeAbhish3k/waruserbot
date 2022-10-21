from random import randint

from instagrapi import Client as IClient
from instagrapi.exceptions import ChallengeRequired, TwoFactorRequired
from pyrogram import Client as PClient
from telethon.sessions import StringSession
from telethon.sync import TelegramClient


def main():
    print("T E A M    R E Z O X B O T   ! !")
    print("Hello!! Welcome to RezoxBot Session Generator\n")
    print("Human Verification Required !!")
    while True:
        verify = int(randint(1, 50))
        okvai = int(input(f"Enter {verify} to continue: "))
        if okvai == verify:
            print("\nChoose the string session type: \n1. RezoxBot (Telethon) \n2. Music Bot (Pyrogram) \n3. Instagram Session")
            while True:
                library = input("\nYour Choice: ")
                if library == "1":
                    generate_telethon_session()
                    break
                elif library == "2":
                    generate_pyro_session()
                    break
                elif library == "3":
                    generate_insta_session()
                    break
                else:
                    print("Please enter integer values (1/2/3 only).")
            break
        else:
            print("Verification Failed! Try Again:")


def generate_pyro_session():
    print("Pyrogram Session for Music Bot!")
    APP_ID = int(input("\nEnter APP ID here: "))
    API_HASH = input("\nEnter API HASH here: ")
    with PClient(':memory:', api_id=APP_ID, api_hash=API_HASH) as hellbot:
        print("\nYour RezoxBot Session Is sent in your Telegram Saved Messages.")
        hellbot.send_message(
            "me",
            f"#RezoxBOT_MUSIC #REZOXBOT_SESSION #PYROGRAM\n\n`{hellbot.export_session_string()}`",
        )


def generate_telethon_session():
    print("\nTelethon Session For WarUserBot!")
    APP_ID = int(input("\nEnter APP ID here: "))
    API_HASH = input("\nEnter API HASH here: ")
    with TelegramClient(StringSession(), APP_ID, API_HASH) as hellbot:
        print("\nYour RezoxBot Session Is sent in your Telegram Saved Messages.")
        hellbot.send_message(
            "me",
            f"#REZOXBOT #REZOXBOT_SESSION #TELETHON \n\n`{hellbot.session.save()}`",
        )


def generate_insta_session():
    print("Instagram Session For WARBot!")
    cl = IClient()
    username = input("Enter your Instagram Username: ")
    password = input("Enter your Instagram Password: ")
    try:
        cl.login(username, password)
        xyz =  cl.get_settings()
        sessionid = xyz['authorization_data']['sessionid']
        print(f"Your Instagram Session is: \n>>> {sessionid}")
        print("\nCopy it from here and remember not to share it with anyone!")
    except (ChallengeRequired, TwoFactorRequired, Exception) as e:
        print(e)


def challenge_code(username, choice):
    while True:
        otp = input("Enter the OTP sent to your Email: ")
        if otp.isdigit():
            break
        else:
            print("Enter digits only!")
    return otp


main()
