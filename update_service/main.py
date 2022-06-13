from sqlalchemy.exc import IntegrityError

from fastapi import Depends, FastAPI, Request

from update_service import database, models, schemas
from update_service.database import SessionLocal

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

@app.post("/update", response_model=schemas.BaseResponse)
async def create_or_update_mahasiswa(mahasiswa: schemas.Mahasiswa, req: Request, db: Session = Depends(get_db)):
    if not req.headers['Content-Type'] == 'application/json':
        return {"message": "Content-Type must be application/json"}
    params = await req.json()
    mahasiswa = schemas.Mahasiswa(** params)
    mahasiswa_in_db = db.query(models.Mahasiswa).filter(models.Mahasiswa.npm == mahasiswa.npm).first()

    if mahasiswa_in_db:
        mahasiswa_in_db.nama = mahasiswa.nama
        db.commit()
    else:
        mahasiswa_in_db = models.Mahasiswa(
            npm = mahasiswa.npm,
            nama = mahasiswa.nama
        )
        db.add(mahasiswa_in_db)
        db.commit() 
        db.refresh()

    return {
        "status": "OK",
    }