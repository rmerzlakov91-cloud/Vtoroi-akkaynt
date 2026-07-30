from telethon import TelegramClient, events
import asyncio

# ТВОИ ДАННЫЕ С my.telegram.org
API_ID = 33694427
API_HASH = 'f819241c056f6827cc0188ff1479a7ce'

# ТОКЕН ОСНОВНОГО БОТА
BOT_TOKEN = '8912629367:AAGDvBUBFE97vLTPzlXsbmALJHi0u3XUCjs'
BOT_ID = 8912629367  # ID основного бота

# ID ГРУППЫ С TopSaverBot
GROUP_ID = -1004459421239

# Создаём клиент для твоего второго аккаунта
client = TelegramClient('session_name', API_ID, API_HASH)

@client.on(events.NewMessage(pattern=r'🔗 https?://'))
async def handle_link(event):
    """Когда приходит ссылка от основного бота"""
    url = event.message.text.replace('🔗 ', '')
    
    # Отправляем ссылку в группу с TopSaverBot
    await client.send_message(GROUP_ID, url)
    
    # Отвечаем основному боту, что ссылка отправлена
    await client.send_message(BOT_ID, "⏳ Ссылка отправлена в группу...")

@client.on(events.NewMessage(chats=GROUP_ID))
async def handle_group_messages(event):
    """Обрабатываем сообщения от TopSaverBot в группе"""
    message = event.message
    
    # Если пришло видео
    if message.video:
        # Отправляем видео основному боту
        await client.send_file(BOT_ID, message.video, caption="✅ Видео готово!")
    
    # Если пришла кнопка с выбором качества
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
    # Вход под номером +79643500460
    await client.start(phone='+79643500460')
    print('✅ UserBot запущен на втором аккаунте!')
    print('Ожидаю ссылки от основного бота...')
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
