from fastapi import FastAPI

app = FastAPI()

TAREFAS = [
    {
        "id": "1",
        "titulo": "Aprender Python",
        "descrição": "Participar do Boot Bootcamp do DevOps Bootcamp",
        "estado": "Finalizado",
    },
    {
        "id": "2",
        "titulo": "Agradecer",
        "descrição": "Agradecer o Cássio e a Amanda",
        "estado": "Finalizado",
    },
    {
        "id": "3",
        "titulo": "Divulgar a comunidade",
        "descrição": "Criar um post no LinkedIn",
        "estado": "Finalizado",
    },
]


@app.get("/tarefas")
def listar():
    return TAREFAS
