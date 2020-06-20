import discord
from bot import Bot
from common.argparser import init_arg_parser

arg_parser = init_arg_parser()
args = arg_parser.parse_args()

client = discord.Client()
bot = Bot(client, args.admin)


# Обработка сообщений
@client.event
async def on_message(message):
    # Игнорирование сообщений от себя
    if message.author.id == client.user.id:
        return

    # Приветствие
    if message.content.startswith("!hello"):
        await bot.hello(message)
        return

    # Подсказка
    if message.content.startswith("!help"):
        await bot.help(message)
        return

    # Включить сервер
    if message.content.startswith("!server-on"):
        await bot.server_on(message)
        return

    # Выключить сервер
    if message.content.startswith("!server-off"):
        await bot.server_off(message)
        return

    # Включить уведомления на сервере
    if message.content.startswith("!notifications-on"):
        await bot.notifications_on(message)
        return

    # Выключить уведомления на сервере
    if message.content.startswith("!notifications-off"):
        await bot.notifications_off(message)
        return

    # Подписаться на уведомления
    if message.content.startswith("!subscribe"):
        await bot.subscribe(message)
        return

    # Отписаться от уведомлений
    if message.content.startswith("!unsubscribe"):
        await bot.unsubscribe(message)
        return

client.run(args.token)
