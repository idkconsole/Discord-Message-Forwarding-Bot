import discord
from discord.ext import commands
import os
import sys
import asyncio 
os.system('clear')
cid1 = 1061296695046058015 # msg
cid2 = 1061296731557470380 # log

client = commands.Bot(command_prefix='nword',intents=discord.Intents.all(),help_command=None)

@client.event
async def on_ready():
  print(f'connected to {client.user}')

async def pussy():
  while True:
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=".gg/codez"), status=discord.Status.idle)

@client.event
async def on_message(message):
  if message.channel.id == cid1:
    pass
  else:
    return
  if message.author.bot:
    return
  content = message.content
  author = message.author
  sv = message.guild
  if content == "":
    content = "None"
  try:
    if message.reference.resolved.author:
      x=f"\nReplying To: {message.reference.resolved.author}"
  except Exception as e:
    x=""
  em = discord.Embed(title='Sync Bot',description=f'Message Content: {content}\nGuild Name: {sv.name}\nMessage sent by: {author}\nChannel: {message.channel.name}{x}', color=0x2f3136)
  if message.attachments:
    urx = ""
    for attach in message.attachments:
      urx+=f"{attach.url}\n"
    em.add_field(name="Attachments", value=urx)
  channel = client.get_channel(cid2)
  await channel.send(embed=em)
  await client.process_commands(message)

@client.event
async def on_disconnect():
  os.system("kill 1 && python3 main.py")

try:
  client.run("")
except:
  os.system("kill 1 && python3 main.py")
