"""Restart or Terminate the bot from any chat
Available Commands:
.restart
.shutdown"""
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html
from telethon import events
import asyncio
import os
import sys


@borg.on(events.NewMessage(pattern=r"\.restart", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await asyncio.sleep(4)
    await event.edit("Restarting 🔴 ...\n❕Hello @bohthardbohthard , Your Userbot Is Being Restarted.❕")
    await asyncio.sleep(4)
    await event.edit("Restarting ⚫ ...\n❗Hello @bohthardbohthard , Your Userbot Is Being Restarted.❗")
    await asyncio.sleep(4)
    await event.edit("Restarting 🔵 ...\n❕Hello @bohthardbohthard , Your Userbot Is Being Restarted.❕")
    await asyncio.sleep(4)
    await event.edit("Restarting ✅...\n ❗Hello @bohthardbohthard , Your Userbot Is Being Restarted.❗")
    await asyncio.sleep(4)
    await event.edit("♻️**Hello** @bohthardbohthard , **Your Userbot Has Been Restarted.**♻️")
    await borg.disconnect()
    # https://archive.is/im3rt
    os.execl(sys.executable, sys.executable, *sys.argv)
    # You probably don't need it but whatever
    quit()


@borg.on(events.NewMessage(pattern=r"\.shutdown", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await asyncio.sleep(4)
    await event.edit("Windows 98 Shutting Down Safely....")
    await asyncio.sleep(4)
    await event.edit("Your PC Has Been Shutdown, Turn Me On Manually")
    await borg.disconnect()
    
    
    
    borg.on(events.NewMessage(pattern=r"\.repo", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    await asyncio.sleep(4)

    await event.edit("https://www.github.com/ravana69/uniborg")
