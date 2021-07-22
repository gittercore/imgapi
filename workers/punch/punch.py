import requests
import base64
import os
from PIL import Image

def punch(caller: str, id: int):
    try:
        caller_avatar_raw = Image.open(requests.get(caller, stream=True).raw)
    
        caller_avatar = caller_avatar_raw.resize((100,100), Image.ANTIALIAS)
    
        template = Image.open("templates/punch.png")
    
        result = template.copy()
        result.paste(caller_avatar, (90, 140))
        result.save(f"out/punch{id}.png")
    
        encoded = base64.b64encode(open(f"{os.getcwd()}/out/punch{id}.png", "rb").read()).decode()
        if os.path.exists(f"out/punch{id}.png"):
            os.remove(f"out/punch{id}.png")
        return {
            "image": "data:image/png;base64,{}".format(encoded)
        }
    except:
        return {
            "error": "not found"
        }