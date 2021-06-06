@bot.command(name="타이머", aliases=["timer"])
async def timer(ctx, time:int):
    async with ctx.typing():
        await ctx.send(f"{time}초 타이머가 시작 되었습니다!")
        await asyncio.sleep(time)
        await ctx.send(f"{ctx.author.mention}, {time}초가 지났습니다!")
