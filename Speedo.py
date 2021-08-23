import os
import sys
import random
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon. sessions import StringSession
from telethon. tl. functions. account import UpdateProfileRequest
from Config import STRING, SUDO, BIO_MESSAGE, API_ID, API_HASH, STRING2, STRING3, STRING4 ,STRING5, STRING6, STRING7, STRING8 ,STRING9, STRING10, HEROKU_API_KEY, HEROKU_APP_NAME
import asyncio
import telethon. utils
from telethon. tl import functions
from telethon. tl. functions. channels import LeaveChannelRequest
from telethon. tl. functions. messages import ImportChatInviteRequest
from Utils import RAID, RRAID
import git
import heroku3

a = API_ID
b = API_HASH
speedo = STRING
speedox = STRING2
speedoxx = STRING3
speedoxxx = STRING4
speedoxxxx = STRING5
sixth = STRING6
seven = STRING7
eight = STRING8
ninth = STRING9
tenth = STRING10


idk = ""
ydk = ""
wdk = ""
sdk = ""
hdk = ""
adk = ""
bdk = ""
cdk = ""
edk = ""
ddk = ""


que = {}

PRO_USERS = []
for x in SUDO:
    PRO_USERS. append(x)
    
async def start_atgk():
    global idk
    global ydk
    global wdk
    global sdk
    global hdk
    global adk
    global bdk
    global cdk
    global ddk
    global edk
    if speedo:
        session_name = str(speedo)
        print("String 1 Found")
        idk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 1")
            await idk. start()
            botme = await idk. get_me()
            await idk(functions.  channels. JoinChannelRequest(channel="@SpeedoSupportOfficial"))
            await idk(functions.  channels. JoinChannelRequest(channel="@Andencento"))
            botid = telethon. utils. get_peer_id(botme)
            PRO_USERS. append(botid)
        except Exception as e:
            idk = "speedo"
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "startup"
        idk = TelegramClient(session_name, a, b)
        try:
            await idk. start()
        except Exception as e:
            pass
   
    if speedox:
        session_name = str(speedox)
        print("String 2 Found")
        ydk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 2")
            await ydk. start()
            await ydk(functions.  channels. JoinChannelRequest(channel="@Andencento"))
            await ydk(functions.  channels. JoinChannelRequest(channel="@SpeedoSupportOfficial"))
            botme = await ydk. get_me()
            botid = telethon. utils. get_peer_id(botme)
            PRO_USERS. append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = "startup"
        ydk = TelegramClient(session_name, a, b)
        try:
            await ydk. start()
        except Exception as e:
            pass

    if speedoxx:
        session_name = str(speedoxx)
        print("String 3 Found")
        wdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 3")
            await wdk. start()
            await wdk(functions.  channels. JoinChannelRequest(channel="@Andencento"))
            await wdk(functions.  channels. JoinChannelRequest(channel="@SpeedoSupportOfficial"))
            botme = await wdk. get_me()
            botid = telethon. utils. get_peer_id(botme)
            PRO_USERS. append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = "startup"
        wdk = TelegramClient(session_name, a, b)
        try:
            await wdk. start()
        except Exception as e:
            pass

    if speedoxxx:
        session_name = str(speedoxxx)
        print("String 4 Found")
        hdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 4")
            await hdk. start()
            await hdk(functions.  channels. JoinChannelRequest(channel="@Andencento"))
            await hdk(functions.  channels. JoinChannelRequest(channel="@SpeedoSupportOfficial"))
            botme = await hdk. get_me()
            botid = telethon. utils. get_peer_id(botme)
            PRO_USERS. append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = "startup"
        hdk = TelegramClient(session_name, a, b)
        try:
            await hdk.start()
        except Exception as e:
            pass

    if speedoxxxx:
        session_name = str(speedoxxxx)
        print("String 5 Found")
        sdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 5")
            await sdk.start()
            await sdk(functions.channels.JoinChannelRequest(channel="@Andencento"))
            await sdk(functions.channels.JoinChannelRequest(channel="@SpeedoSupportOfficial"))
            botme = await sdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            PRO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = "startup"
        sdk = TelegramClient(session_name, a, b)
        try:
            await sdk.start()
        except Exception as e:
            pass
                  
    if sixth:
        session_name = str(sixth)
        print("String 6 Found")
        adk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 6")
            await adk.start()
            await adk(functions.channels.JoinChannelRequest(channel="@Andencento"))
            await adk(functions.channels.JoinChannelRequest(channel="@SpeedoSupportOfficial"))
            botme = await adk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            PRO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        pass
        session_name = "startup"
        adk = TelegramClient(session_name, a, b)
        try:
            await adk.start()
        except Exception as e:
            pass

    if seven:
        session_name = str(seven)
        print("String 7 Found")
        bdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 7")
            await bdk.start()
            await bdk(functions.channels.JoinChannelRequest(channel="@Andencento"))
            await bdk(functions.channels.JoinChannelRequest(channel="@SpeedoSupportOfficial"))
            botme = await bdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            PRO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        pass
        session_name = "startup"
        bdk = TelegramClient(session_name, a, b)
        try:
            await bdk. start()
        except Exception as e:
            pass    
        
    
    if eight:
        session_name = str(eight)
        print("String 8 Found")
        cdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 8")
            await cdk. start()
            await cdk(functions.  channels. JoinChannelRequest(channel="@Andencento"))
            await cdk(functions.  channels. JoinChannelRequest(channel="@SpeedoSupportOfficial"))
            botme = await cdk. get_me()
            botid = telethon. utils. get_peer_id(botme)
            PRO_USERS. append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        pass
        session_name = "startup"
        cdk = TelegramClient(session_name, a, b)
        try:
            await cdk. start()
        except Exception as e:
            pass   
        
    if ninth:
        session_name = str(ninth)
        print("String 9 Found")
        ddk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 9")
            await ddk. start()
            await ddk(functions.  channels. JoinChannelRequest(channel="@Andencento"))
            await ddk(functions.  channels. JoinChannelRequest(channel="@SpeedoSupportOfficial"))
            botme = await ddk. get_me()
            botid = telethon. utils. get_peer_id(botme)
            PRO_USERS. append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        pass
        session_name = "startup"
        ddk = TelegramClient(session_name, a, b)
        try:
            await ddk. start()
        except Exception as e:
            pass   
    
  
    if tenth:
        session_name = str(tenth)
        print("String 10 Found")
        edk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 10")
            await edk. start()
            await edk(functions.  channels. JoinChannelRequest(channel="@Andencento"))
            await edk(functions.  channels. JoinChannelRequest(channel="@SpeedoSupportOfficial"))
            botme = await edk. get_me()
            botid = telethon. utils. get_peer_id(botme)
            PRO_USERS. append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 not Found")
        pass
        session_name = "startup"
        edk = TelegramClient(session_name, a, b)
        try:
            await edk. start()
        except Exception as e:
            pass 

