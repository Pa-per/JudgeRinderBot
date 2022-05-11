from typing import Optional

import discord


def create_embed(title=None, description: Optional[str] = None, color: Optional[str] = None, thumbnail: Optional[str] = None, image: Optional[str] = None, author: Optional[str] = None, footer: Optional[list] = None):
    color = color or discord.Color.blurple()
    description = description or ""
    Embed = discord.Embed(
        title=title,
        description=description,
        color=color
    )
    if author:
        Embed.set_author(name=author[0], icon_url=author[1])
    if thumbnail:
        Embed.set_thumbnail(url=thumbnail)
    if image:
        Embed.set_image(url=image)
    if footer:
        Embed.set_footer(text=footer[0], icon_url=footer[1])
    return Embed

def profile_embed(requester, user, profile):
    embed = discord.Embed(
        description=f"{user.mention}'s Profile",
        color=discord.Color.dark_theme()
    )
    embed.add_field(name="Level", value=profile[1])
    embed.add_field(name="XP", value=profile[2])
    embed.add_field(name="XP Needed", value=profile[4])
    embed.set_thumbnail(url=user.avatar.url)
    embed.set_footer(text=f"Requested by: {requester}", icon_url=requester.avatar.url)
    return embed
