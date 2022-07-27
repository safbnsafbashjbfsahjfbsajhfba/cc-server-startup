from secrets import token_urlsafe
from turtle import end_fill
import discord
import os

import cloudscraper, time
from colorama import Fore, Back, Style
import colorama
from python_aternos import Client
colorama.init()

aternos = Client.from_credentials('super256yes', 'super256!')

# Returns AternosServer list
servs = aternos.list_servers()
toker = input("Enter your bot token: ")
# Get the first server by the 0 index
myserv = servs[0]
status = 'Status: {}'.format(myserv.status)
class MyClient(discord.Client):
    async def on_ready(self):

        print('Logged on as', self.user)
        print(Fore.RED)
        print ("\033[A                             \033[A")


    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == '!start':
            await message.channel.send('Starting CobbleCraft!')
            print(Fore.GREEN + "[BOT]: Sent requested startup")
            print(Fore.RED)
            print ("\033[A                             \033[A")

            myserv.start()
        if message.content == '!status':
            print(Fore.GREEN + "[BOT]: Sent requested status")
            print(Fore.RED)
            print ("\033[A                             \033[A")
            await message.channel.send(status)
            
client = MyClient()
client.run(toker)

