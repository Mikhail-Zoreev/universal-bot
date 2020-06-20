import configparser
import os


def init_config():
    config = configparser.ConfigParser()

    if os.path.exists("universal-bot.cfg"):
        config.read("universal-bot.cfg")
    else:
        # Инициализация конфигурации бота
        config.add_section("Main")
        config.set("Main", "show-ip", "true")
        # Запись файла конфигурации
        with open("universal-bot.cfg", 'w') as config_file:
            config.write(config_file)

    return config


# Запись конфигурации бота
def write_config(config):
    with open("universal-bot.cfg", 'w') as config_file:
        config.write(config_file)


# Инициализации конфигурации сервера
def init_servers_config():
    config = configparser.ConfigParser()

    if os.path.exists("configs/servers.cfg"):
        config.read("configs/servers.cfg")
    else:
        # Запись файла конфигурации
        with open("configs/servers.cfg", 'w') as config_file:
            config.write(config_file)

    return config


# Запись конфигурации сервера
def write_servers_config(config):
    with open("configs/servers.cfg", 'w') as config_file:
        config.write(config_file)


# Инициализации конфигурации пользователей
def init_users_config():
    config = configparser.ConfigParser()

    if os.path.exists("configs/users.cfg"):
        config.read("configs/users.cfg")
    else:
        # Запись файла конфигурации
        with open("configs/users.cfg", 'w') as config_file:
            config.write(config_file)

    return config


# Запись конфигурации пользователей
def write_users_config(config):
    with open("configs/users.cfg", 'w') as config_file:
        config.write(config_file)
