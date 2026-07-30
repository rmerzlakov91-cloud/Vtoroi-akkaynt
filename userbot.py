from telethon import TelegramClient, events
import asyncio
import os

# ТВОИ ДАННЫЕ
API_ID = 33694427
API_HASH = 'f819241c056f6827cc0188ff1479a7ce'
BOT_TOKEN = '8912629367:AAGDvBUBFE97vLTPzlXsbmALJHi0u3XUCjs'
BOT_ID = 8912629367  # ID основного бота
GROUP_ID = -1004459421239

# КОД ПОДТВЕРЖДЕНИЯ (если есть)
TG_CODE = os.environ.get('TG_CODE', '')  # Берём код из переменной окружения

# Создаём клиент
client = TelegramClient('session', API_ID, API_HASH)

@client.on(events.NewMessage(pattern=r'🔗 https?://'))
async def handle_link(event):
    url = event.message.text.replace('🔗 ', '')
    await client.send_message(GROUP_ID, url)
    await client.send_message(BOT_ID, "⏳ Ссылка отправлена в группу...")

@client.on(events.NewMessage(chats=GROUP_ID))
async def handle_group_messages(event):
    message = event.message
    if message.video:
        await client.send_file(BOT_ID, message.video, caption="✅ Видео готово!")
    elif message.buttons:
        try:
            for row in message.buttons:
                for button in row:
                    if '1080' in button.text:
                        await button.click()
                        break
        except:
            pass

async def main():
    # Пробуем загрузить сессию
    try:
        # Если есть код, передаём его
        if TG_CODE:
            await client.start(phone='+79643500460', code=TG_CODE)
        else:
            await client.start(phone='+79643500460')
        print('✅ UserBot запущен!')
    except Exception as e:
        print(f'❌ Ошибка: {e}')
        print('Если это первый запуск, добавь переменную TG_CODE с кодом подтверждения.')
    
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
