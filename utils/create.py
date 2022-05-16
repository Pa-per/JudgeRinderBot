"""Import the discord client."""
import discord


def create_embed(
    title=None,
    description: str = None,
    thumbnail: str = None,
    image: str = None,
    author: str = None,
):
    """
    Create an embed with the given parameters.

    Args:
        title: The title of the embed.
        description: The description of the embed.
        thumbnail: The thumbnail of the embed.
        image: The image of the embed.
        author: The author of the embed.

    Returns:
        Returns an embed with the given parameters.
    """
    color = discord.Color.blurple()
    description = description or ''
    embed = discord.Embed(title=title, description=description, color=color)
    if author:
        embed.set_author(name=author[0], icon_url=author[1])
    if thumbnail:
        embed.set_thumbnail(url=thumbnail)
    if image:
        embed.set_image(url=image)
    return embed


def profile_embed(requester, user, profile):
    """Create an embed with profile parameters.

    Args:
        requester: the user who requested the profile
        user: the user who's profile is being requested
        profile: the profile of the user

    Returns:
        A profile embed for the user.
    """
    embed = discord.Embed(
        description=f"{user.mention}\'s Profile",
        color=discord.Color.dark_theme(),
    )
    embed.add_field(name='Level', value=profile[1])
    embed.add_field(name='XP', value=profile[2])
    embed.add_field(name='XP Needed', value=profile[4])
    embed.set_thumbnail(url=user.avatar.url)
    embed.set_footer(
        text=f'Requested by: {requester}', icon_url=requester.avatar.url,
    )
    return embed
