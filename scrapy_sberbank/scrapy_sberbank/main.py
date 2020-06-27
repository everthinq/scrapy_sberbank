from scrapy.cmdline import execute

def main():
    # execute(['scrapy', 'crawl', 'sberbank', '--nolog'])
    execute(['scrapy', 'crawl', 'sberbank'])

if __name__ == '__main__':
    main()