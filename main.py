from crawlers.mozzartjobs import MozzartCrawler

def main():
    mozzartcrawler = MozzartCrawler()
    mozzartjobs = mozzartcrawler.find_jobs()
    print(mozzartjobs)

if __name__ == "__main__":
    main()