# Stable diffusion deepnude

This approach uses stable diffusion inpainting technology that assumes to be better than the previous original idea implementation

For now it needs you to:

1. run local Automatic1111 webui with the `--nowebui` flag
2. install python deps
3. download "cm.lib" from any source that provides deepnude weights (google it) and to place the file inside the "checkpoints" folder in the repo root
4. create your telegram bot with @botfather and to add its token to your env vars like `export API_TOKEN=<insert-token-here>`
5. run the bot like `python3 bot.py`

And with that -- it just finally works mf!