loop = asyncio. get_event_loop()
loop. run_until_complete(start_atgk())       

async def gifspam(e, speedo):
    try:
        await e. client(
            functions. messages. SaveGifRequest(
                id=types. InputDocument(
                    id=sandy. media. document. id,
                    access_hash=speedo. media. document. access_hash,
                    file_reference=speedo. media. document. file_reference,
                ),
                unsave=True,
            )
        )
    except Exception as e:
        pass


@idk. on(events.  NewMessage(incoming=True, pattern=r"\.bio"))
@ydk. on(events.  NewMessage(incoming=True, pattern=r"\.bio"))
@wdk. on(events.  NewMessage(incoming=True, pattern=r"\.bio"))
@hdk. on(events.  NewMessage(incoming=True, pattern=r"\.bio"))
@sdk. on(events.  NewMessage(incoming=True, pattern=r"\.bio"))
@adk. on(events.  NewMessage(incoming=True, pattern=r"\.bio"))
@bdk. on(events.  NewMessage(incoming=True, pattern=r"\.bio"))
@cdk. on(events.  NewMessage(incoming=True, pattern=r"\.bio"))
@edk. on(events.  NewMessage(incoming=True, pattern=r"\.bio"))
@ddk. on(events.  NewMessage(incoming=True, pattern=r"\.bio"))        
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗼\n\nCommand:\n\n.bio <Message to set Bio of Userbot accounts>"
    if e. sender_id in PRO_USERS:
        atgk = ("".  join(e.  text. split(maxsplit=1)[1:])). split(" ", 1)     
        if len(e.  text) > 5:
            bio = str(atgk[0])
            text = "Changing Bio"
            event = await e. reply(text, parse_mode=None, link_preview=None )
            try:
                await e. client(functions.  account. UpdateProfileRequest(about=bio))
                await event. edit("Succesfully Changed Bio")
            except Exception as e:
                await event. edit(str(e))   
        else:
            await e. reply(usage, parse_mode=None, link_preview=None )
            
@idk. on(events.  NewMessage(incoming=True, pattern=r"\.join"))
@ydk. on(events.  NewMessage(incoming=True, pattern=r"\.join"))
@wdk. on(events.  NewMessage(incoming=True, pattern=r"\.join"))
@hdk. on(events.  NewMessage(incoming=True, pattern=r"\.join"))
@sdk. on(events.  NewMessage(incoming=True, pattern=r"\.join"))
@adk. on(events.  NewMessage(incoming=True, pattern=r"\.join"))
@bdk. on(events.  NewMessage(incoming=True, pattern=r"\.join"))
@cdk. on(events.  NewMessage(incoming=True, pattern=r"\.join"))
@edk. on(events.  NewMessage(incoming=True, pattern=r"\.join"))
@ddk. on(events.  NewMessage(incoming=True, pattern=r"\.join"))        
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.join <Public Channel or Group Link/Username>"
    if e. sender_id in PRO_USERS:
        atgk = ("".  join(e.  text. split(maxsplit=1)[1:])). split(" ", 1)
        if len(e.  text) > 6:
            bc = atgk[0]
            text = "Joining..."
            event = await e. reply(text, parse_mode=None, link_preview=None )
            try:
                await e. client(functions.  channels. JoinChannelRequest(channel=bc))
                await event. edit("Succesfully Joined")
            except Exception as e:
                await event. edit(str(e))   
        else:
            await e. reply(usage, parse_mode=None, link_preview=None )
            
@idk. on(events.  NewMessage(incoming=True, pattern=r"\.pjoin"))
@ydk. on(events.  NewMessage(incoming=True, pattern=r"\.pjoin"))
@wdk. on(events.  NewMessage(incoming=True, pattern=r"\.pjoin"))
@hdk. on(events.  NewMessage(incoming=True, pattern=r"\.pjoin"))
@sdk. on(events.  NewMessage(incoming=True, pattern=r"\.pjoin"))
@adk. on(events.  NewMessage(incoming=True, pattern=r"\.pjoin"))
@bdk. on(events.  NewMessage(incoming=True, pattern=r"\.pjoin"))
@cdk. on(events.  NewMessage(incoming=True, pattern=r"\.pjoin"))
@edk. on(events.  NewMessage(incoming=True, pattern=r"\.pjoin"))
@ddk. on(events.  NewMessage(incoming=True, pattern=r"\.pjoin"))        
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.pjoin <Private Channel or Group's access hash>\n\nExample :\nLink = https://t.me/joinchat/HGYs1wvsPUplMmM1\n\n.pjoin HGYs1wvsPUplMmM1"
    if e. sender_id in PRO_USERS:
        atgk = ("".  join(e.  text. split(maxsplit=1)[1:])). split(" ", 1)
        if len(e.  text) > 7:
            bc = atgk[0]
            text = "Joining...."
            event = await e. reply(text, parse_mode=None, link_preview=None )
            try:
                await e. client(ImportChatInviteRequest(bc))
                await event. edit("Succesfully Joined")
            except Exception as e:
                await event. edit(str(e))   
        else:
            await e. reply(usage, parse_mode=None, link_preview=None )
            
        
