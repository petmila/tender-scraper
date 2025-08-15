from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/tenders")
def get_tenders():
    return FileResponse("data/tenders.csv",
                        filename="data/tenders.csv",
                        media_type="application/octet-stream")