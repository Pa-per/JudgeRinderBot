"""The Moderation Cog."""

from datetime import datetime

import discord
from discord.ext import commands


class Moderation(commands.Cog):
    """
    Moderation Class.

    Args:
        commands (_type_): The discord commands module.
    """

    def __init__(self, client):
        """
        __init__ Initialise the Class.

        Args:
            client (_type_): The discord client.
        """
        self.client = client

    @commands.command(
        name='purge',
        description='Purges a number of messages.',
        usage='<number>',
    )
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def purge(self, ctx, amount: int = 10):
        """
        Purge messages from the current channel.

        Args:
            ctx (_type_): The command context to pull from.
            amount (int): The amount of messages to delete.
        """
        await ctx.channel.purge(limit=amount)
        await ctx.send(
            f'Purged {amount} messages.',
            delete_after=5,
        )

    @commands.command(
        name='kick',
        description='Kicks a user from the server.',
        usage='<user>',
    )
    @commands.has_permissions(kick_members=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def kick(self, ctx, member: discord.Member = None, *, reason: str):
        """
        Kick a user from the Guild.

        Args:
            ctx (_type_): The command context to pull from.
            reason (str): The reason for the kick.
            member (discord.Member): The member to kick.
        """
        if reason is None:
            reason = 'No reason provided.'
        await member.kick(
            reason=reason,
        )
        await ctx.reply(
            f'Kicked {member.mention}.\nReason: {reason}',
            mention_author=False,
            delete_after=5,
        )

    @commands.command(
        name='ban',
        description='Ban a user from the server.',
        usage='<user>',
    )
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ban(self, ctx, member: discord.Member = None, *, reason: str):
        """
        Ban a user from the Guild.

        Args:
            ctx (_type_): The command context to pull from.
            reason (str): The reason for the ban.
            member (discord.Member): The member to ban.
        """
        if reason is None:
            reason = 'No reason provided.'
        await member.ban(
            reason=reason,
        )
        await ctx.reply(
            f'Banned {member.mention}.\nReason: {reason}',
            mention_author=False,
            delete_after=5,
        )

    @commands.command(
        name='mute',
        description='Mutes a user.',
        usage='<user> [time]',
    )
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    async def mute(
        self,
        ctx,
        member: discord.Member = None,
        amount: int = None,
    ):
        """
        Mute a user.

        Args:
            ctx (_type_): The command context to pull from.
            member (discord.Member, optional): The member to mute.
            amount (int): The amount of time to mute them for.

        Returns:
            __type_: None if member or amount is None.
        """
        if member is None:
            return await ctx.reply(
                '🗙 Please specify a user to mute.',
                mention_author=False,
            )
        if amount is None:
            return await ctx.reply(
                '🗙 Please specify a time to mute them for.',
                mention_author=False,
            )
        until = datetime.now(datetime.timezone.utc) + datetime.timedelta(
            minutes=amount,
        )

        await member.timeout(until)
        await ctx.reply(
            f'Muted {member.mention} for {amount} minutes.',
            mention_author=False,
        )

    @commands.command(
        name='unmute',
        description='Un-mute a user.',
        usage='<user>',
    )
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member = None):
        """
        Unmute a user in the Guild.

        Args:
            ctx (_type_): The command context to pull from.
            member (discord.Member, optional): The member to unmute.
        """
        if member is None:
            await ctx.reply(
                '🗙 Please specify a user to un-mute.',
                mention_author=False,
            )
        await member.timeout(None)
        await ctx.reply(
            f'Un-muted {member.mention}.',
            mention_author=False,
        )


async def setup(client: commands.Bot):
    """
    Initialise the cog for the client.

    Args:
        client (commands.Bot): The discord client.
    """
    await client.add_cog(Moderation(client))
