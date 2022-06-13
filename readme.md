## How to run
1. Jalankan perintah `pip install -r requirements.txt` untuk menginstall _dependencies_.
2. Jalankan perintah `uvicorn update_service.main:app --port 8001 --reload` untuk menjalankan service update.
3. Jalankan perintah `uvicorn read_service.main:app --port 8002 --reload` untuk menjalankan service read.