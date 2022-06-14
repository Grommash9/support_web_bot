import uvicorn
from fastapi import FastAPI
from fastapi import Request
from fastapi.templating import Jinja2Templates

from web_chat import db, config

app = FastAPI()

templates = Jinja2Templates(directory=config.templates_path)


@app.get('/chat/{my_id}/{target_user_id}')
async def hello_world(request: Request, my_id: int, target_user_id: int):
    messages = await db.message.get_correspondence(my_id, target_user_id)
    return templates.TemplateResponse("chat.html", {"messages": messages, "request": request})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
