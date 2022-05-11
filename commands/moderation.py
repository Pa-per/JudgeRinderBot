import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(
        name="purge",
        description="Purges a number of messages.",
        usage="<number>"
    )
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def purge(self, ctx, amount: int = None):
        """Purge a number of messages."""
        if amount is None:
            amount = 10
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"Purged {amount} messages.", delete_after=5)

    @commands.command(
        name="kick",
        description="Kicks a user from the server.",
        usage="<user>"
    )
    @commands.has_permissions(kick_members=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def kick(self, ctx, member: discord.Member = None, *, reason: str = None):
        """Kick a user from the server."""
        if member is None:
            return await ctx.reply("🗙 Please specify a user to kick.", mention_author=False)
        if reason is None:
            reason = "No reason provided."
        await member.kick(reason=reason)
        await ctx.reply(f"Kicked {member.mention}.\nReason: {reason}", mention_author=False, delete_after=5)

    @commands.command(
        name="mute",
        description="Mutes a user.",
        usage="<user> [time]"
    )
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member = None, time: str = None):
        if member is None:
            return await ctx.reply("🗙 Please specify a user to mute.", mention_author=False)

async def setup(client: commands.Bot):
    await client.add_cog(Moderation(client))
