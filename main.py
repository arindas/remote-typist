from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
import time
from pynput.keyboard import Controller
from pynput.keyboard import Key

contoller = Controller()

templates = Jinja2Templates(directory="templates")

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def index_html(request: Request):
    return templates.TemplateResponse("index.html",
                                      {'request': request})


def type_key(key):
    contoller.press(key)
    contoller.release(key)


def map_char_to_key(char, prev=None):
    if char == '\r':
        return

    return Key.enter \
        if prev == '\r' and char == '\n' else char


def type_out_text(text: str):
    prev = None

    for char in text:
        key = map_char_to_key(char, prev)

        if key is not None:
            type_key(key)

        prev = char


@app.post("/type_out/")
async def type_out(selection: str = Form(...)):
    """Types out the given selection.

    Function to handle POST /type_out. Types out the form data.
    Params:
        selection: string to be typed out.
    """
    time.sleep(6)
    # You got 6 seconds to change your active form / window where typing is to be done
    type_out_text(selection)

    return "Selection printed!"
