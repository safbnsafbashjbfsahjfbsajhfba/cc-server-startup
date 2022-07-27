from turtle import end_fill
import discord
import os

import cloudscraper, time
from colorama import Fore, Back, Style
import colorama
from python_aternos import Client
colorama.init()

aternos = Client.from_credentials('CobblecraftSeason5', 'p1zz4p13')

# Returns AternosServer list
servs = aternos.list_servers()

# Get the first server by the 0 index
myserv = servs[0]
status = 'Status: {}'.format(myserv.status)
class MyClient(discord.Client):
    async def on_ready(self):

        print('Logged on as', self.user)


    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == '!start':
            await message.channel.send('Starting CobbleCraft!')

            myserv.start()
        if message.content == '!status':

            await message.channel.send(status)
            
client = MyClient()
client.run('MTAwMTIxMTU5ODQ4NjExNDM2NQ.GLtkoZ.RcxNMZwm1AsjOHB8VexoewLNfSYUhkRvbARSwA')

