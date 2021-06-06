@bot.command(name="채팅청소")
async def clean(ctx, number: int):
    if ctx.author.guild_permissions.manage_messages or ctx.author.id in administer:
        if number <= 120: #지우는 메시지가 120개 이하라면
            await ctx.channel.purge(limit=number + 1)
            embed = discord.Embed(color=0x00FF27, description=f"{number} 개의 메시지를 삭제했어요!")
            await ctx.send(embed=embed, delete_after=5)
        else:
            await ctx.message.delete()
            embed = discord.Embed(color=0xFF0000, description=f"{number}개의 메시지를 지울수 없습니다... `120`개 이하의 메시지만 삭제할 수 있습니다!")
            await ctx.send(embed=embed, delete_after=5)
    else:
        await ctx.message.delete()
        embed = discord.Embed(color=0xFF0000, description=f"{ctx.author.name}님, 채팅 지우기 권한이 없어요...")
        await ctx.send(embed=embed, delete_after=5)
