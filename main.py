import os

import discord
from discord.ext import commands
from bad_words import BadWords


def main():
    TOKEN = ''
    intents = discord.Intents.all()
    client = commands.Bot(intents=intents, help_command=None)
    bad_words = BadWords()

    @client.event
    async def on_ready():
        print('{0.user} hat die Bar betregen.'.format(client))
        await client.change_presence(activity=discord.Game(name="Cricket Simulator 22"))

    @client.event
    async def on_message(message):
        if bad_words.forbidden_words(message.content):
            await message.add_reaction('\U0001F6AB')
            await message.channel.send(f'{message.author.mention} Wortwahl!!')


    client.run(os.environ['TOKEN'])

if __name__ == '__main__':
    main()
