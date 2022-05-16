"""Simple functions to act as irregular checks."""


def is_cmd_channel(ctx):
    """
    Return True if the channel is a command channel.

    Args:
        ctx: the context the command was called in.

    Returns:
        True or False depending on if the channel is a command channel.
    """
    channel_ids = [973583752477433896, 973421932546519090]
    return ctx.channel.id in channel_ids
