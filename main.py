import os
import time

from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse

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
    try:
        contoller.press(key)
        contoller.release(key)
    except:
        # fail silently and move on...
        print('[+] Given key not available!', key)


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


def wait_for_user():
    #Default wait value 6 seconds
    wait_duration = os.getenv('WAIT_DURATION', 6)
    time.sleep(int(wait_duration))


@app.post("/type_out/")
async def type_out(selection: str = Form(...)):
    """Types out the given selection.

    Function to handle POST /type_out. Types out the form data.
    Params:
        selection: string to be typed out.
    """

    wait_for_user()
    type_out_text(selection)

    return "Selection typed!"
