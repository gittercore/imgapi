# ImageAPI
Image Modification API for discord avatars.

# Documentation
Documentation can be found in the [`documentation`](https://github.com/gittercore/imgapi/blob/main/documentation) directory.

# Getting started
## You will need
- 2 Discord avatar links
## Request
If I want a punch, I would send a request to `/image/punch`  
The request body would be as follows:
```json
{
    "avatarURL": [
            "https://cdn.discordapp.com/avatars/665488298533322762/fbcfbd26a8b93472763e3fd3ca0e014f.webp?size=256"
        ]
}
```
The response will be a `data` url, which when decoded will be
![idk](https://cdn.discordapp.com/attachments/834456504903663626/867358176243351592/unknown.png)

# Support
Support for use of the API can be found at the discord server [`discord.gg/n7EQSvGPax`](https://discord.gg/n7EQSvGPax)

## Disclaimer
We will not provide support for self hosting of the API