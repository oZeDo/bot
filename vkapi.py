import vk
import random
from settings import token

session = vk.Session(access_token=token)
api = vk.API(session, v=5.101)


def send_message(peer_id, message, attachment):
    api.messages.send(peer_id=peer_id, message=message, attachment=attachment, random_id=random.randint(1, 10**10))
