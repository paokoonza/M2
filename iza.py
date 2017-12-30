# -*- coding: utf-8 -*-
#My Script by danrfq
#Support by My Beloved Team Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞
#i'm Owner Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,requests,urllib
from bs4 import BeautifulSoup
from gtts import gTTS
import requests
import shutil
import time
import json
import html5lib
import wikipedia
import goslate

cl = LINETCR.LINE()
cl.login(qr=True)
cl.loginResult()

print "Login Success Boss"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅHelp CommandᎢ̡̦͎͇͈̘̻̎̉̅́̒͗ͅ
⌨️ ʜɢ - ʜᴇʟᴘ ɢʀᴏᴜᴘ
⌨️ ʜᴀ - ʜᴇʟᴘ ᴀᴅᴍɪɴ
⌨️ ʜᴋ - ʜᴇʟᴘ ᴋɪᴄᴋᴇʀ
⌨️ ʜᴜ - ʜᴇʟᴘ ᴜᴛɪʟɪᴛʏ
⌨️ ʜs - ʜᴇʟᴘ sᴇᴛᴛɪɴɢ
⌨️ ʜᴘ - ʜᴇʟᴘ ᴘʀᴏᴛᴇᴄᴛ
⌨️ sᴇᴛ - ɢʀᴏᴜᴘ sᴇᴛᴛɪɴɢs
"""

hgMessage ="""[👨‍👩‍👧‍👦] - ʜᴇʟᴘ ғᴏʀ ɢʀᴏᴜᴘ - [👨‍👩‍👧‍👦]
⌨  ʜᴀɪ         - Tᴀɢ Sᴇᴍᴜᴀ Mᴇᴍʙᴇʀ Gʀᴜᴘ
⌨  ᴄɪᴅᴜᴋ     - Mᴇᴍʙᴜᴀᴛ Sᴇᴛ Sɪᴅᴇʀ
⌨  ɪɴᴛɪᴘ      - Mᴇɴɢɪɴᴛɪᴘ Sɪᴅᴇʀ
⌨  Gɪɴғᴏ     - Iɴғᴏ Gʀᴜᴘ
⌨️  Sᴛᴇᴀʟ ʜᴏᴍᴇ @     - Mᴇɴᴄᴜʀɪ Cᴏᴠᴇʀ Oʀᴀɴɢ
⌨️  .ᴍs       - Mᴇɴᴄᴀʀɪ Mᴜsɪᴄ ʏᴀɴɢ Dɪɪɴɢɪɴᴋᴀɴ
⌨️  .ʏᴛ        - Mᴇɴᴄᴀʀɪ Yᴏᴜᴛᴜʙᴇ ʏᴀɴɢ Dɪɪɴɢɪɴᴋᴀɴ
⌨️  .ɪɢ        - Mᴇɴᴄᴀʀɪ Iɴsᴛᴀɢʀᴀᴍ ʏᴀɴɢ Dɪɪɴɢɪɴᴋᴀɴ
⌨️  .ʀᴊ        - Mᴇɴɢᴄᴀɴᴄᴇʟ Sᴇᴍᴜᴀ Uɴᴅᴀɴɢᴀɴ Gʀᴜᴘ Aɴᴅᴀ
⌨️  .ᴄʙ       - Cᴇᴋ Kᴇᴀᴋᴛɪғᴀɴ Bᴏᴛ
⌨️  .ʀᴛ       - Cᴇᴋ Wᴀᴋᴛᴜ Bᴏᴛ Bᴇʀᴊᴀʟᴀɴ
⌨  .ʀᴄ       - Mᴇɴɢʜᴀᴘᴜs Rɪᴡᴀʏᴀᴛ Oʙʀᴏʟᴀɴ Gʀᴜᴘ
⌨️  .ʟɢ       - Kᴇʟᴜᴀʀ Dᴀʀɪ Gʀᴜᴘ
⌨️  ᴍɪᴅ     - Mᴇɴɢɪʀɪᴍ Mɪᴅ Aɴᴅᴀ
⌨️  ᴍᴇ       - Mᴇɴɢɪʀɪᴍ Kᴏɴᴛᴀᴋ Aɴᴅᴀ"""

haMessage = """[👤] - ʜᴇʟᴘ ғᴏʀ ᴀᴅᴍɪɴ - [👤]
⌨  Gʟɪsᴛ        - Dᴀғᴛᴀʀ Gʀᴜᴘ
⌨️  Gʟɪᴅ          - Dᴀғᴛᴀʀ Gʀᴜᴘ Dᴇɴɢᴀɴ Gʀᴜᴘ
⌨️  Fʟɪsᴛ         - Dᴀғᴛᴀʀ Tᴇᴍᴀɴ 
⌨  Cᴀɴᴄᴇʟ     - Cᴀɴᴄᴇʟ Pᴇɴᴅɪɴɢ Gʀᴜᴘ Rᴏᴍʙᴏɴɢᴀɴ
⌨  B!!!               - Cᴀɴᴄᴇʟ Pᴇɴᴅɪɴɢ Gʀᴜᴘ Sᴀᴛᴜ²
⌨  Mɪᴅ @      - Mᴇɴᴅᴀᴘᴀᴛᴋᴀɴ Mɪᴅ Oʀᴀɴɢ
⌨  Iɴᴠɪᴛᴇ       - Iɴᴠɪᴛᴇ Vɪᴀ Sᴇɴᴅ Cᴏɴᴛᴀᴄᴛ
⌨  Iɴᴠɪᴛᴇ:      - Vɪᴀ MID
⌨  ᴜɴʙᴀɴ @  - Vɪᴀ Tᴀɢ
⌨  ᴜɴʙᴀɴ:      - Vɪᴀ Mɪᴅ
⌨  ᴜɴʙᴀɴ       - Vɪᴀ Sᴇɴᴅ Cᴏɴᴛᴀᴄᴛ
⌨  ʙᴀɴ @       - Vɪᴀ Tᴀɢ
⌨  ʙᴀɴ:           - Vɪᴀ Mɪᴅ
⌨  ʙᴀɴ            - Vɪᴀ Sᴇɴᴅ Cᴏɴᴛᴀᴄᴛ
⌨  Cʟᴇᴀʀ ʙᴀɴ   - Hᴀᴘᴜs Sᴇᴍᴜᴀ Bᴀɴʟɪsᴛ
⌨  ʙǫʀ        - Bᴜᴋᴀ QR Gʀᴜᴘ
⌨  ᴛǫʀ      - Tᴜᴛᴜᴘ QR Gʀᴜᴘ
⌨  Gᴜʀʟ            - Bᴜᴋᴀ QR ᴅᴀɴ Dᴀᴘᴀᴛᴋᴀɴ Lɪɴᴋ QR Gʀᴜᴘ
⌨  Uʀʟ               - Mᴇɴᴅᴀᴘᴀᴛᴋᴀɴ Lɪɴᴋ QR
⌨  ɢɴ                 - Mᴇɴɢɢᴀɴᴛɪ Nᴀᴍᴀ Gʀᴜᴘ
⌨  Bᴀɴʟɪsᴛ        - Cᴇᴋ Bᴀɴʟɪsᴛ
⌨️  .ʙᴍ                - Cᴇᴋ Bᴀɴʟɪsᴛ Mɪᴅ
⌨  Dᴇᴛᴀɪʟs ɢʀᴜᴘ      - Vɪᴀ Gɪᴅ
⌨  Iɴᴠɪᴛᴇᴍᴇ:              - Vɪᴀ Gɪᴅ
⌨  Iɴғᴏ ɢʀᴜᴘ
⌨  Cʟᴇᴀʀ ɢʀᴜᴘ"""

hkMessage ="""[💀] - ʜᴇʟᴘ ғᴏʀ ᴋɪᴄᴋᴇʀ - [💀]
⌨  Nᴜᴋᴇ
⌨  .ᴄɢ
⌨  ᴛᴀᴍᴘᴏʟ sᴇᴍᴜᴀ
⌨  ᴛᴀᴍᴘᴏʟ @       - Vɪᴀ Tᴀɢ
⌨  ᴛᴀᴍᴘᴏʟ:           - Vɪᴀ MID
⌨️  .ᴛᴀᴍᴘᴏʟ            - Mᴇɴᴀᴍᴘᴏʟ Bᴀɴʟɪsᴛ"""

huMessage = """[🛠️] - ʜᴇʟᴘ ғᴏʀ ᴜᴛɪʟɪᴛʏ - [🛠️]
⌨️  .ᴄᴄ         - Cᴏɴᴛᴀᴄᴛ ʏᴀɴɢ Mᴇᴍʙᴜᴀᴛ Cʀᴀsʜ
⌨  Bᴄᴄ        - Bᴄ Kᴇ Sᴇᴍᴜᴀ Kᴏɴᴛᴀᴋ
⌨  Bᴄɢ        - Bᴄ Kᴇ Sᴇᴍᴜᴀ Gʀᴜᴘ
⌨  Sᴘᴀᴍ ᴏɴ/ᴏғғ 「ᴊᴜᴍʟᴀʜ」「 ᴛᴇxᴛ」
⌨  Uɴɪ
⌨  Speed/Sp         - Cᴇᴋ Sᴘᴇᴇᴅ
⌨️  Mʏɴᴀᴍᴇ       - Mᴇɴɢᴜʙᴀʜ Nᴀᴍᴀ Aɴᴅᴀ
⌨️  Mʏʙɪᴏ          - Mᴇɴɢᴜʙᴀʜ Bɪᴏ Aɴᴅᴀ 
⌨  Mʏᴄᴏᴘʏ @    - Cᴏᴘʏ Pʀᴏғɪʟᴇ ᴏʀᴀɴɢ
⌨  Mʏʙᴀᴄᴋᴜᴘ    - Bᴀᴄᴋᴜᴘ Pʀᴏғɪʟᴇ
⌨️  ŤĽ:           - Mᴇᴍᴘᴏsᴛɪɴɢ Sᴇsᴜᴀᴛᴜ ᴅɪ TL
⌨️  /say - Mᴇɴɢᴜʙᴀʜ Tᴇxᴛ Mᴇɴᴊᴀᴅɪ VN
⌨️  Wᴏʏ @  -  Mᴇɴɢsᴘᴀᴍ Pᴇsᴀɴ Vɪᴀ Tᴀɢ
⌨️  ᴄɪᴜᴍ (ᴍɪᴅ) (ᴊᴜᴍʟᴀʜ sᴘᴀᴍ - 999)
⌨️  sᴘᴀᴍ ᴏɴ/ᴏғғ (ᴊᴜᴍʟᴀʜ sᴘᴀᴍ) (ᴛᴇxᴛ)
⌨️  ᴋᴇᴅᴀᴘᴋᴇᴅɪᴘ - Mᴇᴍʙᴜᴀᴛ Tᴇxᴛ Mᴇɴᴊᴀᴅɪ Kᴇᴅᴀᴘᴋᴇᴅɪᴘ"""

hsMessage = """[⚙️] - ʜᴇʟᴘ ғᴏʀ sᴇᴛᴛɪɴɢ - [⚙️]
    
