from sqlalchemy.exc import IntegrityError

from fastapi import Depends, FastAPI, Request

from read_service import database, models, schemas
from read_service.database import SessionLocal

from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Dependency

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/{npm}", response_model=schemas.MahasiswaResponse)
async def get_mahasiswa(npm: str, req: Request, db: Session = Depends(get_db)):
    mahasiswa_in_db = db.query(models.Mahasiswa).filter(models.Mahasiswa.npm == npm).first()

    return {
        "status": "OK",
        "npm": mahasiswa_in_db.npm,
        "nama": mahasiswa_in_db.nama
    }