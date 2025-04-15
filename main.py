from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Подключаем HTML и статику
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/pet-status")
async def get_pet_status(user_id: int):
    # Тут пока заглушка
    return {
        "name": "Котик",
        "hungry": False,
        "clean": True,
        "next_turn_in": "23:59:59"
    }
