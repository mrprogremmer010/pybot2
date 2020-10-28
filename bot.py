import discord
import random
#from discord importin commands
from discord.ext import commands
#set us the sign to execute our bot and intencing the bot
client = commands.Bot(command_prefix = '.')
#event is a bit of code that runs when the bot detects an activity and we always need him
#declaring that we are to do event 
@client.event
#execute the commands when the bot is ready
async def on_ready():
    print ('the bot is online')
@client.event
#def function that detects whenever member is joined then he printing us member has joined
async def on_member_join(ctx,member):
    author = ctx.message.author
    channel = ctx.channel
    await channel.send(f'{author.mention} has joined')
#def function that tells us when member has left
@client.event
async def on_member_remove(ctx,member):
    author = ctx.message.author
    channel= ctx.channel
    await channel(f'{author.mention} has left')


@client.command()
#extansion represents us the cog thah we to load
async def load(ctx,extension):
    #load cog method
    client.load_extension()


@client.command()
async def fuck(ctx):
    author = ctx.message.author
    #if this is my id with int write hello dad
    if ctx.author.id == 310754465684914176:
        await ctx.send(f"fuck me daddy {author.mention}:sweat_drops:")
    #if its someone else write hello fucker
    else:
        await ctx.send("hello fucker")

@client.command()
async def ping(ctx):
    #sending us the leatcny and converting it to ms
    await ctx.send(f'your latency is {round(client.latecncy * 1000)} in ms')

@client.command(aliases=['8ball'])
#getting the contex then the question
async def _8ball(ctx,*,question):
    #response
    response = ['yes','no','maybe']
    #writng the Question drop a line then choose random response 
    await ctx.send(f'Question:{question}\n Answer:{random.choice(response)}')
    
@client.command()
#define our default amount
async def clear(ctx,amount = 5):
    #deleting with purge
    await ctx.channel.purge(limit=amount)
@client.command()
#getting us the member object from the audit log for we can mention the member and we typing the reson
async def kick(ctx , member : discord.Member,*,reasond=None):
    #the kick method
    await member.kick(reason=reasond)
    await ctx.send(f"kicked{member.mention}")

@client.command()
async def ban(ctx , member : discord.Member,*,reason=None):
    #the ban method
   await member.ban(reason=reason)
   await ctx.send(f"banned{member.mention}")

@client.command()
async def hello(ctx):
    #defining the author of the message 
    author = ctx.message.author
    #defining the channel 
    channel = ctx.channel
    #responses list 
    responsess= ['hello tsadik','hello gay']
    #sending to the channel
    await channel.send(f"{random.choice(responsess)}{author.mention}:eggplant:")


@client.command()
async def sasihuy(ctx):
    author= ctx.message.author
    channel= ctx.message.channel
    if ctx.author.id == 310754465684914176:
        await channel.send(f"dont sasihuy you are my dad {author.mention}")

    else:
        pin = ['8=D','8==D','8===D','8====D','8=====D','8========D','8=================D']
        await channel.send(f'{author.mention}sasi huy vot takoy {random.choice(pin)} ')

@client.command()
async def nigga(ctx):
    await ctx.send(":bearded_person: :bearded_person: :bearded_person: :bearded_person: :woman_red_haired: :bearded_person: :bearded_person: :bearded_person: :bearded_person:")

@client.command()
#taking ctx and member that doesnt in the server
#the * sign taking all the arguments as a member
#guild is method that gets all the from the server and changing them
async def unban(ctx, *,member):
    #guild getting us the banned users list and generating them as a name tupple guild = server
    banned_users = await ctx.guild.bans()
    #accessing the member name and the member discriminator
    member_name, member_discriminator = member.split('#')
    #going thourgh all the banned members in bannd member variable
    for ban_entry in banned_users:
        user = ban_entry.user
        #if user name and discriminator is = to the name of ther user and his discriminator
        if (user.name, user.discriminator ) == (member_name,member_discriminator):
            #the unban command
            await ctx.guild.unban(user)
            await ctx.send(f'unbanned {user.mention}')
            #stopping the loop
            return


    

@client.command()
async def amongus(ctx):
    player=['noam','mavtiah the amit','eitan','idan','shalev']
    await ctx.send(f'the killer is {random.choice(player)}')


#run the bot
client.run('NzU1NjU2MTkxOTEyMzEyOTIz.X2Gdqw.Td-xRpEbI8EQ2VkoqELkvB9BDk8')
