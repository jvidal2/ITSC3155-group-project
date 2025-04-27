import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from routers import index as indexRoute
from models import model_loader
from dependencies.config import conf
from sqlalchemy.orm import Session
from dependencies.database import get_db


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_loader.index()
indexRoute.load_routes(app)


if __name__ == "__main__":
    uvicorn.run(app, host=conf.app_host, port=conf.app_port)

@app.get("/third_party_delivery_service/{status}", response_model=model_loader.third_party_delivery_service, tags=["Delivery Status"])
def read_one(status: str, db: Session = Depends(get_db)):
    service = model_loader.third_party_delivery_service.read_one(db, status=status)
    if service is None:
        raise HTTPException(status_code=404, detail="Delivery status not found")
    return service