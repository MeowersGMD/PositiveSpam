from distutils.command.upload import upload
import time,requests,random,os,base64,hashlib
from itertools import cycle
from urllib3 import connection
from json import loads
from threading import Thread

def request(self, method, url, body=None, headers=None):
    if headers is None:
        headers = {}
    else:
        headers = headers.copy()
    super(connection.HTTPConnection, self).request(method, url, body=body, headers=headers)
connection.HTTPConnection.request = request

def comment_chk(*,username,comment,levelid,percentage,type):
        part_1 = username + comment + levelid + str(percentage) + type + "xPT6iUrtws0J"
        return base64.b64encode(xor(hashlib.sha1(part_1.encode()).hexdigest(),"29481").encode()).decode()
def xor(data, key):
        return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(data, cycle(key)))
def gjp_encrypt(data):
        return base64.b64encode(xor(data,"37526").encode()).decode()
def gjp_decrypt(data):
        return xor(base64.b64decode(data.encode()).decode(),"37526")

def getGJUsers(target):
    data={
        "secret":"Wmfd2893gb7",
        "str":target
    }
    request =  requests.post("http://www.boomlings.com/database/getGJUsers20.php",data=data,headers={"User-Agent": ""}).text.split(":")[1::2]
    username = request[0]
    uuid = request[2]
    accountid = request[10]
    return (username,accountid,uuid)

def uploadGJComment(name,passw,comment,perc,level):
    print("[Information]  Uploading comment...")
    try:
        accountid = getGJUsers(name)[1]                                                                                                                        
        gjp = gjp_encrypt(passw)
        c = base64.b64encode(comment.encode()).decode()
        chk = comment_chk(username=name,comment=c,levelid=str(level),percentage=perc,type="0")
        data={
            "secret":"Wmfd2893gb7",
            "accountID":accountid,
            "gjp":gjp,
            "userName":name,
            "comment":c,
            "levelID":level,
            "percent":perc,
            "chk":chk
        }
        return requests.post("http://www.boomlings.com/database/uploadGJComment21.php",data=data,headers={"User-Agent": ""}).text
    except:
        return "Error"

def uploadGJMessage(user, passw, sendto, subject, message):
    print("[Information]  Uploading message...")
    try:
        data = {
            "accountID": getGJUsers(user)[1],
            "gjp": gjp_encrypt(passw),
            "toAccountID": getGJUsers(sendto)[1],
            "subject": base64.b64encode(subject.encode()).decode(),
            "body": base64.b64encode(message.encode()).decode(),
            "secret": "Wmfd2893gb7",
        }
        return requests.post('http://www.boomlings.com/database/uploadGJMessage20.php', data=data, headers={"User-Agent":""}).text
    except:
        return "Error"
def uploadGJFriendRequest(user, passw, sendto, comment):
    print("[Information]  Uploading friend request...")
    try:
        data = {
            "accountID": getGJUsers(user)[1],
            "gjp": gjp_encrypt(passw),
            "toAccountID": getGJUsers(sendto)[1],
            "comment": base64.b64encode(comment.encode()).decode(),
            "secret": "Wmfd2893gb7",
        }
        return requests.post('http://www.boomlings.com/database/uploadFriendRequest20.php', data=data, headers={"User-Agent":""}).text
    except:
        return "Error"

def fetchInfo():
    data={
        "gameVersion":"21",
        "binaryVersion":"35",
        "gdw":"0",
        "type":"4",
        "str":"",
        "diff":"-",
        "len":"-",
        "page":"0",
        "total":"0",
        "uncompleted":"0",
        "onlyCompleted":"0",
        "featured":"0",
        "original":"0",
        "twoPlayer":"0",
        "coins":"0",
        "epic":"0",
        "secret":"Wmfd2893gb7"
    }
    fetched = requests.post("http://www.boomlings.com/database/getGJLevels21.php",data=data,headers={"User-Agent": ""}).text
    return (fetched.split(":")[1],fetched.split(":")[3],getGJUsers(fetched.split(":")[7])[0],fetched.split(":")[7])

print(" /\_/\                    FastPop")
print("( . . )            by NumbersTada")
print(">)-A-(<   Popularity in a second!")
print("Thanks Sevenworks for helping me!")
print("---------------------------------")
print("[Loading]      Reading config.dat")
with open("config.dat", mode="r", encoding="utf-8") as configfile:
    config=configfile.read().split(";")
    username=config[0]
    password=config[1]
