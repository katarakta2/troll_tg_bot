# troll_tg_bot
A telegram bot that will send a specific sticker in response to any message from a specific user. The user ID of the profile in the Telegram is used to send a sticker in response to the user's message.

TOKEN - use token for your bot from official tg bot @@BotFather
TARGET_USER_ID - use the ID of the user you want to link the bot to. You can take it from @giveme_id_bot (send him username)
STICKER_ID - use the ID of the sticker that you want the bot to send automatically. You can take it from @idstickerbot (just send him your sticker)

Bot on Python version 3.12.5
PIP python_telegram_bot version 22.5

In order for the bot to work in a shared chat, it needs to be given the opportunity to send messages in the settings of this shared chat.
In the @BotFather settings, enter the /setprivacy command. Select your bot and select Disable.
