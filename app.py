from fastapi import FastAPI
from varejao.views import router as varejao_router
from macapa.views import router as macapa_router
from auth.views import router as auth_router

app = FastAPI()

app.include_router(varejao_router)
app.include_router(macapa_router)
app.include_router(auth_router)

@app.get("/")
def read_root():
    return {"status_code": 200}