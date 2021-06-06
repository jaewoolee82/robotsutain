@bot.command(name="핑", aliases=["ping"])
async def ping(ctx):
    gcolor = 0x336BFF
    ecolor = 0x00ff56
    ncolor = 0xD9EA33
    omgcolor = 0xFF0000
    errorcolor = 0xC70039
    pings = round(bot.latency*1000)
    if pings < 100: 
        pinglevel = '🔵 매우좋음'
        color=gcolor
    elif pings < 200:
        pinglevel = '🟢 양호함'
        color=ecolor
    elif pings < 300:
        pinglevel = '🟡 보통'
        color=ncolor
    elif pings < 500:
        pinglevel = '🔴 나쁨'
        color=errorcolor
    else:
        pinglevel = '🔴 매우나쁨'
        color=omgcolor
    embed = discord.Embed(title="🏓 | Pong!", description=f"{pings}ms\n{pinglevel}", color=color)
    await ctx.send(embed=embed)
