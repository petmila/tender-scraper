from fastapi import FastAPI

from utils.web_scraper import WebScraper

app = FastAPI()


@app.get("/tenders")
def get_tenders():
    scraper = WebScraper()
    df = scraper.parse_website(100)
    return {"tenders": df.to_dict(orient="records")}