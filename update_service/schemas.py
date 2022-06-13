from email import message
from pydantic import BaseModel

class Mahasiswa(BaseModel):
    npm: str
    nama: str

class BaseResponse(BaseModel):
    status: str