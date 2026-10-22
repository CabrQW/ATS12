from fastapi import FastAPI

app = FastAPI(title="API ATS12")

@app.get("/")
def inicio():
    return {"mensagem": "API ATS12 funcionando!"}

@app.get("/somar/{a}/{b}")
def somar(a: int, b: int):
    return {"resultado": a + b}

@app.get("/multiplicar/{a}/{b}")
def multiplicar(a: int, b: int):
    return {"resultado": a * b}