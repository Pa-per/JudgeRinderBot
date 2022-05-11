import datetime

import discord
from discord.ext import commands

from utils.create import create_embed


class on_join(discord.ext.commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.bot:
            return
        guild = member.guild
        role = guild.get_role(973579954791010314)
        await member.add_roles(role)
        log_channel = guild.get_channel(973410011449536555)
        embed = create_embed(
            title="Member Joined",
            description=f"{member.mention} has joined the server.",
            color=discord.Color.dark_theme(),
            footer=[f"{member}", f"{member.avatar.url}"],
            thumbnail=member.avatar.url,
        )
        embed.add_field(name="Member ID", value=f"`{member.id}`", inline=True)
        created_at = datetime.datetime.timestamp(member.created_at)
        embed.add_field(
            name="Created At", value=f"<t:{int(created_at)}:R>", inline=True
        )
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        joined_at = datetime.datetime.timestamp(member.joined_at)
        embed.add_field(name="Joined At", value=f"<t:{int(joined_at)}:R>", inline=True)
        embed.add_field(
            name="Member #",
            value=f"**{len([i for i in guild.members if not i.bot])}**",
            inline=True,
        )
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        member_check = await self.client.fetch_member(member.id)
        if member_check.banner:
            embed.add_field(name="\u200b", value="**Banner:**", inline=False)
            banner = member_check.banner.url
            embed.set_image(url=banner)
        await log_channel.send(embed=embed)


async def setup(client: commands.Bot):
    await client.add_cog(on_join(client))
