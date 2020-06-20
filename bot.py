import discord

from urllib.request import Request, urlopen

import common.config


class Bot:
    def __init__(self, client, admin):
        self.client = client
        self.admin = admin

        # Чтение конфигурационных файлов
        self.config = common.config.init_config()
        self.servers_config = common.config.init_servers_config()
        self.users_config = common.config.init_users_config()

        # Запрос ip
        ip_request = Request("https://api.ipify.org")
        self.ip = urlopen(ip_request).read().decode("utf-8")

    @staticmethod
    async def hello(message):
        await message.channel.send("И тебе привет! 😉")

    @staticmethod
    async def help(message):
        await message.channel.send("!hello - показать приветствие\n"
                                   "!help - показать список команд\n"
                                   "!subscribe - подписаться на уведомления\n"
                                   "!unsubscribe - отписаться от уведомлений")

    async def server_on(self, message):
        if message.author.id == self.admin:
            game = message.content[len("server-on") + 2:]
            await self.client.change_presence(status=discord.Status.online, activity=discord.Game(game))
            await message.channel.send("Ок, теперь сервер включён.")

            # Подготовка упоминания подписчиков
            subscribers = str()
            for user in self.users_config.sections():
                if self.users_config.get(user, "subscribed") == "true":
                    subscribers += "<@" + user + '>'

            # Рассылка уведомлений
            for channel_id in self.servers_config.sections():
                if self.servers_config.get(channel_id, "notifications") == "true":
                    if self.config.get("Main", "show-ip") == "true":
                        await self.client.get_channel(int(channel_id)).send(
                            subscribers + '\n'
                                          "Запущен сервер " + game + '\n'"Подключиться можно по адресу: " + self.ip)
                    else:
                        await self.client.get_channel(int(channel_id)).send(
                            subscribers + '\n' + "Запущен сервер " + game)

    async def server_off(self, message):
        if message.author.id == self.admin:
            await self.client.change_presence(status=discord.Status.online, activity=None)
            await message.channel.send("Ок, теперь сервер выключен.")

    async def notifications_on(self, message):
        if message.author.id == self.admin:
            if not self.servers_config.has_section(str(message.channel.id)):
                self.servers_config.add_section(str(message.channel.id))
            self.servers_config.set(str(message.channel.id), "notifications", "true")
            common.config.write_servers_config(self.servers_config)
            await message.channel.send("Теперь на сервере будут отображаться уведомления")

    async def notifications_off(self, message):
        if message.author.id == self.admin:
            if not self.servers_config.has_section(str(message.channel.id)):
                self.servers_config.add_section(str(message.channel.id))
            self.servers_config.set(str(message.channel.id), "notifications", "false")
            common.config.write_servers_config(self.servers_config)
            await message.channel.send("Уведомления для этого сервера отключены")

    async def subscribe(self, message):
        if not self.users_config.has_section(str(message.author.id)):
            self.users_config.add_section(str(message.author.id))
        self.users_config.set(str(message.author.id), "subscribed", "true")
        common.config.write_users_config(self.users_config)
        await message.channel.send("Вы подписались на уведомления")

    async def unsubscribe(self, message):
        if not self.users_config.has_section(str(message.author.id)):
            self.users_config.add_section(str(message.author.id))
        self.users_config.set(str(message.author.id), "subscribed", "false")
        common.config.write_users_config(self.users_config)
        await message.channel.send("Вы отписались от  уведомлений")
