from subprocess import call
from os import chdir
from Library.Process import top5

if __name__ == "__main__":
    print("")
    chdir("imdbscraper")
    call(["scrapy", "crawl","imdb","-o","results.csv","log-level=WARNING"])