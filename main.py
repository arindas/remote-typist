from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse

templates = Jinja2Templates(directory="templates")

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def index_html(request: Request):
    return templates.TemplateResponse("index.html",
                                      {'request': request})


@app.post("/type_out/")
async def type_out(selection: str = Form(...)):
    """Types out the given selection.

    Function to handle POST /type_out. Types out the form data.
    Params:
        selection: string to be typed out.
    """
    print(selection)

    return "Selection printed!"
