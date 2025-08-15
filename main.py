
import argparse

from config import DATAFOLDER
from utils.web_scraper import WebScraper

def main():
    parser = argparse.ArgumentParser(description="A CLI tool to retrieve tender's information in csv.")

    # Optional argument --output
    parser.add_argument("--output", default="tenders.csv", help="Name of output file")
    # Optional argument --max
    parser.add_argument("--max", default="100", help="Maximum number of tenders in output")

    args = parser.parse_args()
    scraper = WebScraper()
    df = scraper.parse_website(int(args.max))
    print(df)
    df.to_csv(DATAFOLDER + args.output, encoding='utf-8')

if __name__ == "__main__":
    main()