#
# Copyright (C) 2021-present by TeamArchMusic@Github, < https://github.com/TeamArchMusic >.
#
# This file is part of < https://github.com/TeamArchMusic/ArchMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamArchMusic/ArchMusicBot/blob/master/LICENSE >
#
# All rights reserved.
#

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from ArchMusic import app
from strings.filters import command
from ArchMusic.core.call import ArchMusic
from ArchMusic.utils.database import set_loop
from ArchMusic.utils.decorators import AdminRightsCheck

# Commands
STOP_COMMAND = get_command("STOP_COMMAND")


@app.on_message(
    filters.command(STOP_COMMAND)
    & filters.group
    & ~BANNED_USERS
)
@app.on_message(
    command(["كافي","ايقاف"])
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    await ArchMusic.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(_["admin_9"].format(message.from_user.mention))
