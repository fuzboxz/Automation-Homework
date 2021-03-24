from Library.Process import top5, createCsv
from Library.GoogDrive import UploadToGDrive
from subprocess import call
from os import chdir, remove, path

if __name__ == "__main__":
    csv = "./imdbscraper/results.csv"
    '''
    # Delete parsed results if they exist
    csv = "./imdbscraper/results.csv"
    if path.exists(csv):
        print(csv, "exists - deleting it now")
        remove(csv)
    
    # Run crawler on IMDB Top 250
    print("Running scrapy")
    chdir("imdbscraper")
    call(["scrapy", "crawl", "imdb", "-o", "results.csv", "--loglevel=WARNING"])
    chdir("..")
    print("Crawl complete")
    '''
    # Return the top 5 cast
    topcast = top5(csv)
    print("Top 5 cast: ", topcast)
    filename = "top5.csv"
    createCsv(topcast, filename)
    UploadToGDrive(filename)