@idk. on(events.  NewMessage(incoming=True, pattern=r"\.leave"))
@ydk. on(events.  NewMessage(incoming=True, pattern=r"\.leave"))
@wdk. on(events.  NewMessage(incoming=True, pattern=r"\.leave"))
@hdk. on(events.  NewMessage(incoming=True, pattern=r"\.leave"))
@sdk. on(events.  NewMessage(incoming=True, pattern=r"\.leave"))
@adk. on(events.  NewMessage(incoming=True, pattern=r"\.leave"))
@bdk. on(events.  NewMessage(incoming=True, pattern=r"\.leave"))
@cdk. on(events.  NewMessage(incoming=True, pattern=r"\.leave"))
@edk. on(events.  NewMessage(incoming=True, pattern=r"\.leave"))
@ddk. on(events.  NewMessage(incoming=True, pattern=r"\.leave"))        
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗟𝗲𝗮𝘃𝗲\n\nCommand:\n\n.leave <Channel or Chat ID>"
    if e. sender_id in PRO_USERS:
        atgk = ("".  join(e.  text. split(maxsplit=1)[1:])). split(" ", 1)
        if len(e.  text) > 7:
            bc = atgk[0]
            bc = int(bc)
            text = "Leaving....."
            event = await e. reply(text, parse_mode=None, link_preview=None )
            try:
                await event. client(LeaveChannelRequest(bc))
                await event. edit("Succesfully Left")
            except Exception as e:
                await event. edit(str(e))   
        else:
            await e. reply(usage, parse_mode=None, link_preview=None )
            
                
        
        
