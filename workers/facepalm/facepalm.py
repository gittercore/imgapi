import requests
from PIL import Image

def facepalm(target: str, caller: str) -> str:
    caller_avatar_raw = Image.open(requests.get(caller, stream=True).raw)
    target_avatar_raw = Image.open(requests.get(target, stream=True).raw)
    
    caller_avatar = caller_avatar_raw.resize((64,64), Image.ANTIALIAS)
    target_avatar = target_avatar_raw.resize((64,64), Image.ANTIALIAS)
    
    template = Image.open("templates/facepalm.png")
    
    result = template.copy()
    result.paste(caller_avatar, (152, 60))
    result.show()