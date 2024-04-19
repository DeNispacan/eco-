import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def мусор(ctx):
    await ctx.send(f'мусор нельзя выбрасывать на улитцу ведь-Мусор, оставленный на природе, в итоге окажется в воде, что в свою очередь вредит микроорганизмам, которые вырабатывают кислород.')

@bot.command()
async def ъуъ(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def заводы(ctx):
    await ctx.send(f'Промышленное производство потребляет огромное количество энергии. Это приводит к повышению уровня выбросов парниковых газов, таких как диоксид углерода, которые в свою очередь влияют на изменение климата. Кроме того, потребление энергии может привести к истощению природных ресурсов, таких как нефть, газ и уголь.')

@bot.command()
async def уголь(ctx):
    await ctx.send(f'К основным негативным последствиям для природы относят выбросы метана при разработке угольных пластов и диоксида углерода при сжигании топлива, загрязнение атмосферы угольной пылью, кислотные дожди, разрушение почв, подземные пожары и обвалы горных пород, накопление токсичных отходов.')

bot.run("MTIzMDgyODY5ODM5NjEzNTQyNA.Gi0e9g.83iRE-CDSLall8_dkWKOgHah5UJBujR6mdTd6I")
