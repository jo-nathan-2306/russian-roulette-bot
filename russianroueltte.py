import discord
from discord.ext import commands
import random
import os
game_going_on= False
rolled= False
people=[]
client= commands.Bot(command_prefix='r ',help_command=None)
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("Russian Roulette"))
    print("Works")
@client.command()
async def help(ctx):
        embed=discord.Embed(title="Commands",color=0xe20303)
        embed.add_field(name="r join",value="enters the russian roulette match")
        embed.add_field(name="r leave",value="removes yourself from the match")
        embed.add_field(name="r quit",value="removes everyone from the match")
        embed.add_field(name="r remove [member]",value="removes the specified user from the match")
        embed.add_field(name="r roll",value="rolls the barrel, only to be done when everyone joins")
        embed.add_field(name="r shoot",value="pulls the trigger of the gun")
        embed.add_field(name="tip",value="If an admin plays, he/she cannot be removed")
        embed.add_field(name="feedback",value="for any feedback/bug report, please contact the dev,at the [discord server](https://discord.gg/vfgEREhQep) or instagram @jo_nathan_2306")
        await ctx.send(embed=embed)
@client.command()
async def join(ctx):
    if game_going_on is True:
        await ctx.send("you cant join since the barrel has already been rolled")
    if game_going_on is False:
        people.append(ctx.author)
        await ctx.send("Thank you for joining russian roulette, say r roll once to roll the barrel and r shoot to shoot")
@client.command()
async def leave(ctx):
   if game_going_on is True:
        await ctx.send("you cant leave since the barrel has already been rolled")
   if game_going_on is False:
       people.remove(ctx.author)
       await ctx.send("lmao coward, if you changed your mind say r join")
   else:
       await ctx.send("Dumbass you didn't even join")
@client.command()
async def quit(ctx):
    global rolled,game_going_on
    people.clear()
    await ctx.send("lmao yall are pussies")
    game_going_on=False
    rolled=False
@client.command()
async def roll(ctx):
    global rolled,game_going_on
    
    global chosen
    chosen=random.choice(people)
    if len(people)>1:
        game_going_on= True
        rolled= True
        await ctx.send(f"The barrel has been rolled,1 person out of {len(people)} will die")
    else:
        await ctx.send("Lmao wait for more people")
@client.command()
async def remove(ctx, user : discord.Member):
    if user in people:
        people.remove(user)
        await ctx.send(f"@{user} removed from list")
    else:
        await ctx.send("Ayo fam, that person aint there")
@client.command()
async def shoot(ctx):
    if ctx.author in people:
        if rolled is True:
            if ctx.author==chosen:
                await ctx.send(":gun: You pull the trigger and.....")
                channel= await discord.Member.create_dm(chosen)
                await channel.send("Welcome to the afterlife, you got shot")
                await discord.Member.kick(chosen)
                await ctx.send(f"{chosen} died lmao")
                people.clear()
            elif ctx.author not in people:
                await ctx.send("You already tried")
            elif ctx.author !=chosen:
                await ctx.send(":gun: You pull the trigger and.....")
                await ctx.send("you are safe")
                people.remove(ctx.author)
        else:
            await ctx.send("Dumbass roll the gun")
    else:
        await ctx.send("You either already tried or you didnt join")
client.run(os.environ['DISCORD_TOKEN'])
