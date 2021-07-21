import requests
import base64
import os
from PIL import Image

def facepalm(target: str, caller: str, id: int) -> bytes:
    caller_avatar_raw = Image.open(requests.get(caller, stream=True).raw)
    target_avatar_raw = Image.open(requests.get(target, stream=True).raw)
    
    caller_avatar = caller_avatar_raw.resize((64,64), Image.ANTIALIAS)
    target_avatar = target_avatar_raw.resize((64,64), Image.ANTIALIAS)
    
    template = Image.open("templates/facepalm.png")
    
    result = template.copy()
    result.paste(caller_avatar, (152, 60))
    result.save("out/facepalm.png")
    
    encoded = base64.b64encode(open("out/facepalm.png", "rb").read()).decode()
    if os.path.exists("out/facepalm.png"):
         os.remove("demofile.txt")
    return 'data:image/png;base64,{}'.format(encoded)