@idk. on(events.  NewMessage(incoming=True, pattern=r"\.spam"))
@ydk. on(events.  NewMessage(incoming=True, pattern=r"\.spam"))
@wdk. on(events.  NewMessage(incoming=True, pattern=r"\.spam"))
@hdk. on(events.  NewMessage(incoming=True, pattern=r"\.spam"))
@sdk. on(events.  NewMessage(incoming=True, pattern=r"\.spam"))
@adk. on(events.  NewMessage(incoming=True, pattern=r"\.spam"))
@bdk. on(events.  NewMessage(incoming=True, pattern=r"\.spam"))
@cdk. on(events.  NewMessage(incoming=True, pattern=r"\.spam"))
@edk. on(events.  NewMessage(incoming=True, pattern=r"\.spam"))
@ddk. on(events.  NewMessage(incoming=True, pattern=r"\.spam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗦𝗽𝗮𝗺\n\nCommand:\n\n.spam <count> <message to spam>\n\n.spam <count> <reply to a message>\n\nCount must be a integer."
    error = "Spam Module can only be used till 100 count. For bigger spams use BigSpam."
    if e. sender_id in PRO_USERS:
        if e. text[0]. isalpha() and e. text[0] in ("/", "#", "@", "!"):
            return await e. reply(usage, parse_mode=None, link_preview=None )
        atgk = ("".  join(e.  text. split(maxsplit=1)[1:])). split(" ", 1)
        speedo = await e. get_reply_message()
        if len(atgk) == 2:
            message = str(atgk[1])
            counter = int(atgk[0])
            if counter > 100:
                return await e. reply(error, parse_mode=None, link_preview=None )
            await asyncio. wait([e.  respond(message) for i in range(counter)])
        elif e. reply_to_msg_id and speedo. media: 
            counter = int(yukki[0])
            if counter > 100:
                return await e. reply(error, parse_mode=None, link_preview=None )
            for _ in range(counter):
                speedo = await e. client. send_file(e.  chat_id, speedo, caption=speedo. text)
                await gifspam(e, speedo)  
        elif e. reply_to_msg_id and speedo. text:
            message = speedo. text
            counter = int(atgk[0])
            if counter > 100:
                return await e. reply(error, parse_mode=None, link_preview=None )
            await asyncio. wait([e.  respond(message) for i in range(counter)])
        else:
            await e. reply(usage, parse_mode=None, link_preview=None )
            

@idk. on(events.  NewMessage(incoming=True, pattern=r"\.delayspam"))
@ydk. on(events.  NewMessage(incoming=True, pattern=r"\.delayspam"))
@wdk. on(events.  NewMessage(incoming=True, pattern=r"\.delayspam"))
@hdk. on(events.  NewMessage(incoming=True, pattern=r"\.delayspam"))
@sdk. on(events.  NewMessage(incoming=True, pattern=r"\.delayspam"))
@adk. on(events.  NewMessage(incoming=True, pattern=r"\.delayspam"))
@bdk. on(events.  NewMessage(incoming=True, pattern=r"\.delayspam"))
@cdk. on(events.  NewMessage(incoming=True, pattern=r"\.delayspam"))
@edk. on(events.  NewMessage(incoming=True, pattern=r"\.delayspam"))
@ddk. on(events.  NewMessage(incoming=True, pattern=r"\.delayspam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗹𝗮𝘆𝗦𝗽𝗮𝗺\n\nCommand:\n\n.delayspam <sleep time> <count> <message to spam>\n\n.delayspam <sleep time> <count> <reply to a message>\n\nCount and Sleeptime must be a integer."
    if e. sender_id in PRO_USERS:
        if e. text[0]. isalpha() and e. text[0] in ("/", "#", "@", "!"):
            return await e. reply(usage, parse_mode=None, link_preview=None )
        speedo = await e. get_reply_message()
        atgk = "". join(e.  text. split(maxsplit=1)[1:]). split(" ", 2)
        atgksexy = atgk[1:]
        if len(atgksexy) == 2:
            message = str(atgksexy[1])
            counter = int(atgksexy[0])
            sleeptime = float(atgk[0])
            for _ in range(counter):
                async with e. client. action(e.  chat_id, "typing"):
                    if e. reply_to_msg_id:
                        await speedo. reply(message)
                    else:
                        await e. client. send_message(e.  chat_id, message)
                    await asyncio. sleep(sleeptime)
        elif e. reply_to_msg_id and speedo. media: 
            counter = int(atgksexy[0])
            sleeptime = float(atgk[0])
            for _ in range(counter):
                async with e. client. action(e.  chat_id, "document"):
                    speedo = await e. client. send_file(e.  chat_id, speedo, caption=speedo. text)
                    await gifspam(e, speedo) 
                await asyncio. sleep(sleeptime)
        elif e. reply_to_msg_id and speedo. text:
            message = speedo. text
            counter = int(atgksexy[0])
            sleeptime = float(atgk[0])
            for _ in range(counter):
                async with e. client. action(e.  chat_id, "typing"):
                    await e. client. send_message(e.  chat_id, message)
                    await asyncio. sleep(sleeptime)
        else:
            await e. reply(usage, parse_mode=None, link_preview=None )


@idk. on(events.  NewMessage(incoming=True, pattern=r"\.bigspam"))
@ydk. on(events.  NewMessage(incoming=True, pattern=r"\.bigspam"))
@wdk. on(events.  NewMessage(incoming=True, pattern=r"\.bigspam"))
@hdk. on(events.  NewMessage(incoming=True, pattern=r"\.bigspam"))
@sdk. on(events.  NewMessage(incoming=True, pattern=r"\.bigspam"))
@adk. on(events.  NewMessage(incoming=True, pattern=r"\.bigspam"))
@bdk. on(events.  NewMessage(incoming=True, pattern=r"\.bigspam"))
@cdk. on(events.  NewMessage(incoming=True, pattern=r"\.bigspam"))
@edk. on(events.  NewMessage(incoming=True, pattern=r"\.bigspam"))
@ddk. on(events.  NewMessage(incoming=True, pattern=r"\.bigspam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗴𝗦𝗽𝗮𝗺\n\nCommand:\n\n.bigspam <count> <message to spam>\n\n.bigspam <count> <reply to a message>\n\nCount must be a integer."
    if e. sender_id in PRO_USERS:
        if e. text[0]. isalpha() and e. text[0] in ("/", "#", "@", "!"):
            return await e. reply(usage, parse_mode=None, link_preview=None )
        atgk = ("".  join(e.  text. split(maxsplit=1)[1:])). split(" ", 1)
        speedo = await e. get_reply_message()
        if len(atgk) == 2:
            message = str(atgk[1])
            counter = int(atgk[0])
            for _ in range(counter):
                async with e. client. action(e.  chat_id, "typing"):
                    if e. reply_to_msg_id:
                        await speedo. reply(message)
                    else:
                        await e. client. send_message(e.  chat_id, message)
                    await asyncio. sleep(0.3)
        elif e. reply_to_msg_id and speedo. media: 
            counter = int(atgk[0])
            for _ in range(counter):
                async with e. client. action(e.  chat_id, "document"):
                    speedo = await e. client. send_file(e.  chat_id, speedo, caption=speedo. text)
                    await gifspam(e, speedo) 
                await asyncio. sleep(0.3)  
        elif e. reply_to_msg_id and speedo. text:
            message = speedo. text
            counter = int(atgk[0])
            for _ in range(counter):
                async with e. client. action(e.  chat_id, "typing"):
                    await e. client. send_message(e.  chat_id, message)
                    await asyncio. sleep(0.3)
        else:
            await e. reply(usage, parse_mode=None, link_preview=None )


@idk. on(events.  NewMessage(incoming=True, pattern=r"\.raid"))
@ydk. on(events.  NewMessage(incoming=True, pattern=r"\.raid"))
@wdk. on(events.  NewMessage(incoming=True, pattern=r"\.raid"))
@hdk. on(events.  NewMessage(incoming=True, pattern=r"\.raid"))
@sdk. on(events.  NewMessage(incoming=True, pattern=r"\.raid"))
@adk. on(events.  NewMessage(incoming=True, pattern=r"\.raid"))
@bdk. on(events.  NewMessage(incoming=True, pattern=r"\.raid"))
@cdk. on(events.  NewMessage(incoming=True, pattern=r"\.raid"))
@edk. on(events.  NewMessage(incoming=True, pattern=r"\.raid"))
@ddk. on(events.  NewMessage(incoming=True, pattern=r"\.raid"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗮𝗶𝗱\n\nCommand:\n\n.raid <count> <Username of User>\n\n.raid <count> <reply to a User>\n\nCount must be a integer."
    if e. sender_id in PRO_USERS:
        if e. text[0]. isalpha() and e. text[0] in ("/", "#", "@", "!"):
            return await e. reply(usage, parse_mode=None, link_preview=None )
        atgk = ("".  join(e.  text. split(maxsplit=1)[1:])). split(" ", 1)
        speedo = await e. get_reply_message()
        if len(atgk) == 2:
            message = str(atgk[1])
            print(message)
            a = await e. client. get_entity(message)
            g = a. id
            c = a. first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(atgk[0])
            for _ in range(counter):
                reply = random. choice(RAID)
                caption = f"{username}   {reply}"
                async with e. client. action(e.  chat_id, "typing"):
                    await e. client. send_message(e.  chat_id, caption)
                    await asyncio. sleep(0.3)
        elif e. reply_to_msg_id: 
            a = await e. get_reply_message()
            b = await e. client. get_entity(a.  sender_id)
            g = b. id
            c = b. first_name
            counter = int(atgk[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random. choice(RAID)
                caption = f"{username}   {reply}"
                async with e. client. action(e.  chat_id, "typing"):
                    await e. client. send_message(e.  chat_id, caption)
                    await asyncio. sleep(0.3)
        else:
            await e. reply(usage, parse_mode=None, link_preview=None )





@idk. on(events.  NewMessage(incoming=True))
@ydk. on(events.  NewMessage(incoming=True))
@wdk. on(events.  NewMessage(incoming=True))
@hdk. on(events.  NewMessage(incoming=True))
@sdk. on(events.  NewMessage(incoming=True))
@adk. on(events.  NewMessage(incoming=True))
@bdk. on(events.  NewMessage(incoming=True))
@cdk. on(events.  NewMessage(incoming=True))
@edk. on(events.  NewMessage(incoming=True))
@ddk. on(events.  NewMessage(incoming=True))
async def _(event):
    global que
    queue = que. get(event.  sender_id)
    if not queue:
        return
    async with event. client. action(event.  chat_id, "typing"):
        await asyncio. sleep(0.3)
    async with event. client. action(event.  chat_id, "typing"):
        await event. client. send_message(
            entity=event. chat_id,
            message="""{}""". format(random.  choice(RRAID)),
            reply_to=event. message. id,
        )           
            
            
@idk. on(events.  NewMessage(incoming=True, pattern=r"\.replyraid"))
@ydk. on(events.  NewMessage(incoming=True, pattern=r"\.replyraid"))
@wdk. on(events.  NewMessage(incoming=True, pattern=r"\.replyraid"))
@hdk. on(events.  NewMessage(incoming=True, pattern=r"\.replyraid"))
@sdk. on(events.  NewMessage(incoming=True, pattern=r"\.replyraid"))
@adk. on(events.  NewMessage(incoming=True, pattern=r"\.replyraid"))
@bdk. on(events.  NewMessage(incoming=True, pattern=r"\.replyraid"))
@cdk. on(events.  NewMessage(incoming=True, pattern=r"\.replyraid"))
@edk. on(events.  NewMessage(incoming=True, pattern=r"\.replyraid"))
@ddk. on(events.  NewMessage(incoming=True, pattern=r"\.replyraid"))
async def _(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.replyraid <Username of User>\n\n.replyraid <reply to a User>"
    if e. sender_id in PRO_USERS:
        if e. text[0]. isalpha() and e. text[0] in ("/", "#", "@", "!"):
            return await e. reply(usage, parse_mode=None, link_preview=None )
        atgk = ("".  join(e.  text. split(maxsplit=1)[1:])). split(" ", 1)
        speedo = await e. get_reply_message()
        if len(e.  text) > 11:
            message = str(atgk[0])
            a = await e. client. get_entity(message)
            g = a. id
            que[g] = []
            qeue = que. get(g)
            appendable = [g]
            qeue. append(appendable)
            text = "Activated Reply Raid"
            await e. reply(text, parse_mode=None, link_preview=None )
        elif e. reply_to_msg_id: 
            a = await e. get_reply_message()
            b = await e. client. get_entity(a.  sender_id)
            g = b. id
            que[g] = []
            qeue = que. get(g)
            appendable = [g]
            qeue. append(appendable)
            text = "Activated Reply Raid"
            await e. reply(text, parse_mode=None, link_preview=None )
        else:
            await e. reply(usage, parse_mode=None, link_preview=None )

            
@idk. on(events.  NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ydk. on(events.  NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@wdk. on(events.  NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@hdk. on(events.  NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@sdk. on(events.  NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@adk. on(events.  NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bdk. on(events.  NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@cdk. on(events.  NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@edk. on(events.  NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ddk. on(events.  NewMessage(incoming=True, pattern=r"\.dreplyraid"))
async def _(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.dreplyraid <Username of User>\n\n.dreplyraid <reply to a User>"
    if e. sender_id in PRO_USERS:
        if e. text[0]. isalpha() and e. text[0] in ("/", "#", "@", "!"):
            return await e. reply(usage, parse_mode=None, link_preview=None )
        atgk = ("".  join(e.  text. split(maxsplit=1)[1:])). split(" ", 1)
        speedo = await e. get_reply_message()
        if len(e.  text) > 12:
            message = str(atgk[0])
            a = await e. client. get_entity(message)
            g = a. id
            try:
                queue = que. get(g)
                queue. pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e. reply(text, parse_mode=None, link_preview=None )
        elif e. reply_to_msg_id: 
            a = await e. get_reply_message()
            b = await e. client. get_entity(a.  sender_id)
            g = b. id
            try:
                queue = que. get(g)
                queue. pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e. reply(text, parse_mode=None, link_preview=None )
        else:
            await e. reply(usage, parse_mode=None, link_preview=None )
    
       

@idk. on(events.  NewMessage(incoming=True, pattern=r"\.ping"))
@ydk. on(events.  NewMessage(incoming=True, pattern=r"\.ping"))
@wdk. on(events.  NewMessage(incoming=True, pattern=r"\.ping"))
@hdk. on(events.  NewMessage(incoming=True, pattern=r"\.ping"))
@sdk. on(events.  NewMessage(incoming=True, pattern=r"\.ping"))
@adk. on(events.  NewMessage(incoming=True, pattern=r"\.ping"))
@bdk. on(events.  NewMessage(incoming=True, pattern=r"\.ping"))
@cdk. on(events.  NewMessage(incoming=True, pattern=r"\.ping"))
@edk. on(events.  NewMessage(incoming=True, pattern=r"\.ping"))
@ddk. on(events.  NewMessage(incoming=True, pattern=r"\.ping"))
async def ping(e):
    if e. sender_id in PRO_USERS:
        start = datetime. now()
        text = "Pong!"
        event = await e. reply(text, parse_mode=None, link_preview=None )
        end = datetime. now()
        ms = (end-start). microseconds / 1000
        await event. edit(f"🤖 𝗣𝗼𝗻𝗴!  \n`{ms}` 𝗺𝘀")



        
        

@idk. on(events.  NewMessage(incoming=True, pattern=r"\.restart"))
@ydk. on(events.  NewMessage(incoming=True, pattern=r"\.restart"))
@wdk. on(events.  NewMessage(incoming=True, pattern=r"\.restart"))
@hdk. on(events.  NewMessage(incoming=True, pattern=r"\.restart"))
@sdk. on(events.  NewMessage(incoming=True, pattern=r"\.restart"))
@adk. on(events.  NewMessage(incoming=True, pattern=r"\.restart"))
@bdk. on(events.  NewMessage(incoming=True, pattern=r"\.restart"))
@cdk. on(events.  NewMessage(incoming=True, pattern=r"\.restart"))
@edk. on(events.  NewMessage(incoming=True, pattern=r"\.restart"))
@ddk. on(events.  NewMessage(incoming=True, pattern=r"\.restart"))
async def restart(e):
    if e. sender_id in PRO_USERS:
        text = "𝙍𝙚𝙨𝙩𝙖𝙧𝙩𝙚𝙙\n\nPlease wait till it reboots..."
        await e. reply(text, parse_mode=None, link_preview=None )
        try:
            await idk. disconnect()
        except Exception as e:
            pass
        try:
            await ydk. disconnect()
        except Exception as e:
            pass
        try:
            await wdk. disconnect()
        except Exception as e:
            pass
        try:
            await hdk. disconnect()
        except Exception as e:
            pass
        try:
            await sdk. disconnect()
        except Exception as e:
            pass
        try:
            await adk. disconnect()
        except Exception as e:
            pass
        try:
            await bdk. disconnect()
        except Exception as e:
            pass
        try:
            await cdk. disconnect()
        except Exception as e:
            pass
        try:
            await ddk. disconnect()
        except Exception as e:
            pass
        try:
            await edk. disconnect()
        except Exception as e:
            pass
        os. execl(sys.  executable, sys. executable, *sys. argv)
        quit()

        
        
        
        
        
@idk. on(events.  NewMessage(incoming=True, pattern=r"\.help"))
@ydk. on(events.  NewMessage(incoming=True, pattern=r"\.help"))
@wdk. on(events.  NewMessage(incoming=True, pattern=r"\.help"))
@hdk. on(events.  NewMessage(incoming=True, pattern=r"\.help"))
@sdk. on(events.  NewMessage(incoming=True, pattern=r"\.help"))
@adk. on(events.  NewMessage(incoming=True, pattern=r"\.help"))
@bdk. on(events.  NewMessage(incoming=True, pattern=r"\.help"))
@cdk. on(events.  NewMessage(incoming=True, pattern=r"\.help"))
@edk. on(events.  NewMessage(incoming=True, pattern=r"\.help"))
@ddk. on(events.  NewMessage(incoming=True, pattern=r"\.help"))
async def help(e):
    if e. sender_id in PRO_USERS:
       text = "𝗔𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀\n\n𝙐𝙩𝙞𝙡𝙨 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.ping\n.restart\n\n𝙐𝙨𝙚𝙧𝙗𝙤𝙩 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.bio\n.join\n.pjoin\n.leave\n\n𝙎𝙥𝙖𝙢 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.spam\n.delayspam\n.bigspam\n.raid\n.replyraid\n.dreplyraid\n\n\nFor more help regarding usage of plugins type plugins name"
       await e. reply(text, parse_mode=None, link_preview=None )

        

 # --------------------------------------------------------------------------------------------------------------------------------

from telethon. errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError,
)
from telethon. tl import functions
from telethon. tl. functions. channels import GetFullChannelRequest
from telethon. tl. functions. messages import GetFullChatRequest


async def get_chatinfo(event):
    chat = event. pattern_match. group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event. reply_to_msg_id:
            replied_msg = await event. get_reply_message()
            if replied_msg. fwd_from and replied_msg. fwd_from. channel_id is not None:
                chat = replied_msg. fwd_from. channel_id
        else:
            chat = event. chat_id
    try:
        chat_info = await event. client(GetFullChatRequest(chat))
    except:
        try:
            chat_info = await event. client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event. reply("`Invalid channel/group`")
            return None
        except ChannelPrivateError:
            await event. reply(
                "`This is a private channel/group or I am banned from there`"
            )
            return None
        except ChannelPublicGroupNaError:
            await event. reply("`Channel or supergroup doesn't exist`")
            return None
        except (TypeError, ValueError):
            await event. reply("`Invalid channel/group`")
            return None
    return chat_info


def make_mention(user):
    if user. username:
        return f"@{user.  username}"
    else:
        return inline_mention(user)


def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"[{full_name}](tg://user?id={user.  id})"


def user_full_name(user):
    names = [user.  first_name, user. last_name]
    names = [i for i in list(names) if i]
    full_name = " ". join(names)
    return full_name


@idk. on(events.  NewMessage(incoming=True, pattern=r"\.inviteall"))
@ydk. on(events.  NewMessage(incoming=True, pattern=r"\.inviteall"))
@wdk. on(events.  NewMessage(incoming=True, pattern=r"\.inviteall"))
@hdk. on(events.  NewMessage(incoming=True, pattern=r"\.inviteall"))
@sdk. on(events.  NewMessage(incoming=True, pattern=r"\.inviteall"))
@adk. on(events.  NewMessage(incoming=True, pattern=r"\.inviteall"))
@bdk. on(events.  NewMessage(incoming=True, pattern=r"\.inviteall"))
@cdk. on(events.  NewMessage(incoming=True, pattern=r"\.inviteall"))
@edk. on(events.  NewMessage(incoming=True, pattern=r"\.inviteall"))
@ddk. on(events.  NewMessage(incoming=True, pattern=r"\.inviteall"))
async def get_users(event):
    if event. sender_id in PRO_USERS:
        rkp = await event. reply("`processing...`")
    else:
        rkp = await event. edit("`processing...`")
    rk1 = await get_chatinfo(event)
    chat = await event. get_chat()
    if event. is_private:
        return await rkp. edit("`Sorry, Can add users here`")
    s = 0
    f = 0
    error = "None"

    await rkp. edit("**TerminalStatus**\n\n`Collecting Users.......`")
    async for user in event. client. iter_participants(rk1.  full_chat. id):
        try:
            if error. startswith("Too"):
                return await rkp. edit(
                    f"**Terminal Finished With Error**\n(`May Got Limit Error from telethon Please try agin Later`)\n**Error** : \n`{error}`\n\n• Invited `{s}` people \n• Failed to Invite `{f }` people"
                )
            await event. client(
                functions. channels. InviteToChannelRequest(channel=chat, users=[user.  id])
            )
            s = s + 1
            await rkp. edit(
                f"**Terminal Running...**\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people\n\n**× LastError:** `{error}`"
            )
        except Exception as e:
            error = str(e)
            f = f + 1
    return await rkp. edit(
        f"**Terminal Finished** \n\n• Successfully Invited `{s}` people \n• failed to invite `{f}` people"
    )

################################
from os import remove, execle, path, makedirs, getenv, environ
from shutil import rmtree
import asyncio
import sys
import git
import git
import heroku3
from git import Repo
from git. exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError


requirements_path = path. join(
    path. dirname(path.  dirname(path.  dirname(__file__))), 'requirements.txt')


GIT_REPO_NAME = "SPAMMER"
UPSTREAM_REPO_URL = "https://github.com/InternetAmethyst/SpeedoSpamBot"

async def gen_chlog(repo, diff):
    ch_log = ''
    d_form = "On " + "%d/%m/%y" + " at " + "%H:%M:%S"
    for c in repo. iter_commits(diff):
        ch_log += f"**#{c.  count()}** :  {c.  committed_datetime. strftime(d_form)}  : [{c.  summary}]({UPSTREAM_REPO_URL.  rstrip('/')}/commit/{c}) by **{c.  author}**\n"
    return ch_log


async def updateme_requirements():
    reqs = str(requirements_path)
    try:
        process = await asyncio. create_subprocess_shell(
            ' '. join([sys.  executable, "-m", "pip", "install", "-r", reqs]),
            stdout=asyncio. subprocess. PIPE,
            stderr=asyncio. subprocess. PIPE)
        await process. communicate()
        return process. returncode
    except Exception as e:
        return repr(e)


@idk. on(events.  NewMessage(incoming=True, pattern=r"\.update"))
@ydk. on(events.  NewMessage(incoming=True, pattern=r"\.update"))
@wdk. on(events.  NewMessage(incoming=True, pattern=r"\.update"))
@hdk. on(events.  NewMessage(incoming=True, pattern=r"\.update"))
@sdk. on(events.  NewMessage(incoming=True, pattern=r"\.update"))
@adk. on(events.  NewMessage(incoming=True, pattern=r"\.update"))
@bdk. on(events.  NewMessage(incoming=True, pattern=r"\.update"))
@cdk. on(events.  NewMessage(incoming=True, pattern=r"\.update"))
@edk. on(events.  NewMessage(incoming=True, pattern=r"\.update"))
@ddk. on(events.  NewMessage(incoming=True, pattern=r"\.update"))
async def _(e):
 if e. sender_id in PRO_USERS:
    "For .update command, check if the bot is up to date, update if specified"
    await e. edit("** Checking for new updates 🧐🧐**")
    conf = e. pattern_match. group(1)
    off_repo = UPSTREAM_REPO_URL
    force_updateme = False

    try:
        txt = "`Oops.. Updater cannot continue as "
        txt += "some problems occured`\n\n**LOGTRACE:**\n"
        repo = Repo()
    except NoSuchPathError as error:
        await e. edit(f'{txt}\n`directory  {error}  is not found`')
        repo. __del__()
        return
    except GitCommandError as error:
        await e. edit(f'{txt}\n`Early failure!  {error}`')
        repo. __del__()
        return
    except InvalidGitRepositoryError as error:
        if conf != "now":
            await e. edit(
                f"**Sync-Verification required since the directory  {error}  does not seem to be a git repository. \
 \nSync-Verify now with  {GIT_REPO_NAME}\
            \nTo do This type** `.update now`."
            )
            return
        repo = Repo. init()
        origin = repo. create_remote('upstream', off_repo)
        origin. fetch()
        force_updateme = True
        repo. create_head('master', origin.  refs. master)
        repo. heads. master. set_tracking_branch(origin.  refs. master)
        repo. heads. master. checkout(True)

    ac_br = repo. active_branch. name
    if ac_br != 'master':
        await e. edit(
            f'**[UPDATER]:**` Looks like you are using your own custom branch ({ac_br}). '
            'in that case, Updater is unable to identify '
             'which branch is to be merged. '
            'Please checkout the official branch`')
        repo. __del__()
        return

    try:
        repo. create_remote('upstream', off_repo)
    except BaseException:
        pass

    e_rem = repo. remote('upstream')
    e_rem. fetch(ac_br)

    changelog = await gen_chlog(repo, f'HEAD.. upstream/{ac_br}')

    if not changelog and not force_updateme:
        await e. edit(
            f'\nBot is  **up-to-date**  `with`  **[[{ac_br}]]({UPSTREAM_REPO_URL}/tree/{ac_br})**\n')
        repo. __del__()
        return

    if conf != "now" and not force_updateme:
        changelog_str = f'**New UPDATE available for [[{ac_br}]]({UPSTREAM_REPO_URL}/tree/{ac_br}):**\n\n' + '**CHANGELOG**\n\n ' + f'{changelog}'
        if len(changelog_str) > 4096:
            await e. edit("`Changelog is too big, view the file to see it.`")
            file = open("output.txt", "w+")
            file. write(changelog_str)
            file. close()
            await e. client. send_file(
                e. chat_id,
                "output.txt",
                reply_to=e. id,
            )
            remove("output.txt")
        else:
            await e. edit(changelog_str)
        await e. respond(f'Do `.update now` to update')
        return

    if force_updateme:
        await e. edit(
            '`Force-Updating to latest stable code, please wait sur😅😅...`')
    else:
        await e. edit('`Updating your` **ßoott** `please wait for 5 mins then type .alive/.ping/.help/.test to see if I am On...`')
    # We're in a Heroku Dyno, handle it's memez.
    if config. HEROKU_API_KEY is not None:
        import heroku3
        heroku = heroku3. from_key(config.  HEROKU_API_KEY)
        heroku_app = None
        heroku_applications = heroku. apps()
        if not config. HEROKU_APP_NAME:
            await e. edit('`Please set up the HEROKU_APP_NAME configiable to be able to update SPAMMER.`')
            repo. __del__()
            return
        for app in heroku_applications:
            if app. name == config. HEROKU_APP_NAME:
                heroku_app = app
                break
        if heroku_app is None:
            await e. edit(
                f'{txt}\n`Invalid Heroku credentials for updating.`'
            )
            repo. __del__()
            return
        await e. edit('`Updating Started 😎😎✨\nRestarting, please wait 5min then type .alive to check if I alive!!! 🙂`'
                       )
        e_rem. fetch(ac_br)
        repo. git. reset("--hard", "FETCH_HEAD")
        heroku_git_url = heroku_app. git_url. replace(
            "https://", "https://api:" + config. HEROKU_API_KEY + "@")
        if "heroku" in repo. remotes:
            remote = repo. remote("heroku")
            remote. set_url(heroku_git_url)
        else:
            remote = repo. create_remote("heroku", heroku_git_url)
        try:
            remote. push(refspec="HEAD:refs/heads/master", force=True)
        except GitCommandError as error:
            await e. edit(f'{txt}\n`Here is the error log:\n{error}`')
            repo. __del__()
            return
        await e. edit('`Sync Verified Successfully 🙂🙂\n'
                       'Restarting, please wait a min ,then type .alive to check if I alive 😂!! `')
    else:
        # Classic Updater, pretty straightforward.
        try:
            e_rem. pull(ac_br)
        except GitCommandError:
            repo. git. reset("--hard", "FETCH_HEAD")
        await updateme_requirements()
        await e. edit('`Successfully Updated!  \n'
                       'Bot is restarting... Wait for a minute😎😎!`')
        # Spin a new instance of bot
        args = [sys.  executable, "-m", "atgk"]
        execle(sys.  executable, *args, environ)
        return


        
text = """
Aman Is Pro
"""
print(text)
print("")
print("Started! SpeedoXAndencento SPAMMER Started Sucessfully.")
if len(sys.  argv) not in (1, 3, 4):
    try:
        idk. disconnect()
    except Exception as e:
        pass
    try:
        ydk. disconnect()
    except Exception as e:
        pass
    try:
        wdk. disconnect()
    except Exception as e:
        pass
    try:
        hdk. disconnect()
    except Exception as e:
        pass
    try:
        sdk. disconnect()
    except Exception as e:
        pass
    try:
        adk. disconnect()
    except Exception as e:
        pass
    try:
        bdk. disconnect()
    except Exception as e:
        pass
    try:
        cdk. disconnect()
    except Exception as e:
        pass
    try:
        edk. disconnect()
    except Exception as e:
        pass
    try:
        ddk. disconnect()
    except Exception as e:
        pass
else:
    try:
        idk. run_until_disconnected()
    except Exception as e:
        pass
    try:
        ydk. run_until_disconnected()
    except Exception as e:
        pass
    try:
        wdk. run_until_disconnected()
    except Exception as e:
        pass
    try:
        hdk. run_until_disconnected()
    except Exception as e:
        pass
    try:
        sdk. run_until_disconnected()
    except Exception as e:
        pass
    try:
        adk. run_until_disconnected()
    except Exception as e:
        pass
    try:
        bdk. run_until_disconnected()
    except Exception as e:
        pass
    try:
        cdk. run_until_disconnected()
    except Exception as e:
        pass
    try:
        edk. run_until_disconnected()
    except Exception as e:
        pass
    try:
        ddk. run_until_disconnected()
    except Exception as e:
        pass
