from telethon import events

from userbot import bot, devilversion

PM_IMG = "https://telegra.ph/file/b659ddbb131090c775e3f.jpg"
pm_caption = "➥ **ASSISTANT IS:** `ONLINE`\n\n"
pm_caption += "➥ **SYSTEMS STATS**\n"
pm_caption += "➥ **Telethon Version:** `1.15.0` \n"
pm_caption += "➥ **Python:** `3.7.4` \n"
pm_caption += "➥ **Database Status:**  `Functional`\n"
pm_caption += "➥ **Current Branch** : `main`\n"
pm_caption += f"➥ **Version** : `{devilversion}`\n"
pm_caption += f"➥ **My Boss** : \n"
pm_caption += "➥ **Heroku Database** : `AWS - Working Properly`\n\n"
pm_caption += "➥ **License** : [GNU General Public License v3.0](github.com/ahirearyan2/HyperUserBot-X/blob/main/LICENSE)\n"
pm_caption += "➥ **Copyright** : By [TEAM DEVIL BOT](https://github.com/sameerpanthi/D3VIL&BOT)\n"
pm_caption += "[Assistant By D3VIL BOT ]"

# only Owner Can Use it
@tgbot.on(events.NewMessage(pattern="^/alive", func=lambda e: e.sender_id == bot.uid))
async def jarvis(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
