import os


def getAllSubDir(path):
    subfolders = [f.path for f in os.scandir(path) if f.is_dir()]
    return subfolders


def XoaFilePath(path):
    os.remove(path)

#
# for folder in getAllSubDir(fr'{os.getcwd()}\Tele\Tele'):
#     filePath = fr'{folder}\Telegram.exe'
#     try:
#         XoaFilePath(filePath)
#     except:
#         pass

# with open('TelePath.txt' , 'w') as file:
#     for folder in getAllSubDir(fr'{os.getcwd()}\Tele\Tele'):
#         file.write(f'{folder}\n')
#     file.close()

import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix = 'bday ', intents = intents)

@client.event
async def on_ready():
    guild = client.get_guild(873805775460511765)
    memberList = guild.members
    print(memberList)
client.run('OTE5MjI1MDI4MzYzNTU4OTQz.YbStBQ.CW9nFQitspenp0gYyj0UEk0RNE8')