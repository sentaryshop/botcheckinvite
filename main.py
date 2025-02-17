import discord
from discord.ext import commands
import DiscordUtils
import datetime
import os
from os import system 
from time import sleep
from colorama import Fore

from myserver import server_on


prefixs = '!'
guils_id = 1340207528050556978
logs_welcome_id = 1340207528574717987
logs_leave_id = 1340207528574717989

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = prefixs, intents = intents)
client.remove_command('help')

invtrck = DiscordUtils.InviteTracker(client)

@client.event
async def on_ready():
    system('cls')
    print(' -----')
    print('\n > Login....')
    sleep(1)
    system('cls')
    print(' -----')
    print(f'{Fore.GREEN}\n > Login Token client Done!{Fore.RESET}')
    sleep(0.5)
    system('cls')
    print(' -----')
    print(f'\n > Login Token client : {client.user}')
    print('\n -----')
    await client.change_presence(activity=discord.Streaming(name="Streaming Now", url="https://www.twitch.tv/Sentary.Shop"))

@client.event
async def on_member_join(member):

    inver = await invtrck.fetch_inviter(member) 
    channel = client.get_channel(logs_welcome_id)
    guild = client.get_guild(guils_id)
    total = 0

    for i in await guild.invites():
        if i.inviter == inver :
            total += i.uses

        embedjoin = discord.Embed(
            title = "Restore",
            description = f"คุณ {member.mention} เข้าร่วมเซิฟเวอร์ ยืนยันตัวตนได้ที่<#1246756850834341969>\n\nได้รับคำเชิญจาก : {inver.mention}",
            colour = 0x00FF99
        ) 
        embedjoin.timestamp = datetime.datetime.utcnow()
        embedjoin.set_footer(text=" | RESTORE For Wellcome ")
        embedjoin.set_thumbnail(url = f"{member.avatar.url}")
        
    await channel.send(embed=embedjoin)

@client.event
async def on_member_remove(member):
    
    inver = await invtrck.fetch_inviter(member) 
    channel = client.get_channel(logs_leave_id)
            
    embedremove = discord.Embed(
        title = "สมาชิกได้ออกจากServer",
        description = f"คุณ {member.mention} ออกดิสไปแล้ว",
        colour = 0x00FF99
    ) 
    embedremove.timestamp = datetime.datetime.utcnow()
    embedremove.set_footer(text=" | Restore For Goodbye ")
    await channel.send(embed=embedremove)
    
server_on()

client.run(os.getenv('TOKEN'))