print("[Message]      Successfully loaded.")
input("[Confirmation] Press ENTER to start the bot (using account "+username+").")
with open("FastPopLog.log", mode="a", encoding="utf-8") as log:
    print("----------------------------------------------------", file=log)
    print("[Information]  Bot started with account "+username, file=log)
lvlID = ""
lvlName = ""
lvlAuthor = ""

while True:
    with open("FastPopLog.log", mode="a", encoding="utf-8") as log:
        infoList = fetchInfo()
        lvlID = infoList[0]
        lvlName = infoList[1]
        lvlAuthor = infoList[2]
        lvlAuthorID = infoList[3]
        comments = [
            "Meow!",
            "I like this",
            "Approved by "+username,
            "xD",
            "Hello friend!",
            ":3",
            "Cool level",
            "[CoolLevelDetector] Cool level detected (ID: "+lvlID+")",
            "Meowwwww",
            "LOL why did that happen",
            "Rly cool effects",
            "Damn this is really hard",
            ":extremeDemon:",
            "pog",
            "POV: you created a really cool level and it doesn't get rated",
            "Meow",
            ":starRate:",
            "This goes hard",
            "W",
            "uploadComment('This is really cool!')",
            "liked",
            "liked, cool",
            "yooooo",
            "swag",
            "Gamer moment",
            "xDDDD",
            "/!\ ALERT  Good level detected. ID: "+lvlID,
            "...",
            " ",
            "Sussy impasta",
            "Hello "+lvlAuthor,
            "Hi "+lvlAuthor+", I like this level!",
            "UwU",
            "Insert likebegging here",
            "POV: you likebegged and actually got likes",
            "like this comme (Windows NT)",
            "haha yeah",
            "Imagine dying at 69% LOL",
            "Featured?",
            "*likebegs* *gets smashed by this amazing level*",
            "c o o l   l e v e l   l o l",
            "topkek",
            "LMAO",
            "I found a LOT of swag routes.",
            "This is cool NGL",
            "Meow meow :3",
            "Can you please make me a challenge? Thank you :)",
            "Hello "+lvlAuthor+", could you make a challenge for me please?",
            "how do i make a cat out of characters in gd help me",
            "LOL secret way",
            "this would get a rate on a GDPS",
            "dayum",
            "Mewo",
            "level of the year",
            "W level",
            "I thought I am not playing GD",
            "Woah, it's Wulzy",
            "Woah, it's "+username+", welcome back to another Geometry Dash video. Today we will go through the recent tab.",
            "Got some W's?",
            "Why, just why",
            "counting to 1337",
            "GMD",
            "Cool level xD",
            "uploadFriendRequest("+lvlAuthor+")",
            "nuh uh!",
            
            ]
        friendReqs = [
            "Hi, I like your levels! Can we be friends?",
            ":D",
            "I like your level"+lvlName+"!",
            "Your level "+lvlName+" is cool!",
            "Meow",
            "No message",
            "Hello",
            ":3",
            ]
        msgSubjects = [
            "Yoooooo, cool level!",
            "Cool levels detected on your account",
            "Here from level "+lvlName+"!",
            ":)",
            ":3",
            ]
        msgMessages = [
            "Meow!",
            "I like your level!",
            ]
        print("[Fetching]     Fetched level ID "+lvlID+" ("+lvlName+" by "+lvlAuthor+")")
        def percentage():
            if random.randint(0,2) == 0:
                return random.randint(0,100)
            else:
                return 0
        if random.randint(0,3) >= 2:
            cResponse = str(uploadGJComment(username,password,random.choice(comments),percentage(),lvlID))
            print("[Information]  Comment uploaded ("+cResponse+")")
            print("[Information]  Comment uploaded ("+cResponse+")", file=log)
        if random.randint(0,1) == 0:
            fResponse = str(uploadGJFriendRequest(username,password,lvlAuthor,random.choice(friendReqs)))
            print("[Information]  Friend Request uploaded ("+fResponse+")")
            print("[Information]  Friend Request uploaded ("+fResponse+")", file=log)
        if random.randint(0,1) == 2:
            mResponse = str(uploadGJMessage(username,password,lvlAuthor,random.choice(msgSubjects),random.choice(msgMessages)))
            print("[Information]  Message uploaded ("+mResponse+")")
            print("[Information]  Message uploaded ("+mResponse+")", file=log)
        time.sleep(random.randint(25,45))
