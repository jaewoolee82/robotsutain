import discord, asyncio
from discord.ext import commands

class Core(commands.Cog):

    def __init__(self, bot): 
        self.bot = bot
    
    @commands.command(name="계산", help="더하기,빼기,곱하기 계산함")
    async def calc(self,ctx,lan:str=None,first:int=None,second:int=None):
        if first==None or second==None:
            await ctx.send("수를 입력해주세요")
        first=int(first)
        second=int(second)
        if lan=="더하기":
            await ctx.send(first+second)
        elif lan=="빼기":
            await ctx.send(first-second)
        elif lan=="나누기":
            await ctx.send(first/second)
        elif lan=="곱하기":
            await ctx.send(first*second)
        else:
            await ctx.send("더하기,빼기,곱하기 또는 나누기를 입력해주세요")

def setup(bot):
    bot.add_cog(Core(bot))
