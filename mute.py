@bot.command(name="뮤트", aliases=["mute"])
async def mute(ctx, user: discord.User):
    if ctx.author.guild_permissions.kick_members:
        await ctx.guild.get_channel(ctx.channel.category_id).set_permissions(user, send_messages=False)
        await ctx.send(f"{user}님을 뮤트 하였습니다!")
    else:
      await ctx.send("님은 추방할수 있는 권한이 없습니다!")
