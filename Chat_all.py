from pyrogram import Client
api_id = 27118638
api_hash = "c2af664faebc094058128a8c405b1cae"
bot_token = "6729627691:AAEmf-478dgb44IqDM3EsEtN3A_yTk9ZK6A"

async def get_chat_members(chat_id):
    app = Client("Имя | Бот", api_id=api_id, api_hash=api_hash, bot_token=bot_token, in_memory=True)
    chat_members = []
    await app.start()
    async for member in app.get_chat_members(int(chat_id)):
        chat_members = chat_members + [member.user.id]
    await app.stop()
    return chat_members