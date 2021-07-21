import requests
from PIL import Image

def slap(target: str, caller: str):
    callar_avatar = Image.open(requests.get(caller, stream=True).raw)
    target_avatar = Image.open(requests.get(target, stream=True).raw)