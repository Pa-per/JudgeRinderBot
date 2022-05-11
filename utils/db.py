import aiosqlite


async def create_db():
    db = await aiosqlite.connect("databases/users.sqlite")
    cursor = await db.cursor()
    await cursor.execute(
        f"""
    CREATE TABLE IF NOT EXISTS "profile" (
        "id"    INTEGER,
        "level"    INTEGER,
        "xp"    INTEGER,
        "xp_to_next_level"    INTEGER,
        "xp_needed"    INTEGER,
        "credits"    INTEGER,
        PRIMARY KEY("id")
        );
    """
    )
    await db.commit()
    await db.close()
    print("Users Database Created Successfully.")


async def get_profile(id):
    db = await aiosqlite.connect("databases/users.sqlite")
    cursor = await db.cursor()
    await cursor.execute(f"SELECT * FROM profile WHERE id = {id}")
    result = await cursor.fetchone()
    if not result:
        await create_profile(id)
        await cursor.execute(f"SELECT * FROM profile WHERE id = {id}")
        result = await cursor.fetchone()
    await db.close()
    return result


async def create_profile(id):
    db = await aiosqlite.connect("databases/users.sqlite")
    cursor = await db.cursor()
    await cursor.execute(f"SELECT id FROM profile WHERE id = {id}")
    result = await cursor.fetchone()
    if not result:
        xp_to_next_level = 50 * 1.1 ** (2 - 1)
        xp_needed = xp_to_next_level - 0
        await cursor.execute(
            f"INSERT INTO profile VALUES ({id}, 1, 0, {int(xp_to_next_level)}, {int(xp_needed)}, 0)"
        )
        await db.commit()
    await db.close()


async def check_level(id):
    db = await aiosqlite.connect("databases/users.sqlite")
    cursor = await db.cursor()
    await cursor.execute(
        f"SELECT level, xp, xp_to_next_level FROM profile WHERE id = {id}"
    )
    result = await cursor.fetchone()
    if result:
        if result[1] >= result[2]:
            new_level = result[0] + 1
            xp_to_next_level = int(result[1] * 1.1 ** (new_level - 1))
            await cursor.execute(
                f"UPDATE profile SET level = {new_level}, xp = 0, xp_to_next_level = {xp_to_next_level}, xp_needed = 0 WHERE id = {id}"
            )
            await db.commit()
            await db.close()
            return True
    else:
        await create_profile(id)

    return False


async def get_level(id):
    db = await aiosqlite.connect("databases/users.sqlite")
    cursor = await db.cursor()
    await cursor.execute(f"SELECT level FROM profile WHERE id = {id}")
    result = await cursor.fetchone()
    if result:
        await db.close()
        return result[0]
    else:
        return 0


async def add_exp(id, xp):
    db = await aiosqlite.connect("databases/users.sqlite")
    cursor = await db.cursor()
    await cursor.execute(
        f"SELECT level, xp, xp_to_next_level, xp_needed FROM profile WHERE id = {id}"
    )
    result = await cursor.fetchone()
    if result:
        current_xp = result[1]
        xp_to_next_level = result[2]
        new_total_xp = current_xp + xp
        new_needed_xp = xp_to_next_level - new_total_xp
        await cursor.execute(
            f"UPDATE profile SET xp = {new_total_xp}, xp_needed = {new_needed_xp} WHERE id = {id}"
        )
        await db.commit()
        await db.close()
        levelled = await check_level(id)
        if levelled:
            return True
        return False
    else:
        await create_profile(id)
