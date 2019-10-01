from fuzzywuzzy import process as process_
from commandHandler import command_list
import messageSender
import importlib
import os


def load_modules():
    files = os.listdir("/root/bot/commands")
    modules = filter(lambda x: x.endswith('.py'), files)
    for m in modules:
        importlib.import_module("commands." + m[0:-3])


def get_answer(body, attachment=''):
    if len(body) > 3:
        for c in command_list:
            string = process_.extract(query=body, choices=c.keys)[0]
            if int(string[1]) > 75:  # Порог схожести команды 100 - полное совпадение / 0 - совершенно не совпадает
                message, attachment = c.process()
                return message, attachment
    return "", ""


def create_answer(peer_id, message, attachment=""):
    load_modules()
    message, attachment = get_answer(message, attachment)
    if message != "" or attachment != "":
        messageSender.send_message(peer_id, message, attachment)
