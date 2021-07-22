import requests
import base64
import os
from PIL import Image

def facepalm(caller: str, id: int):
    try:
        caller_avatar_raw = Image.open(requests.get(caller, stream=True).raw)
    
        caller_avatar = caller_avatar_raw.resize((64,64), Image.ANTIALIAS)
    
        template = Image.open("templates/facepalm.png")
    
        result = template.copy()
        result.paste(caller_avatar, (152, 60))
        result.save(f"out/facepalm{id}.png")
    
        encoded = base64.b64encode(open(f"{os.getcwd()}/out/facepalm{id}.png", "rb").read()).decode()
        if os.path.exists(f"out/facepalm{id}.png"):
            os.remove(f"out/facepalm{id}.png")
        return {
            "image": "data:image/png;base64,{}".format(encoded)
        }
    except:
        return {
            "error": "not found"
        }