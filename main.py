from fastapi import FastAPI, HTTPException

app = FastAPI()


def calcul_cout(
    kwh: float, prix_kwh: float = 0.25, heures_creuses: bool = False
) -> float:
    if kwh < 0:
        raise ValueError("L'énergie doit être positive")
    if heures_creuses:
        prix_kwh *= 0.8
    return round(kwh * prix_kwh, 2)


@app.get("/")
def accueil():
    return {"message": "Hello Qevan le boss"}


@app.get("/cout")
def cout(kwh: float, prix_kwh: float = 0.25, heures_creuses: bool = False):
    try:
        return {"kwh": kwh, "cout_eur": calcul_cout(kwh, prix_kwh, heures_creuses)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
