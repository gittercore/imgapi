# Punch
Endpoint - `/image/punch`  

Any requests to the Endpoint must have this request body
```json
{
    "avatarURL": [
        "avatar link"
    ]
}
```
Response will be along the lines of 
```json
{
    "image": "data:image/png;base64,iVBORw0KGgoAAAANSUh..."
}
```
You will need to decode the data url.

All requests must be json, (`application/json`)