@bot.command(name="ν", aliases=["ping"])
async def ping(ctx):
    gcolor = 0x336BFF
    ecolor = 0x00ff56
    ncolor = 0xD9EA33
    omgcolor = 0xFF0000
    errorcolor = 0xC70039
    pings = round(bot.latency*1000)
    if pings < 100: 
        pinglevel = 'π΅ λ§€μ°μ’μ'
        color=gcolor
    elif pings < 200:
        pinglevel = 'π’ μνΈν¨'
        color=ecolor
    elif pings < 300:
        pinglevel = 'π‘ λ³΄ν΅'
        color=ncolor
    elif pings < 500:
        pinglevel = 'π΄ λμ¨'
        color=errorcolor
    else:
        pinglevel = 'π΄ λ§€μ°λμ¨'
        color=omgcolor
    embed = discord.Embed(title="π | Pong!", description=f"{pings}ms\n{pinglevel}", color=color)
    await ctx.send(embed=embed)
