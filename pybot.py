import discord
import random
from discord.ext.commands import Greedy
#from discord importin commands
from discord.ext import commands
import os
from random import randint
from discord.ext import tasks
from itertools import cycle
import asyncio
import sys
client = commands.Bot(command_prefix = 'py ')
from discord.voice_client import VoiceClient
from random import choice


@client.command()
async def gif(ctx):
    member = ctx.guild.members
    giflist=['https://tenor.com/view/punt-kick-baby-grandma-gif-8217719','https://tenor.com/view/jew-tsoptihs-gif-8882100','https://tenor.com/view/mindfuck-mind-fuck-sex-brain-gif-17418377']
    await ctx.send(random.choice(giflist))
    await ctx.send(f"{random.choice(member)}")
@client.command()
async def hentai(ctx):
    hentai=['https://tenor.com/view/anime-anna-nishikinomiya-shimoneta-steam-shower-gif-12190819','https://tenor.com/view/hentai-panties-butt-anime-anime-girl-gif-16161778','https://tenor.com/view/dancing-anime-sexy-hentai-gif-5476864']
    await ctx.send(random.choice(hentai))
       

#set us the sign to execute our bot and intencing the bot

#making a list that will run in a cycle
status= cycle(['BEING CODED BY A GOD'])
#event is a bit of code that runs when the bot detects an activity and we always need him
#declaring that we are to do event 
@client.event
#execute the commands when the bot is ready
async def on_ready():
    #starting the loop 
    status_change.start()
    #changing the status of the bot and activity
    await client.change_presence(status= discord.Status.online,activity=discord.Game("BEING CODED BY A GOD"))
    print ('the bot is online')
@client.event
#def function that detects whenever member is joined then he printing us member has joined
async def on_member_join(ctx):
    author = ctx.author.mention
    channel = ctx.channel
    await channel.send(f'{author.mention} dont be gay be tsadik ')
#def function that tells us when member has left
@client.event
async def on_member_remove(ctx):
    author = ctx.author.mention
    channel = ctx.channel
    await channel.send(f'{author.mention} is gay idiot')
@client.command()
async def ping2(ctx):
    await ctx.send("enter ping")
    await client.wait_for('message')
    await ctx.send('pong')
#wating 12 hours and then run the loop 
#task is something that will run in the background
@tasks.loop(hours=12)
async def status_change():
    #changing the status by getting game object and next status
    await client.change_presence(activity=discord.Game(next(status)))



@client.command()
#extansion represents us the cog that we to load
async def load(ctx,extension):
    #load cog method and searching the cog
    #have to be the same name as the folder to make it know where to go
    client.load_extension(f"example.{extension}")


@client.command()
async def boker(ctx):
    await ctx.send("BOKER TOV TO EVERYONE ")


@client.command()
#extansion represents us the cog thah we to unload
async def unload(ctx,extension):
    #unload cog method and searching the cog
    #have to be the same name as the folder to make it know where to go
    client.unload_extension(f"example.{extension}")

#getting all the files that ends it with py in the directory
for filename in os.listdir("./example"):
    if filename.endswith(".py"):
        #cutting of the last three charectres
        #have to be the same name as the folder to make it know where to go
        client.load_extension(f"example.{filename[:-3]}")
        

@client.command(name='one', help = 'onepiece')
async def one(ctx):
    respones1=['one piece is and anime that only gods watching','one piece i an good anime ', 'one piece is the best anime in the world','one piece is the best']
    await ctx.send(random.choice(respones1))
@client.command(name= 'random', help='this command picks random member ')
async def _random(ctx):
    listmembers=['']
    member  = ctx.guild.members
    random1= random.choice(member)
    listmembers.append(member)
    await ctx.send(f'your member is {random1}')


