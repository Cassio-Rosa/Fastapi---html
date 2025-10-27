# pip install fastapi uvicorn jinja2 python-multipart
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Lista de alunos")

#Definir a pasta onde está os html
templates = Jinja2Templates(directory="templates")

#Definir a pasta onde está os arquivos estaticos (CSS, Imagens, e JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

alunos = [
    {"nome": "Murilo", "nota": 9.5},
    {"nome": "Joanna", "nota": 5.5},
    {"nome": "Cassio", "nota": 10.0}

]

#Rota principal 
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "listar_alunos": alunos}
    )

#Tela de cadastro
@app.get("/cadastro", response_class=HTMLResponse)
def tela_cadastro(request: Request):
    return templates.TemplateResponse(
        "cadastro.html",
        {"request": request}
    )

@app.post("/cadastro")
def salvar_aluno(nome:str = Form(...), nota: float = Form(...)):
    alunos.append({"nome": nome, "nota": nota})
    return RedirectResponse(url="/", status_code=303)