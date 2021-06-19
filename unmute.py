@bot.command(name="언뮤트", aliases=["unmute"]) 
async def unmute(ctx, user:discord.User):
    if ctx.author.guild_permissions.kick_members:
        await ctx.guild.get_channel(ctx.channel.category_id).set_permissions(user, send_messages=True)
        await ctx.send(f"{user}님을 언뮤트 하였습니다!")
