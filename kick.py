@bot.command(name="추방", aliases=['킥'])
async def kickuser(ctx, member: discord.Member):
    if ctx.author.guild_permissions.kick_members or ctx.author.id in administer:
        try:
            await ctx.guild.kick(member)
        except:
            await ctx.send("사용자를 추방하지 못했어요...")
        else:
            await ctx.send(f"{member}님을 킥했어요!")
