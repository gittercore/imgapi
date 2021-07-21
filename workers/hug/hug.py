import requests
import base64
import os
from PIL import Image

def hug(target: str, caller: str, id: int):
    try:
        caller_avatar_raw = Image.open(requests.get(caller, stream=True).raw)
        target_avatar_raw = Image.open(requests.get(target, stream=True).raw)
    
        caller_avatar = caller_avatar_raw.resize((64,64), Image.ANTIALIAS)
        target_avatar = target_avatar_raw.resize((64,64), Image.ANTIALIAS)
    
        template = Image.open("templates/hug.png")
    
        result = template.copy()
        result.paste(caller_avatar, (200, 200))
        result.paste(caller_avatar, (380, 60))
        result.save(f"out/hug{id}.png")
    
        encoded = base64.b64encode(open(f"{os.getcwd()}/out/hug{id}.png", "rb").read()).decode()
        result.show()
        # if os.path.exists(f"out/hug{id}.png"):
        #     os.remove(f"out/hug{id}.png")
        return {
            "image": "data:image/png;base64,{}".format(encoded)
        }
    except:
        return {
            "error": "not found"
        }