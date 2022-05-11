import datetime

import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(
        name="purge", description="Purges a number of messages.", usage="<number>"
    )
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def purge(self, ctx, amount: int = None):
        """purge message within a channel

        Keyword Arguments:
            amount -- the amount of messages to delete (default: {None})
        """
        if amount is None:
            amount = 10
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"Purged {amount} messages.", delete_after=5)

    @commands.command(
        name="kick", description="Kicks a user from the server.", usage="<user>"
    )
    @commands.has_permissions(kick_members=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def kick(self, ctx, member: discord.Member = None, *, reason: str = None):
        """
        kick a user from the guild

        Keyword Arguments:
            member -- the member to kick (default: {None})
            reason -- the reason for the kick (default: {None})

        Returns:
            Returns an error message if no member is specified.
        """
        if member is None:
            return await ctx.reply(
                "🗙 Please specify a user to kick.", mention_author=False
            )
        if reason is None:
            reason = "No reason provided."
        await member.kick(reason=reason)
        await ctx.reply(
            f"Kicked {member.mention}.\nReason: {reason}",
            mention_author=False,
            delete_after=5,
        )

    @commands.command(name="mute", description="Mutes a user.", usage="<user> [time]")
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    async def mute(
        self,
        ctx,
        member: discord.Member = None,
        amount: int = None,
    ):
        """
        mute a user in the guild

        Keyword Arguments:
            member -- the member to mute (default: {None})
            amount -- the amount of time to mute them for (default: {None})

        Returns:
            Returns an error message if no member is specified.
        """
        if member is None:
            return await ctx.reply(
                "🗙 Please specify a user to mute.", mention_author=False
            )
        if amount is None:
            return await ctx.reply(
                "🗙 Please specify a time to mute them for.", mention_author=False
            )
        until = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
            minutes=amount
        )

        await member.timeout(until)
        await ctx.reply(
            f"Muted {member.mention} for {amount} minutes.", mention_author=False
        )

    @commands.command(name="unmute", description="Un-mute a user.", usage="<user>")
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member = None):
        """
        unmute a user in the guild

        Keyword Arguments:
            member -- the member to unmute (default: {None})
        """
        if member is None:
            await ctx.reply("🗙 Please specify a user to un-mute.", mention_author=False)
        await member.timeout(None)
        await ctx.reply(f"Un-muted {member.mention}.", mention_author=False)


async def setup(client: commands.Bot):
    await client.add_cog(Moderation(client))
