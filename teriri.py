import os
import random
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from keep_alive import keep_alive


token = os.environ['TOKEN']
bot = commands.Bot(command_prefix='-')
slash_client = SlashCommand(bot)

@slash_client.slash(name="helo")
async def _slash_hello(ctx: SlashContext):
    await ctx.send(content="Hello!")

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
        response = f'{member} が' + hug
    else:
        hugs = [
            'を抱きしめる〜♡',
            'からのハグを待っている！',
        ]
        response = f'{member} が {arg} ' + random.choice(hugs)

    await ctx.send(response)

@bot.command(name='kill', help='誰をころしたいの？')
async def _kill(ctx, *, arg: str = ''):
    member = ctx.author.mention

    if arg == '':
        msg = '殺気を感じる...'
        response = f'{member} から' + msg
    else:
        msgs = [
            f'{member} が {arg} をころす気だぞ！',
            f'{arg} はテリリが守ります！',
        ]
        response = random.choice(msgs)

    await ctx.send(response)

keep_alive()
bot.run(token)