@client.command()
async def cul(ctx):
    author = ctx.author.mention
    num1 = await ctx.send('enter number 1')
    msgnum=await client.wait_for('message')
    num2 =  await ctx.send('enter number 2')
    msgnum2=await client.wait_for('message')   
    signal = await ctx.send("enter signal between number")
    signalWait = await client.wait_for('message')
    try:
        #declearing that the variable is int 
        num3=int(msgnum.content)
        num4=int(msgnum2.content)
    except ValueError:
        await ctx.send("invaild option pls enter an number you BAKKA")  
        #returning us output
        return 
    
    var5=str(signalWait.content)
    if var5 == '+':
        await ctx.send(f'this is sum: {num3+num4}')
    elif var5 == '*':
        await ctx.send(f'this is double: {num3*num4}')
    elif var5 == '**':
        await ctx.send(f' this is exponent: {num3**num4}')
        await ctx.send(f'this is exponent but the numbers switch place: {num4**num3}')
    elif var5 == '/':
        await ctx.send(f'this is portion with rest: {num3/num4}')
        await ctx.send(f'this is portion but the numbers switch place: {num4/num3}')
    elif var5 == '//':
        await ctx.send(f'this is portion without rest: {num3//num4}')
        await ctx.send(f'this is portion without the rest but the numbers switch place: {num4//num3}')

    elif var5 == '%':
        await ctx.send(f'this is rest: {num3%num4}')
        await ctx.send(f'this is rest but the numbers switch place: {num4%num3}')
    elif var5 == '-':
        await ctx.send(f' this is Subtraction: {num3-num4}')
        await ctx.send(f'this is Subtraction but the numbers switch place: {num4-num3}')

    else:
        await ctx.send('pls eneter a sign')
        return

    if num1.author.mention != author:
        num1= await client.wait_for('message')
    elif num2.author.mention != author:
        num2= await client.wait_for('message')  
    else:
        massageStatus = False      
balance = 0
@client.command()
async def tsadik(ctx):   
    
     if ctx.author.id == 343713973432090625:
        author = ctx.author.mention
        await ctx.send(f"you are fucking born to be gay atheist :woman_with_headscarf: ")
     #elif ctx.author.id == 310754465684914176:
        #prectage = 1000
        #await ctx.send(f"of course you tsadik you made me :star_of_david:")  

     else:
         cut = ['tsadik','atheist','muslemi','nothri',]
         await ctx.send("what do you think you are? ")
         await ctx.send(f"`{cut}`")
         answer = await client.wait_for('message')
         choose = random.choice(cut)
        #content of the message that user it typed 
         if answer.content == choose:
            balance = random.randint(0,300)
            await ctx.send ("you were right")
            await ctx.send(f"you are {choose}")
            await ctx.send(f"wow you got {balance} shekels")

         else:
            await ctx.send("you were wrong")
            await ctx.send(f"you are {choose} ")
            #dont continue if the user isnt the same user
         if answer.author.mention != author:
             answer = await client.wait_for('message')
         else:
            massageStatus = False       




@client.command()
async def fuck(ctx):
    author = ctx.message.author
    #if this is my id with int write hello dad
    if ctx.author.id == 310754465684914176:
        await ctx.send(f"fuck me daddy {author.mention}:sweat_drops:")
    #if its someone else write hello fucker
    elif ctx.author.id == 756079944693448745:
        await ctx.send(f"ok mia lets go fuck :eggplant:")
    
    else:
        await ctx.send("hello fucker")

@client.command()
async def ping(ctx):
    #sending us the leatcny and converting it to ms
    await ctx.send(f"pong {round(client.latency *1000)} in ms ")

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
    #deleting messages with purge
    await ctx.channel.purge(limit=amount)


@client.command()
#getting us the member object from the audit log for we can mention the member and we typing the reson
async def kick(ctx , member : discord.Member,*,reasond=None):
    #the kick method
    await member.kick(reason=reasond)
    await ctx.send(f"kicked{member.mention}")

@client.command()
#taking member as a object and put him on the reason
async def ban(ctx , member : discord.Member,*,reason=None):
    #the ban method
   await member.ban(reason=reason)
   await ctx.send(f"banned{member.mention}")

@client.command()
async def dm(ctx ,user_id = None):
    try:
        #getting the user id 
        target = await client.fetch_user(user_id)
        #sending the message to the user 
        await target.send("hello fucker")
        if user_id == 756079944693448745:
            await target.send("hello my love forever :heart:")

    except:
        await ctx.send("pls enter member")




@client.command()
async def spam(ctx, member : discord.Member = None):
    author = ctx.author.mention
    if member is None:
      await ctx.send("pls enter member")
    else:
        while True:
            await ctx.send(f"gay you turned me on from my sleep now i will not stop{member.mention}")
    @client.command()
    async def stop(ctx):
        await client.logout()



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
async def mute(ctx, member : discord.Member):
    guild = ctx.guild


    for role in guild.roles:
        if role.name == "Muted":
            await member.add_roles(role)
            await ctx.send("{} has {} has been muted" .format(member.mention,ctx.author.mention))
        

            overwrite = discord.PermissionOverwrite(send_messages=False)
            newRole =  await guild.create_role(name="Muted")

            for channel in guild.text_channels:
                await channel.set_permissions(newRole,overwrite=overwrite)

            
            await ctx.send("{} has been muted by {} has been muted" .format(member.mention,ctx.author.mention))
        else:
            await member.add_roles(newRole)