⌨  [Lɪᴋᴇ ᴏɴ/ᴏғғ]     
⌨  [Aᴅᴅ ᴏɴ/ᴏғғ] 	 
⌨  [Aᴜᴛᴏ ᴊᴏɪɴ ᴏɴ/ᴏғғ] 	   
⌨  [Cᴏɴᴛᴀᴄᴛ ᴏɴ/ᴏғғ] 	
⌨  [Lᴇᴀᴠᴇ ᴏɴ/ᴏғғ]  
⌨  [Sʜᴀʀᴇ ᴏɴ/ᴏғғ]           
⌨  [ᴊᴀᴍ ᴏɴ/ᴏғғ]			   
⌨  [ᴊᴀᴍ sᴀʏ:]			   
⌨  [Cᴏᴍ ᴏɴ/ᴏғғ]	
⌨  [Mᴇssᴀɢᴇ sᴇᴛ:]	
⌨  [Cᴏᴍᴍᴇɴᴛ sᴇᴛ:]	
⌨  [Pᴇsᴀɴ ᴀᴅᴅ:]	
⌨️  [Pᴇsᴀɴ ᴀᴅᴅ ᴄᴇᴋ]"""

hpMessage = """[🛡️] - ʜᴇʟᴘ ғᴏʀ ᴘʀᴏᴛᴇᴄᴛ - [🛡️]
⌨  [Aʟʟᴘʀᴏᴛᴇᴄᴛ ᴏɴ/ᴏғғ]      
⌨  [ᴘʀᴏᴛᴇᴄᴛ ᴏɴ/ᴏғғ]			   
⌨  [ǫʀᴘʀᴏᴛᴇᴄᴛ ᴏɴ/ᴏғғ]			   
⌨  [ɪɴᴠɪᴛᴇᴘʀᴏᴛᴇᴄᴛ ᴏɴ/ᴏғғ]			   
⌨  [cᴀɴᴄᴇʟᴘʀᴏᴛᴇᴄᴛ ᴏɴ/ᴏғғ]"""

KAC=[cl]
mid = cl.getProfile().mid
Bots = [mid,"u997c01ab9d48abd2b807e032d9ac21d3"]
admsa = "u997c01ab9d48abd2b807e032d9ac21d3"
admin = "u997c01ab9d48abd2b807e032d9ac21d3"
crash = "u78e5efff85bf97393cc2c4b8ecf93d25"

wait = {
    'contact':True,
    'autoJoin':False,
    'autoCancel':{"on":False,"members":20},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':" Thank For Add Me\n\nSelf Creator ʙʏ Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅAmiiᎢ̡̦͎͇͈̘̻̎̉̅́̒͗ͅ\n\nline://ti/p/~amiiqila_",
    "lang":"JP",
    "comment":"Aᴜᴛᴏ Lɪᴋᴇ ʙʏ Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅAmiiᎢ̡̦͎͇͈̘̻̎̉̅́̒͗ͅ\n\nline://ti/p/~amiiqila_",
    "commentOn":True,
    "likeOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cNames":"",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protect":False,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
    "tag":True,
}

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    "ricoinvite":{},
    'ROM':{},
    }
    
setTime = {}
setTime = wait2['setTime']
blacklistFile='blacklist.txt'
pendinglistFile='pendinglist.txt'

contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

mulai = time.time()

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False
 
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik 😉' % (hours, mins, secs)
    
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "Mid Kamu":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = cl.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1003)
            if op.type == 26:
                msg = op.message
            
            if 'MENTION' in msg.contentMetadata.keys() != None:
              if wait ["tag"] == True:
                    contact = cl.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["bacot.",cName + " ngapain ngetag?",cName + " sokap bat lu ngetag gua.","apaan?"]
                    ret_ = " " + random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  break                                                       
                
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
            	if wait["ricoinvite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 cl.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 cl.sendText(msg.to,"Sorry, " + _name + " On Banlist")
                                 cl.sendText(msg.to,"Call my daddy to use command !, \n➡unban: " + invite)
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     cl.findAndAddContactsByMid(target)
                                     cl.inviteIntoGroup(msg.to,[target])
                                     random.choice(KAC).sendText(msg.to,"Sukses menginvite gembel ini😆: \n➡ " + _name)
                                     wait2["ricoinvite"] = False
                                     break                              
                                 except:             
                                          cl.sendText(msg.to,"Your Account Limit Invitation.")
                                          wait2["ricoinvite"] = False
                                          break
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam👈")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"Itu tidak berkomentar👈")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"Tidak ada dalam daftar hitam👈")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Done👈")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done👈")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"Done👈")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "Post URL Yang Diatas\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
                
            elif msg.text is None:
                return
            elif msg.text.lower()  == 'help':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpMessage)
            elif msg.text.lower()  == 'hg':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,hgMessage)
                else:
                    cl.sendText(msg.to,hgMessage)
            elif msg.text.lower()  == 'ha':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,haMessage)
                else:
                    cl.sendText(msg.to,haMessage)
            elif msg.text.lower()  == 'hk':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,hkMessage)
                else:
                    cl.sendText(msg.to,hkMessage)
            elif msg.text.lower()  == 'hu':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,huMessage)
                else:
                    cl.sendText(msg.to,huMessage)
            elif msg.text.lower()  == 'hs':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,hsMessage)
                else:
                    cl.sendText(msg.to,hsMessage)
            elif msg.text.lower()  == 'hp':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,hpMessage)
                else:
                    cl.sendText(msg.to,hpMessage)
            elif "tgbot" == msg.text:
            	cl.sendText(msg.to,"Dibawah ini adalah Daftar Kontak BOT TGB")
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki6mid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki7mid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                
            elif "tgb1" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                cl.sendMessage(msg)
            elif "tgb2" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                cl.sendMessage(msg)
            elif "tgb3" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                cl.sendMessage(msg)
            elif "tgb4" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                cl.sendMessage(msg)
            elif "tgb5" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                cl.sendMessage(msg)
           
            elif msg.text in ["Bot1 Gift","Bot1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '2'}
                msg.text = None
                cl.sendMessage(msg)
            elif "@"+cl.getProfile().displayName in msg.text:
               if wait["tag"] == True:
                tanya = msg.text.replace("@"+cl.getProfile().displayName,"")
                jawab = ("Jgn Tag Si "+cl.getProfile().displayName+"!!","Berisik jgn tag si "+cl.getProfile().displayName+" dia masih tidur")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text in ["Bot2 Gift","Bot2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text in ["Bot3 Gift","Bot3 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '4'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["Bot4 Gift","Bot4 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)

#--------------------------------------------------------
            elif msg.text in ["cancel","Cancel"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                        cl.sendText(msg.to,"Sukses Mengancel Undangan")
                    else:
                        cl.sendText(msg.to,"No one is inviting")
                else:
                    cl.sendText(msg.to,"Can not be used outside the group")
                    
            elif msg.text in ["B!!!"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"")
                    cl.sendText(msg.to,"")
                    cl.sendText(msg.to,"")
#--------------------------------------------------------

            elif "Contact" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.to}
                cl.sendMessage(msg)
            elif "tgb1 mid" == msg.text:
                cl.sendText(msg.to,kimid)
            elif "tgb2 mid" == msg.text:
                cl.sendText(msg.to,ki2mid)
            elif "tgb3 mid" == msg.text:
                cl.sendText(msg.to,ki3mid)
            elif "tgb4 mid" == msg.text:
                cl.sendText(msg.to,ki4mid)
            elif "tgb5 mid" == msg.text:
                cl.sendText(msg.to,ki5mid)
                
            elif msg.text.lower() == '.rt':
                eltime = time.time() - mulai
                dan = "Bot sudah berjalan selama "+waktu(eltime)
                cl.sendText(msg.to,dan)
     
            elif "All mid" == msg.text:
                cl.sendText(msg.to,kimid)
                cl.sendText(msg.to,ki2mid)
                cl.sendText(msg.to,ki3mid)
                cl.sendText(msg.to,ki4mid)
                cl.sendText(msg.to,ki5mid)

            elif "TL: " in msg.text:
                tl_text = msg.text.replace("TL: ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])

            elif msg.text in ["Tag on"]:
                if wait["tag"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"turned to on")
                else:
                    wait["tag"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"turned to on")
                    else:
                        cl.sendText(msg.to,"already on")
                        
            elif msg.text in ["Tag off"]:
                if wait["tag"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"turned to off")
                else:
                    wait["tag"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"turned to off")
                    else:
                        cl.sendText(msg.to,"already off")
                        
            elif "Allname: " in msg.text:
                string = msg.text.replace("Allname: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
    
            elif "Allbio: " in msg.text:
                string = msg.text.replace("Allbio: ","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
              
#---------------------------------------------------------
            elif "1pro: " in msg.text:
                string = msg.text.replace("1pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "2pro: " in msg.text:
                string = msg.text.replace("2pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "3pro: " in msg.text:
                string = msg.text.replace("3pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "4pro: " in msg.text:
                string = msg.text.replace("4pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "5pro: " in msg.text:
                string = msg.text.replace("5pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")  
#--------------------------------------------------------
            elif "Mid: " in msg.text:
                mmid = msg.text.replace("Mid: ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)

            elif "Cium! " in msg.text:
                korban = msg.text.replace("Cium! ","")
                korban2 = korban.split()
                midd = korban2[0]
                jumlah = int(korban2[1])
                if jumlah <= 999:
                    for var in range(0,jumlah):
                        cl.sendText(midd,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜Ᏼøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                else:
                    cl.sendText(msg.to, "Kebanyakan gblk! ")
                print "T E R S P A M"
            elif "Add " in msg.text:
                target = msg.text.replace("Add ","")
                cl.findAndAddContactsByMid(target)
                cl.sendText(msg.to, "Sukses Add " +cl.getContact(target).displayName+ " ")
                print "Add user"
            elif msg.text.lower() == 'contact on':
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah On")
                    else:
                        cl.sendText(msg.to,"It is already open")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already open 👈")
                    else:
                        cl.sendText(msg.to,"It is already open 􀜁􀇔􏿿")
            elif msg.text.lower() == 'contact off':
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"sudah off ô€œô€„‰👈")
                    else:
                        cl.sendText(msg.to,"It is already off ô€œ��ô€„‰👈")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"off ô€œô€„‰already")
                    else:
                        cl.sendText(msg.to,"already Close ô€œô€„‰👈")
            elif msg.text.lower() == 'protect on':
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
            elif msg.text.lower() == 'qrprotect on':
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔��👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
            elif msg.text.lower() == 'inviteprotect on':
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ô€¨����👈")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
            elif msg.text.lower() == 'cancelprotect on':
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
            elif msg.text.lower() == 'auto join on':
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah off 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
            elif msg.text in ["Allprotect on","Panick:on"]:
              if msg.from_ in admin:
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect invite on 􀜁􀇔􏿿")
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect cancel on 􀜁􀇔􏿿")
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect on 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Already on")
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR on 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Already on")
            elif msg.text in ["Allprotect off","Panick:off"]:
              if msg.from_ in admin:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah off 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Already off")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect invite off 􀜁􀇔􏿿")
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah off 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Already off")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect cancel off 􀜁􀇔􏿿")
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah off 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Already off")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect off 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Already off")
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah off 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Already off")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR off 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Already off")
            elif msg.text.lower() == 'auto join off':
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Join Already Off")
                    else:
                        cl.sendText(msg.to,"Auto Join set off")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
            elif msg.text in ["Protect off"]:
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"hall ini sudah off ô€œ👈")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
            elif msg.text in ["Qrprotect off","qrprotect off"]:
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"hall ini sudah off ô€œ👈")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
            elif msg.text in ["Inviteprotect off","inviteprotect off"]:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"hall ini sudah off ô€œ👈")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
            elif msg.text in ["Cancelprotect off","cancelprotect off"]:
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"hall ini sudah off ô€œ👈")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
            elif "Group cancel: " in msg.text:
                try:
                    strnum = msg.text.replace("Group cancel: ","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Itu off undangan ditolak👈\nSilakan kirim dengan menentukan jumlah orang ketika Anda menghidupkan👈")
                        else:
                            cl.sendText(msg.to,"Off undangan ditolak👈Sebutkan jumlah terbuka ketika Anda ingin mengirim")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "Kelompok berikut yang diundang akan ditolak secara otomatis👈")
                        else:
                            cl.sendText(msg.to,strnum + "The team declined to create the following automatic invitation")
                except:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Nilai tidak benar👈")
                    else:
                        cl.sendText(msg.to,"Weird value🛡")
            elif msg.text in ["Leave on","Auto leave: on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"on👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Sudah terbuka 􀜁􀇔􏿿")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Is already open👈􀜁􀇔􏿿")
            elif msg.text in ["Leave off","Auto leave: off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"on👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Sudah off👈􀜁􀇔􏿿")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Is already close👈􀜁􀇔􏿿")
            elif msg.text in ["Share on","share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka👈")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"on👈")
                    else:
                        cl.sendText(msg.to,"on👈")
            elif msg.text in ["Share off","share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already turned off 􀜁􀇔􏿿👈")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off👈")
                    else:
                        cl.sendText(msg.to,"Off👈")
            elif msg.text.lower() == 'set':
                md = ""
                if wait["contact"] == True: md+="Dᴀғᴛᴀʀ Sᴇᴛᴛɪɴɢ\n\n▩ Cᴏɴᴛᴀᴄᴛ → ✓\n"
                else: md+="Dᴀғᴛᴀʀ Sᴇᴛᴛɪɴɢ\n\n▩ Cᴏɴᴛᴀᴄᴛ → ✗\n"
                if wait["autoJoin"] == True: md+="▩ Aᴜᴛᴏ ᴊᴏɪɴ → ✓\n"
                else: md+="▩ Aᴜᴛᴏ ᴊᴏɪɴ → ✗\n"
                if wait["autoCancel"]["on"] == True:md+="▩ ᴀᴜᴛᴏ ᴄᴀɴᴄᴇʟ: " + str(wait["autoCancel"]["members"]) + " → ✓\n"
                else: md+="▩ ᴀᴜᴛᴏ ᴄᴀɴᴄᴇʟ → ✗\n"
                if wait["leaveRoom"] == True: md+="▩ Aᴜᴛᴏ ʟᴇᴀᴠᴇ → ✓\n"
                else: md+="▩ Aᴜᴛᴏ ʟᴇᴀᴠᴇ → ✗\n"
                if wait["timeline"] == True: md+="▩ sʜᴀʀᴇ → ✓\n"
                else:md+="▩ sʜᴀʀᴇ → ✗\n"
                if wait["autoAdd"] == True: md+="▩ Aᴜᴛᴏ ᴀᴅᴅ → ✓\n"
                else:md+="▩ Aᴜᴛᴏ ᴀᴅᴅ → ✗\n"
                if wait["commentOn"] == True: md+="▩ Aᴜᴛᴏ ᴄᴏᴍᴍᴇɴᴛ→ ✓\n"
                else:md+="▩ Aᴜᴛᴏ ᴄᴏᴍᴍᴇɴᴛ → ✗\n"
                if wait["protect"] == True: md+="▩ Pʀᴏᴛᴇᴄᴛ → ✓\n"
                else:md+="▩ Pʀᴏᴛᴇᴄᴛ → ✗\n"
                if wait["linkprotect"] == True: md+="▩ ǫʀᴘʀᴏᴛᴇᴄᴛ → ✓\n"
                else:md+="▩ ǫʀᴘʀᴏᴛᴇᴄᴛ → ✗\n"
                if wait["inviteprotect"] == True: md+="▩ Iɴᴠɪᴛᴇᴘʀᴏᴛᴇᴄᴛ → ✓\n"
                else:md+="▩ Iɴᴠɪᴛᴇᴘʀᴏᴛᴇᴄᴛ → ✗\n"
                if wait["cancelprotect"] == True: md+="▩ Cᴀɴᴄᴇʟᴘʀᴏᴛᴇᴄᴛ → ✓\n"
                else:md+="▩ Cᴀɴᴄᴇʟᴘʀᴏᴛᴇᴄᴛ → ✗\n"
                if wait["likeOn"] == True: md+="▩ Aᴜᴛᴏ ʟɪᴋᴇ → ✓\n"
                else:md+="▩ ʟɪᴋᴇ → ✗\n" 
                if wait["tag"] == True: md+="▩ Tᴀɢ → ✓\n\nPᴏᴡᴇʀᴇᴅ ʙʏ:\nᎢ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜Ᏼøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞" 
                else:md+="▩ Tᴀɢ → ✗\n\nPᴏᴡᴇʀᴇᴅ ʙʏ:\nᎢ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜Ᏼøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞" 
                cl.sendText(msg.to,md)
                #cl.sendText(msg.to,"ɪᴅ ʟɪɴᴇ: line://ti/p/~amiiqila_\n\nʙɪʟᴀ ᴀᴅᴀ ᴘᴇʀʟᴜ ᴘᴄ ᴋᴏɴᴛᴀᴋ ᴅɪʙᴀᴡᴀʜ 😁")
                #msg.contentType = 13
                #msg.contentMetadata = {'mid': crash}
                #cl.sendMessage(msg)
            
            elif msg.text in ["Like on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")
            elif msg.text in ["いいね:オフ","Like off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")
                        
            elif msg.text in ["Longname","longname",".ln"]:
            	        cl.sendText(msg.to,"[チェックボックス][チェックボックス][チェックボックス][チェックボックス][チェックボックス][チェックボックス][チェックボックス][チェックボックス][チェックボックス][チェックボックス][チェックボックス][チェックボックス][チェックボックス][チェックボックス][チェックボックス][チェックボックス]")
                        
            elif msg.text in ["Add on","Add auto on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already On")
                    else:
                        cl.sendText(msg.to,"Already On👈")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already On👈")
                    else:
                        cl.sendText(msg.to,"Already On👈")
            elif msg.text in ["Add off","Add auto off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini sudah off👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah dimatikan👈")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already Off👈")
                    else:
                        cl.sendText(msg.to,"Untuk mengaktifkan-off👈")
            elif "Message set: " in msg.text:
                wait["message"] = msg.text.replace("Message set: ","")
                cl.sendText(msg.to,"We changed the message👈")
            elif "Help set: " in msg.text:
                wait["help"] = msg.text.replace("Help set: ","")
                cl.sendText(msg.to,"We changed the Help👈")
            elif "Pesan add: " in msg.text:
                wait["message"] = msg.text.replace("Pesan add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Kami mengubah pesan🛡")
                else:
                    cl.sendText(msg.to,"Change information")
            elif msg.text in ["Pesan add cek","Message Confirmation"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Additional information is automatically set to the following \n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"])
            elif msg.text in ["Change","change"]:
                if wait["lang"] =="JP":
                    wait["lang"] = "TW"
                    cl.sendText(msg.to,"I changed the language to engglis👈")
                else:
                    wait["lang"] = "JP"
                    cl.sendText(msg.to,"I changed the language to indonesia👈")
            elif "Message set: " in msg.text:
                c = msg.text.replace("Message set: ","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Is a string that can not be changed👈")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"This has been changed👈\n\n" + c)
            elif "Comment set: " in msg.text:
                c = msg.text.replace("Comment set: ","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"Ini telah diubah👈\n\n" + c)
            elif msg.text in ["Com on","Com:on","Comment on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Aku berada di👈")
                    else:
                        cl.sendText(msg.to,"To open👈")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It is already turned on")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€👈")
            elif msg.text in ["Flist"]:
				if msg.from_ in admin:
					if wait["teman"] == {}:
						cl.sendText(msg.to,"nothing")
					else:
						cl.sendText(msg.to,"Daftar teman teman ku ada dibawah ini")
						mc = ""
						for mi_d in wait["teman"]:
							mc += "->" +cl.getContact(mi_d).displayName + "\n"
						cl.sendText(msg.to,mc)
            elif msg.text in ["Com off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It is already turned off")
                    else:
                        cl.sendText(msg.to,"It is already turned off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off👈")
                    else:
                        cl.sendText(msg.to,"To turn off")
            elif msg.text in ["Com","Comment"]:
                cl.sendText(msg.to,"Auto Comment saat ini telah ditetapkan sebagai berikut:👈\n\n" + str(wait["comment"]))
            elif msg.text in ["Com Bl"]:
                wait["wblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add to the banlist…”👈")
            elif msg.text in ["Com hapus Bl"]:
                wait["dblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add from the banlist…”👈")
            elif msg.text in ["Com Bl cek"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"Nothing in the blacklistô€œ🛡")
                else:
                    cl.sendText(msg.to,"The following is a blacklistô€œ👈")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "ãƒ»" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text.lower() == 'jam on':
                if wait["clock"] == True:
                    cl.sendText(msg.to,"Sudah On 😊")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"👉Jam on👈")
            elif msg.text.lower() == 'jam off':
                if wait["clock"] == False:
                    cl.sendText(msg.to,"Hal ini sudah off🛡")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"Adalah Off")
            elif "Woy! @" in msg.text:
                _name = msg.text.replace("Woy! @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(msg.to,"Selesai Mengspam Akun Target")
                       
            elif "jam say: " in msg.text:
                n = msg.text.replace("jam say: ","")
                if len(n.decode("utf-8")) > 30:
                    cl.sendText(msg.to,"terlalu lama")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"Ini telah diubah🛡\n\n" + n)
            elif msg.text.lower() == 'update':
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Diperbarui👈")
                else:
                    cl.sendText(msg.to,"Silahkan Aktifkan Nama")

            elif msg.text == "Ciduk":
                if msg.toType == 2:
                    cl.sendText(msg.to, "Mulai Menciduk Sider\nKetik 「intip」ntar gua intip Sidernya 😼\nBuat Yang liat Gausah Ketik intip\nPercuma, ga bakal muncul~\n\nPencidukan Dimulai Pada Tanggal dan Waktu:" + datetime.now().strftime('\n%Y/%m/%d %H:%M:%S'))
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        print wait2
                        
            elif msg.text == "Intip":
                if msg.toType == 2:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "[PENGINTIPAN SIDER]\n---------------\nSider kntl:%s\n\n\n\nSider gblk:\n%s\n\n---------------\nDiintip pada Set Point terakhir pada:\n[%s]\n---------------\n\nJangan Sider Mulu Anjing~ \n\n[🐿️]➦Powered By: Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞\n\n•┅─────" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                        print "ReadPoint Set..."
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        print wait
                        cl.sendText(msg.to, "Pengintipan Pada Tanggal dan Waktu:" + datetime.now().strftime('\n%Y-%m-%d %H:%M:%S'))
                    else:
                        cl.sendText(msg.to, "LO AJA BELOM KETIK CIDUK!")

#-----------------------[Add Staff Section]------------------------
            elif "Add staff @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Add staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the staff list")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "Remove staff @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Remove staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed to the staff list")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif msg.text in ["Stafflist","stafflist"]:
                if staff == []:
                    cl.sendText(msg.to,"The stafflist is empty")
                else:
                    cl.sendText(msg.to,"Staff list: ")
                    mc = ""
                    for mi_d in staff:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"	
                    
#---------------------KEDAPKEDIP SECTION-------------------#

            elif "kedapkedip " in msg.text.lower():
                txt = msg.text.replace("kedapkedip ", "")
                t1 = "\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xa0\x81\xf4\x80\xa0\x81\xf4\x80\xa0\x81"
                t2 = "\xf4\x80\x82\xb3\xf4\x8f\xbf\xbf"
                cl.sendText(msg.to, t1 + txt + t2)							

#----------------------ADMIN COMMAND------------------------------#

            elif ("tampol " in msg.text):
                if msg.from_ in admin:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(msg.to,[target])
                        except:
                            cl.sendText(msg.to,"Error")
                            
            elif ".cg" in msg.text:
                if msg.toType == 2:
                    print "Cleanse is going."
                    _name = msg.text.replace(".cg ","")
                    gs = cl.getGroup(msg.to)
                    cl.sendText(msg.to,"ᴘᴇᴍʙᴇʀsɪʜᴀɴ ᴀᴋᴀɴ ᴅɪʟᴀᴋsᴀɴᴀᴋᴀɴ")
                    cl.sendText(msg.to,"sᴀʏ ɢᴏᴏᴅ ʙʏᴇ ᴛᴏ ᴍᴇ")
                    cl.sendText(msg.to,"ᴘᴇᴍʙᴇʀsɪʜᴀɴ ᴅɪʟᴀᴋsᴀɴᴀᴋᴀɴ")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found.")
                        cl.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                          if not target in Bots:
                            try:
                                klist=[cl]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                                cl.sendText(msg.to,"ɢʀᴏᴜᴘ sᴜᴅᴀʜ ᴅɪʙᴇʀsɪʜᴋᴀɴ")
                            except:
                                cl.sendText(msg,to,"Group cleanse")
                                cl.sendText(msg,to,"Group cleanse")
                    
#-------------TagALL Start---------------#
            elif msg.text in ["Hai"]:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                cb = ""
                cb2 = ""
                strt = int(0)
                akh = int(0)
                for md in nama:
                    akh = akh + int(6)
                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                    strt = strt + int(7)
                    akh = akh + 1
                    cb2 += "@nrik \n"
                cb = (cb[:int(len(cb)-1)])
                msg.contentType = 0
                msg.text = cb2
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                try:
                    cl.sendMessage(msg)
                except Exception as error:
                    print error
#-----------------------------------------------
    #-------------TagALL Finish-------------#           

            elif "Tampol semua" in msg.text:
                  if msg.from_ in admin:
                       nk0 = msg.text.replace("tampol semua","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("all","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for g in gs.members:
                           if _name in g.displayName:
                              targets.append(g.mid)
                       if targets == []:
                           cl.sendText(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:                            
                             if not target in Bots:
                                if not target in admin:
                                  try:
                                      klist=[cl,ki,ki2,ki3,ki4,ki5]
                                      kicker=random.choice(klist)
                                      kicker.kickoutFromGroup(msg.to,[target])
                                      print (msg.to,[g.mid])
                                  except:
                                      cl.sendText(msg.to,"Sukses Bosqu")
                                      cl.sendText(msg.to,"masih mauko sundala")

            elif msg.text in ["Glid"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    h = "===[List Groups]==="
                    total = str(len(gid))
                    for i in gid:
                        if i is not None:
                            try:
                                groups = cl.getGroup(i)
                                if groups.members is not None:
                                    members = str(len(groups.members))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                h += "\n[" + groups.name + "] ->(" + members +")\n -+GroupID : " + i
                            except:
                                break
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,h + "\n|[Total Groups]| : " + str(total))
                    else:
                        cl.sendText(msg.to,"Tidak ada grup saat ini")
                    ginv = cl.getGroupIdsInvited()
                    j = "===[List Groups Invited]==="
                    totals = str(len(ginv))
                    for z in ginv:
                        if z is not None:
                            try:
                                groups = cl.getGroup(z)
                                if groups.members is not None:
                                    members = str(len(groups.mem1bers))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                j += "\n[" + groups.name + "] ->(" + members + ")\n -+GroupID : " + i
                            except:
                                break
                        else:
                            break
                    if ginv is not None:
                        cl.sendText(msg.to,j + "\n|[Total Groups Invited]| : " + str(totals))
                    else:
                        cl.sendText(msg.to,"Tidak ada grup tertunda saat ini")

            elif msg.text in ["Info grup"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    cl.sendText(msg.to,"===[List Details Group]===")
                    total = str(len(gid))
                    for i in gid:
                        if i is not None:
                            try:
                                groups = cl.getGroup(i)
                                if groups.members is not None:
                                    members = str(len(groups.members))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                h = "[" + groups.name + "]\n -+GroupID : " + i + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName
                            except:
                                break
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,h)
                        cl.sendText(msg.to,"|[Total Groups]| : " + str(total))
                    else:
                        cl.sendText(msg.to,"Tidak ada grup saat ini")
                    ginv = cl.getGroupIdsInvited()
                    cl.sendText(msg.to,"===[List Details Groups Invited]===")
                    totals = str(len(ginv))
                    for z in ginv:
                        if z is not None:
                            try:
                                groups = cl.getGroup(z)
                                if groups.members is not None:
                                    members = str(len(groups.members))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                j = "[" + groups.name + "]\n -+GroupID : " + i + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName
                            except:
                                break
                        else:
                            break
                    if ginv is not None:
                        cl.sendText(msg.to,j)
                        cl.sendText(msg.to,"|[Total Groups Invited]| : " + str(totals))
                    else:
                        cl.sendText(msg.to,"Tidak ada grup tertunda saat ini")

            elif "Details grup: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Details grup: ","")
                    if gid in [""," "]:
                        cl.sendText(msg.to,"Grup id tidak valid")
                    else:
                        try:
                            groups = cl.getGroup(gid)
                            if groups.members is not None:
                                members = str(len(groups.members))
                            else:
                                members = "0"
                            if groups.invitee is not None:
                                pendings = str(len(groups.invitee))
                            else:
                                pendings = "0"
                            h = "[" + groups.name + "]\n -+GroupID : " + gid + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName + "\n -+GroupPicture : http://dl.profile.line.naver.jp/" + groups.pictureStatus
                            cl.sendText(msg.to,h)
                        except Exception as error:
                            cl.sendText(msg.to,(error))
            
            elif "Cancel invite: " in msg.text:
                if msg.from_ in admin:
                    gids = msg.text.replace("Cancel invite: ","")
                    gid = cl.getGroup(gids)
                    for i in gid:
                        if i is not None:
                            try:
                                cl.rejectGroupInvitation(i)
                            except:
                                cl.sendText(msg.to,"Error!")
                                break
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,"Berhasil tolak undangan dari grup " + gid.name)
                    else:
                        cl.sendText(msg.to,"Grup tidak ditemukan")
            
            elif msg.text in ["Accept invite"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsInvited()
                    _list = ""
                    for i in gid:
                        if i is not None:
                            gids = cl.getGroup(i)
                            _list += gids.name
                            cl.acceptGroupInvitation(i)
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,"Berhasil terima semua undangan dari grup :\n" + _list)
                    else:
                        cl.sendText(msg.to,"Tidak ada grup yang tertunda saat ini")
            
            elif "Myname " in msg.text:
                string = msg.text.replace("Myname ","")
                if len(string.decode('utf-8')) <= 200000:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Name" + string)

            elif "Mybio " in msg.text:
                string = msg.text.replace("Mybio ","")
                if len(string.decode('utf-8')) <= 500000:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Bio" + string)
            
            elif 'gn ' in msg.text.lower():
                if msg.toType == 2:
                    wildan = cl.getGroup(msg.to)
                    wildan.name = msg.text.replace("gn ","")
                    cl.updateGroup(wildan)
                    cl.sendText(msg.to,"Sukses Mengganti Nama Grup 😀")

            elif "tampol: " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("tampol: ","")
                cl.kickoutFromGroup(msg.to,[midd])
                
            elif "Invite: " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Invite: ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])

            elif "Steal: " in msg.text:
                if msg.from_ in admin:
                    salsa = msg.text.replace("Steal: ","")
                    Manis = cl.getContact(salsa)
                    Imoet = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    try:
                        cover = cl.channel.getCover(Manis)
                    except:
                        cover = ""
                    cl.sendText(msg.to,"Gambar Foto Profilenya")
                    cl.sendImageWithURL(msg.to,Imoet)
                    if cover == "":
                        cl.sendText(msg.to,"User tidak memiliki cover atau sejenisnya")
                    else:
                        cl.sendText(msg.to,"Gambar Covernya")
                        cl.sendImageWithURL(msg.to,cover)

            elif "Mycopy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Mycopy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                    cl.cloneContactProfile(target)
                                    cl.sendText(msg.to, "Sukses Copy Profile")
                                except Exception as e:
                                    print e
                                    
            elif "Copy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Copy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Tidak Ada Target Copy")
                        else:
                            for target in targets:
                                try:
                                    cl.cloneContactProfile(target)
                                    cl.cloneContactProfile(target)
                                    cl.cloneContactProfile(target)
                                    cl.cloneContactProfile(target)
                                    cl.cloneContactProfile(target)
                                    cl.sendText(msg.to, "Sukses Copy Profile")
                                except Exception as e:
                                    print e
                                    
            elif "/say " in msg.text:
                say = msg.text.replace("/say ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                                    
            elif msg.text in ["Mybackup"]:
                try:
                    cl.updateDisplayPicture(mybackup.pictureStatus)
                    cl.updateProfile(mybackup)
                    cl.sendText(msg.to, "Backup Sukses Bosqu")
                except Exception as e:
                    cl.sendText(msg.to, str (e))
                    
            elif msg.text in ["Backup"]:
                try:
                    cl.updateDisplayPicture(backup.pictureStatus)
                    cl.updateProfile(backup)
                    cl.updateDisplayPicture(backup.pictureStatus)
                    cl.updateProfile(backup)
                    cl.updateDisplayPicture(backup.pictureStatus)
                    cl.updateProfile(backup)
                    cl.updateDisplayPicture(backup.pictureStatus)
                    cl.updateProfile(backup)
                    cl.updateDisplayPicture(backup.pictureStatus)
                    cl.updateProfile(backup)                   
                    cl.sendText(msg.to, "Backup Sukses Bosqu")
                except Exception as e:
                    cl.sendText(msg.to, str (e))

            elif "Bcc " in msg.text:
                bctxt = msg.text.replace("Bcc ", "")
                a = cl.getAllContactIds()
                for manusia in a:
                    cl.sendText(manusia, (bctxt))
                    
            elif ".rc" in msg.text.lower():
                if msg.from_ in admin:
                    try:
                        cl.removeAllMessages(op.param2)
                        print "[Command] Remove Chat"
                        cl.sendText(msg.to,"Sukses Menghapus Chat")
                    except Exception as error:
                        print error
                        cl.sendText(msg.to,"Error Menghapus Chat")
                    
            elif msg.text in ["Conban","Contactban","Contact ban"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Tidak Ada Blacklist")
                else:
                    cl.sendText(msg.to,"Daftar Kontak Penjahat")
                    h = ""
                    for i in wait["blacklist"]:
                        h = cl.getContact(i)
                        M = Message()
                        M.to = msg.to
                        M.contentType = 13
                        M.contentMetadata = {'mid': i}
                        cl.sendMessage(M)

            elif "Bot:ct " in msg.text:
              if msg.from_ in admin:
                bctxt = msg.text.replace("Bot:ct ", "")
                b = cl.getAllContactIds()
                for manusia in b:
                    cl.sendText(manusia, (bctxt))
                c = cl.getAllContactIds()
                for manusia in c:
                    cl.sendText(manusia, (bctxt))
                d = cl.getAllContactIds()
                for manusia in d:
                    cl.sendText(manusia, (bctxt))
                e = cl.getAllContactIds()
                for manusia in e:
                    cl.sendText(manusia, (bctxt))
                f = cl.getAllContactIds()
                for manusia in f:
                    cl.sendText(manusia, (bctxt))
            elif "Bcg " in msg.text:
                bctxt = msg.text.replace("Bcg ", "")
                a = cl.getGroupIdsJoined()
                for manusia in a:
                    cl.sendText(manusia, (bctxt))
            
            elif "Bot:grup " in msg.text:
              if msg.from_ in admin:
                bctxt = msg.text.replace("Bot:grup ", "")
                b = cl.getGroupIdsJoined()
                for manusia in b:
                    cl.sendText(manusia, (bctxt))
                c = cl.getGroupIdsJoined()
                for manusia in c:
                    cl.sendText(manusia, (bctxt))
                d = cl.getGroupIdsJoined()
                for manusia in d:
                    cl.sendText(manusia, (bctxt))
                e = cl.getGroupIdsJoined()
                for manusia in e:
                    cl.sendText(manusia, (bctxt))
                f = cl.getGroupIdsJoined()
                for manusia in f:
                    cl.sendText(manusia, (bctxt))  
                    
            elif "Spam " in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (teks+"\n")
                #danrfq TGB Nih Cika~
                if txt[1] == "on":
                    if jmlh <= 100000:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Out of Range!")
                elif txt[1] == "off":
                    if jmlh <= 100000:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Out Of Range!")

            elif msg.text in ["Sp","Speed"]:
                start = time.time()
                cl.sendText(msg.to, "Harap Bersabar...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%s detik." % (elapsed_time))

            elif msg.text.lower() == 'me':
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)

            elif cms(msg.text,["creator","Creator"]):
            	cl.sendText(msg.to,"Tunggu sebentar...")
                msg.contentType = 13
                msg.contentMetadata = {'mid': crash}
                cl.sendText(msg.to,"Kontak DiBawah adalah Pembuat Bot ini")
                cl.sendMessage(msg)
                cl.sendText(msg.to,"Kontak DiAtas adalah Pembuat Bot ini")
                
                
            elif ".cc" in msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': crash}
                cl.sendMessage(msg)
            
            elif "Inviteme: " in msg.text:
              if msg.from_ in admin:
                gid = msg.text.replace("Inviteme: ","")
                if gid == "":
                    cl.sendText(msg.to,"Invalid group id")
                else:
                    try:
                        cl.findAndAddContactsByMid(msg.from_)
                        cl.inviteIntoGroup(gid,[msg.from_])
                    except:
                        cl.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")

            elif msg.text in ["Clear grup"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsJoined()
                gid = cl.getGroupIdsJoined()
                gid = cl.getGroupIdsJoined()
                gid = cl.getGroupIdsJoined()
                gid = cl.getGroupIdsJoined()
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    cl.leaveGroup(i)
                    cl.leaveGroup(i)
                    cl.leaveGroup(i)
                    cl.leaveGroup(i)
                    cl.leaveGroup(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Bot Sudah Keluar Di semua grup")
                else:
                    cl.sendText(msg.to,"He declined all invitations")

            elif msg.text == "Ginfo":
                    group = cl.getGroup(msg.to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Error"
                    md = "[Nama Grup : ]\n" + group.name + "\n\n[Id Grup : ]\n" + group.id + "\n\n[Pembuat Grup :]\n" + gCreator + "\n\n[Gambar Grup : ]\nhttp://dl.profile.line-cdn.net/" + group.pictureStatus
                    if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                    else: md += "\n\nKode Url : Diblokir"
                    if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                    else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                    cl.sendText(msg.to,md)
            
            elif msg.text == "Uni":
	            cl.sendText(msg.to,"JANGAN DI BUKA 😘\n\nHai Perkenalkan.....\nNama saya siapa ya?\n\n1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1\n\nMakasih Sudah Dilihat :)\nJangan Dikick ampun mzz :v")
            
            elif '.ms ' in msg.text.lower():
            	cl.sendText(msg.to,"Tunggu...")
                try:
                    songname = msg.text.lower().replace('music ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Ini Dia Hasilnya\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Tunggu VN Musiknya...")
                        cl.sendAudioWithURL(msg.to, song[4])
		except Exception as njer:
		        cl.sendText(msg.to, str(njer))
            
            #--------------------------------- YOUTUBE START ----------------------------------#
            elif ".yt " in msg.text:
                query = msg.text.replace(".yt ","")
                with requests.session() as s:
                    s.headers['user-agent'] = 'Mozilla/5.0'
                    url = 'http://www.youtube.com/results'
                    params = {'search_query': query}
                    r = s.get(url, params=params)
                    soup = BeautifulSoup(r.content, 'html5lib')
                    hasil = ""
                    for a in soup.select('.yt-lockup-title > a[title]'):
                        if '&list=' not in a['href']:
                            hasil += ''.join((a['title'],'\nhttp://www.youtube.com' + a['href'],'\n\n'))
                    cl.sendText(msg.to,hasil)
                    print '[Command] Youtube Search'
                    #--------------------------------- YOUTUBE FINISH ----------------------------------#
            
            elif msg.text in ["Glist"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[👨‍👩‍👧‍👦] %s\n" % (cl.getGroup(i).name +"→["+str(len(cl.getGroup(i).members))+"]")
                cl.sendText(msg.to,"[List Group]\n\n"+ h +"Total Group =" +"["+str(len(gid))+"]")

            elif msg.text in ["Invite"]:
              if msg.from_ in admin:
                wait["ricoinvite"] = True
                random.choice(KAC).sendText(msg.to,"Mana kontaknya?")
                
            elif ("Check " in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"Mid:" +  key1)

            elif "Mid @" in msg.text:
              if msg.from_ in admin:  
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass

            elif "mid" == msg.text:
                cl.sendText(msg.to,mid)
                
            elif '.ig ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace(".instagram ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Nama: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "========INSTAGRAM INFO USER========\n"
                    details = "\n========INSTAGRAM INFO USER========"
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))

            elif msg.text in ["Bqr"]:
              if msg.from_ in admin:  
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sukses Membuka QR")
                    else:
                        cl.sendText(msg.to,"Sukses Membuka QR")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group ô€œô€„‰👈")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than ô€œô€„‰")
            
            elif msg.text in ["Tqr"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sukses Menutup QR")
                    else:
                        cl.sendText(msg.to,"Sukses Menutup QR")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group  👈")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than ô€œ")

            elif msg.text in ["url","Url"]:
                if msg.toType == 2:
                    g = cl.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        cl.updateGroup(g)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"Link QR Grup : \n line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok")
                    else:
                        cl.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")

            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"Link QR Grup : \n line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")

            elif msg.text in ["S1glist"]:
                gs = cl.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (cl.getGroup(i).name + " | [ " + str(len (cl.getGroup(i).members)) + " ]")
                cl.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S2glist"]:
                gs = cl.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (cl.getGroup(i).name + " | [ " + str(len (cl.getGroup(i).members)) + " ]")
                cl.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S3glist"]:
                gs = cl.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (cl.getGroup(i).name + " | [ " + str(len (cl.getGroup(i).members)) + " ]")
                cl.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S4glist"]:
                gs = cl.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (cl.getGroup(i).name + " | [ " + str(len (cl.getGroup(i).members)) + " ]")
                cl.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S5glist"]:
                gs = cl.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (cl.getGroup(i).name + " | [ " + str(len (cl.getGroup(i).members)) + " ]")
                cl.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")                    
            elif msg.text == "Link bokep":
                    cl.sendText(msg.to,"nekopoi.host")
                    cl.sendText(msg.to,"sexvideobokep.com")
                    cl.sendText(msg.to,"memek.com")
                    cl.sendText(msg.to,"pornktube.com")
                    cl.sendText(msg.to,"faketaxi.com")
                    cl.sendText(msg.to,"videojorok.com")
                    cl.sendText(msg.to,"watchmygf.mobi")
                    cl.sendText(msg.to,"xnxx.com")
                    cl.sendText(msg.to,"pornhd.com")
                    cl.sendText(msg.to,"xvideos.com")
                    cl.sendText(msg.to,"vidz7.com")
                    cl.sendText(msg.to,"m.xhamster.com")
                    cl.sendText(msg.to,"xxmovies.pro")
                    cl.sendText(msg.to,"youporn.com")
                    cl.sendText(msg.to,"pornhub.com")
                    cl.sendText(msg.to,"anyporn.com")
                    cl.sendText(msg.to,"hdsexdino.com")
                    cl.sendText(msg.to,"rubyourdick.com")
                    cl.sendText(msg.to,"anybunny.mobi")
                    cl.sendText(msg.to,"cliphunter.com")
                    cl.sendText(msg.to,"sexloving.net")
                    cl.sendText(msg.to,"free.goshow.tv")
                    cl.sendText(msg.to,"eporner.com")
                    cl.sendText(msg.to,"Pornhd.josex.net")
                    cl.sendText(msg.to,"m.hqporner.com")
                    cl.sendText(msg.to,"m.spankbang.com")
                    cl.sendText(msg.to,"m.4tube.com")
                    cl.sendText(msg.to,"brazzers.com")

            elif msg.text in [".rj"]:
                    gid = cl.getGroupIdsInvited()
                    for i in gid:
                        cl.rejectGroupInvitation(i)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Semua Undangan sudah di Batalkan Boss 😉")
                    else:
                        cl.sendText(msg.to,"Done 😉")
#-----------------------------------------------------------#
            elif "#leave" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:
                    pass
#-----------------------------------------------------------#
            elif msg.text in ["Responsetime"]:
                start = time.time()
                cl.sendText(msg.to, "Waiting...")
                elapsed_time = time.time() - start
                #cl.sendText(msg.to, "%sseconds" % (elapsed_time))
                #elapsed_time = time.time() - start
                #cl.sendText(msg.to, "%sseconds" % (elapsed_time))
                #elapsed_time = time.time() - start
                #cl.sendText(msg.to, "%sseconds" % (elapsed_time))
                #elapsed_time = time.time() - start
                #cl.sendText(msg.to, "%sseconds" % (elapsed_time))
                #elapsed_time = time.time() - start
            
            elif msg.text.lower() == '.responsename':
                profile = cl.getProfile()
                text = profile.displayName
                cl.sendText(msg.to, text)
                #profile = cl.getProfile()
                #text = profile.displayName
                #cl.sendText(msg.to, text)
                #profile = cl.getProfile()
                #text = profile.displayName
                #cl.sendText(msg.to, text)
                #profile = cl.getProfile()
                #text = profile.displayName
                #cl.sendText(msg.to, text)

#------------------------------------------------------------------#	

            elif "Tampol " in msg.text:
             if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      cl.kickoutFromGroup(msg.to,[target])
                      cl.sendText(msg.to,"Sukses Menampol Dia!")
                   except:
                      pass
                      
            elif "Steal home @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Steal home @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"			
 #------------------------------------------------------------------#
            elif ("Ban " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Sukses Banned!")
                   except:
                      pass

            elif ("Unban " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      del wait["blacklist"][target]
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f,sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Sukses UnBanned!")
                   except:
                      pass
                                
            elif "Ban all" in msg.text:
              if msg.from_ in admin:
                  if msg.toType == 2:
                       print "ok"
                       _name = msg.text.replace("Ban all","")
                       gs = cl.getGroup(msg.to)
                       cl.sendText(msg.to,"Semua Telah Di Ban")
                       targets = []
                       for g in gs.members:
                           if _name in g.displayName:
                                targets.append(g.mid)
                       if targets == []:
                            cl.sendText(msg.to,"Maaf")
                       else:
                           for target in targets:
                               if not target in Bots:
                                   try:
                                       wait["blacklist"][target] = True
                                       f=codecs.open('st2__b.json','w','utf-8')
                                       json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                       cl.sendText(msg.to,"Sukses Banned!")
                                   except:
                                       cl.sentText(msg.to,"Berhasil Dihapus")

            elif "Ban: " in msg.text:       
             if msg.from_ in admin:           
                       nk0 = msg.text.replace("ban: ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Target Locked")
                                except:
                                    cl.sendText(msg.to,"Error")

            elif "Unban: " in msg.text:             
              if msg.from_ in admin:     
                       nk0 = msg.text.replace("unban: ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Target Unlocked")
                                except:
                                    cl.sendText(msg.to,"Error")
                                    
            elif msg.text in ["Clear ban"]:
              if msg.from_ in admin:
                wait["blacklist"] = {}
                cl.sendText(msg.to,"Sukses Membersihkan Daftar Penjahat")
 
            elif msg.text in ["Ban"]:
				if msg.from_ in admin:
					wait["wblacklist"] = True
					cl.sendText(msg.to,"send contact")	
				
            elif msg.text in ["Unban"]:
				if msg.from_ in admin:
					wait["dblacklist"] = True
					cl.sendText(msg.to,"send contact")				
                
            elif msg.text in [".cb"]:
              if msg.from_ in admin:
            	cl.sendText(msg.to,"Bot Masih On Kok 😊\nMungkin Commandnya ga Berfungsi\n atau Error 😕")
            
            elif msg.text.lower() == 'banlist':
            	cl.sendText(msg.to,"Tunggu....")
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += "☠️ " +cl.getContact(mm).displayName + "\n"
                    cl.sendText(msg.to,"Daftar Penjahat\n\n" + cocoa)
                
            elif msg.text in [".bm","banlistmid"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = "[⎈] Mid Banlist [⎈]"
                    for mm in matched_list:
                        cocoa += "\n" + mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text.lower() == '.tampol':
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"Tidak ada Daftar Banlist")
                        return
                    for jj in matched_list:
                        try:
                            cl.kickoutFromGroup(msg.to,[jj])
                            cl.kickoutFromGroup(msg.to,[jj])
                            cl.kickoutFromGroup(msg.to,[jj])
                            cl.kickoutFromGroup(msg.to,[jj])
                            cl.kickoutFromGroup(msg.to,[jj])
                            cl.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            elif "Nuke" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Nuke","")
                    gs = cl.getGroup(msg.to)
                    cl.sendText(msg.to,"Masih Mauko Sundala")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Tidak ada Member")
                        cl.sendText(msg.to,"Nothing Bosqu")
                    else:
                        for target in targets:
                          if not target in Bots:
                            try:
                                klist=[cl]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                cl.sendText(msg,to,"Hahaha")
                                cl.sendText(msg,to,"Fakyu Sundala")

#-----------------------------------------------
            elif msg.text.lower() == ["Allkuy"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        random.choice(KAC).updateGroup(G)                     
#-----------------------------------------------
            elif msg.text in ["Joinall"]:
                if msg.from_ in admsa:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)  
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        cl.updateGroup(G)

            elif msg.text.lower() == 'Sp come':
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                        cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                        cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                        cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                        cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        cl.updateGroup(G)
#-----------------------------------------------
            elif "tgb1 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        cl.updateGroup(G)
#-----------------------------------------------
            elif "tgb2 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        cl.updateGroup(G)
#-----------------------------------------------
            elif "tgb3 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        cl.updateGroup(G)
#-----------------------------------------------
            elif "tgb4 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        cl.updateGroup(G)
#-----------------------------------------------
            elif "tgb5 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        cl.updateGroup(G)
#-----------------------------------------------
            elif msg.text in ["@left"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.sendText(msg.to,"Bye Bye "  +  str(ginfo.name)  + " 😘")
                        cl.leaveGroup(msg.to)
                    except:  
											pass
#-----------------------------------------------
            elif "tgb1 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "tgb2 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "tgb3 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "tgb4 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "tgb5 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif msg.text in ["kam","wc","welcome","Wc"]:
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang di Grup " + str(ginfo.name))
                cl.sendText(msg.to,"Yang Buat Grup " + str(ginfo.name) + " Si:\n" + ginfo.creator.displayName )
#----------------------------------------------- 
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in kimid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)                        
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        cl.updateGroup(G)
                        wait["blacklist"][op.param2] = True                        
                elif op.param3 in kimid:
                    if op.param2 in ki2mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                elif op.param3 in ki3mid:
                    if op.param2 in ki2mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)                       
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        
                elif op.param3 in ki2mid:
                    if op.param2 in ki3mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)                        
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                     
                elif op.param3 in ki4mid:
                    if op.param2 in ki5mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)                       
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)

                elif op.param3 in ki5mid:
                    if op.param2 in ki4mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)                        
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                elif op.param3 in ki6mid:
                    if op.param2 in ki5mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)                        
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)  
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
												
            except:
                pass

	if op.type == 17:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
	    if wait["protect"] == True:
		if wait["blacklist"][op.param2] == True:
		   try:
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			G = random.choice(KAC).getGroup(op.param1)
			G.preventJoinByTicket = True
			cl.updateGroup(G)
#			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		   except:
#			pass
			try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    G = random.choice(KAC).getGroup(op.param1)
			    G.preventJoinByTicket = True
			    random.choice(KAC).updateGroup(G)
#			    random.choice(KAK).kickoutFromGroup(op.param1,[op.param2])
			except:
			    pass
		elif op.param2 not in admin + Bots:
		    random.choice(KAC).sendText(op.param1,"Welcome. Don't Play Bots. I can kick you!")
	    else:
		pass
	if op.type == 19:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["protect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 13:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["cancelprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 11:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["linkprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    G = cl.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    cl.updateGroup(G)
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
        if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
                    
#------Open QR Kick start------#
        if op.type == 11:
            if wait["linkprotect"] == True:
                if op.param2 not in Bots:
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventJoinByTicket = True
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param3])
                    random.choice(KAC).updateGroup(G)
        #------Open QR Kick finish-----#
#------------------------------------------------------------------------------------

        if op.type == 55:
            print "[NOTIFIED_READ_MESSAGE]"
            try:
                if op.param1 in wait2['readPoint']:
                    Nama = cl.getContact(op.param2).displayName
                    if Nama in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n🐶 " + Nama
                        wait2['ROM'][op.param1][op.param2] = "🐷 " + Nama
                        wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                else:
                    cl.sendText
            except:
                pass

        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()
#-------------------------------------------------------------------------------------------#
def autolike():
     for zx in range(0,50):
        hasil = cl.activity(limit=10000)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
          try:    
            cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1003)
            cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aᴜᴛᴏ Lɪᴋᴇ ʙʏ line://ti/p/~amiiqila_")
            print "Like Boss"
          except:
            pass
        else:
            print "Udah Di Like Duluan Bang"
     time.sleep(600)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()
#------------------------------------------------------------------------------------------#
while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
