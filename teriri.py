import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='-')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

@bot.command(name='hello', help='ご挨拶')
async def _hello(ctx):
    member = ctx.author.mention

    greetings = [
        'ハロー',
        f'{member}, こんばんは〜',
        'こんばんは〜',
        'テリテリ〜？',
        'ツンツンしないで、怒るわよ',
    ]

    response = random.choice(greetings)
    await ctx.send(response)

@bot.command(name='hug', help='気持ちいいハグ〜')
async def _hug(ctx, *, arg: str = ''):
    member = ctx.author.mention

    if arg == '':
        hug = 'ぎゅってしたい！'
        response = f'{member} が ' + hug
    else:
        hugs = [
            'を抱きしめる〜♡',
            'からのハグを待っている！',
        ]
        response = f'{member} が {arg} ' + random.choice(hugs)

    await ctx.send(response)

bot.run(token)
