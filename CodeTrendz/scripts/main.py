# run the scraping and topic modelling scripts from here
from etl import ExtractAndRun

if __name__ == "__main__":
    etl = ExtractAndRun()
    etl.run()