@client.command()
async def unmute(ctx, member : discord.Member):
    guild = ctx.guild


    for role in guild.roles:
        if role.name == "Muted":
            await member.remove_roles(role)
            await ctx.send("{} has been muted by {} has been unmuted" .format(member.mention,ctx.author.mention))
            return


dyingPlayers= []
@client.command()
async def rolutte(ctx):
    #define the channel    
    channel = ctx.channel
    #define the author
    author = ctx.author.mention
    #if author is in the comp list say you are in the comp list 
    if author in dyingPlayers:
        await channel.send(f"{author} You are in the rolutte list wait for {5 - len(dyingPlayers)} player(s)")
    #if the player isnt in the list append his name on the list and say you are joined
    else:
        dyingPlayers.append(author)
        await channel.send(f"{author} you have joined to {dyingPlayers} rolutte ")
    #if there is 5 player in the list send lets go
        if len(dyingPlayers) == 4:
            await ctx.send('good luck everyone dont die')
            await client.wait_for('message')
        @client.command()
        async def start(ctx):
            for author in dyingPlayers:
                choice= random.choice(dyingPlayers)
                await channel.send(f"the man who is died :gun: {choice} ")
                dyingPlayers.clear()
                if author == choice:
                    dyingPlayers.remove(author)
            if len(dyingPlayers) == 1:
                await channel.send(f"the man who survived is {dyingPlayers}")
            return
@client.command()
async def sasihuy(ctx):
    author= ctx.message.author
    channel= ctx.message.channel
    #if this is my id 
    if ctx.author.id == 310754465684914176:
        #send dont sasihuy
        await channel.send(f"dont sasihuy you are my dad {author.mention}")
    elif ctx.author.id ==756079944693448745:
        await channel.send(f"{author.mention}i dont have a huy that will make you sastify you need somthing like this 8====================================D ")
    #if its not me send normal message
    else:
        pin = ['8=D','8==D','8===D','8====D','8=====D','8========D','8=================D']
        await channel.send(f'{author.mention}sasi huy vot takoy {random.choice(pin)} ')





compPlayers = []
@client.command()
async def joincomp(ctx):
    #define the channel    
    channel = ctx.channel
    #define the author
    author = ctx.author.mention
    #if author is in the comp list say you are in the comp list 
    if author in compPlayers:
        await channel.send(f"{author} You are in the comp list wait for {5 - len(compPlayers)} player(s)")
    #if the player isnt in the list append his name on the list and say you are joined
    else:
        compPlayers.append(author)
        await channel.send(f"{author} you have joined to {compPlayers} comp")
    #if there is 5 player in the list send lets go
    if len(compPlayers) == 5:
        await channel.send(f"LETS GOOO {compPlayers} ARE READY! good luck:trophy:")
        compPlayers.clear()

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
    #accessing the member name and the member discriminator and spiliting them
    member_name, member_discriminator = member.split('#')
    #going thourgh all the banned members in bannd member variable
    for ban_entry in banned_users:
        user = ban_entry.user
        #if we typing user name and discriminator is = to the name of ther user and his discriminator
        if (user.name, user.discriminator ) == (member_name,member_discriminator):
            #the unban command
            await ctx.guild.unban(user)
            await ctx.send(f'unbanned {user.mention}')
            #stopping the loop
            return

@client.command()
async def amongus(ctx):
    player=['orange','mavtiah the amit','eitan','idan','shalev']
    await ctx.send(f'the killer is {random.choice(player)}')

@client.command()
async def num(ctx):
    num1=await ctx .send('maximum number')
    msg1=await client.wait_for('message')
    num2=await ctx.send("enter minimum number")
    msg =await client.wait_for('message')
    #switching us the string to int 
    var1=int(msg.content)
    var2=int(msg1.content)
    if var2-var1 == 5:
        await ctx.send(var1)
        await ctx.send(var2)
    else:
        await ctx.send("enter a number the will equls to 5")




client.run('token')
