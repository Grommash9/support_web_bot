import aiohttp
import uvicorn
from fastapi import FastAPI, Form
from starlette.requests import Request
from fastapi.templating import Jinja2Templates

from web_chat import db, config

app = FastAPI()

templates = Jinja2Templates(directory=config.templates_path)


@app.get('/chat/{my_id}/{target_user_id}')
async def hello_world(request: Request, my_id: int, target_user_id: int):
    messages = await db.message.get_correspondence(my_id, target_user_id)
    return templates.TemplateResponse("chat.html", {"messages": messages, "request": request,
                                                    "message_from": my_id, "message_to": target_user_id})


@app.post('/chat/{my_id}/{target_user_id}')
async def hello_world(request: Request, message: str = Form(...), message_from: int = Form(...), message_to: int = Form(...)):
    async with aiohttp.ClientSession() as session:
        async with session.post(f"https://72a9-176-98-90-146.eu.ngrok.io/support_web_bot/new_message/?message={message}&message_from={message_from}&message_to={message_to}") as resp:
            print(resp.status)
            messages = await db.message.get_correspondence(message_from, message_to)
            return templates.TemplateResponse("chat.html", {"messages": messages, "request": request,
                                                            "message_from": message_from, "message_to": message_to})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
