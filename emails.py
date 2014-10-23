import scrapy
import urlparse
import csv


class Emails(scrapy.Item):
	email = scrapy.Field()

class emailscrapper(scrapy.Spider):
	name = "emailscrap"
	f = open("urls.txt")
	#allowed_urls =  [url.strip() for url in f.readlines()] 
        start_urls =  [url.strip() for url in f.readlines()]
        f.close()


	def parse(self, response):
		email_list = []
		email_links = response.xpath("//a[starts-with(@href, 'mailto')]/text()").extract()
		if (email_links <= 1):
			return
                if (email_links > 1):
			for address in email_links:
				email_list.append(address)


	        myfile = open('final.csv', 'a')
	        wr = csv.writer(myfile, quoting = csv.QUOTE_ALL)
	        wr.writerow(email_list)	
		
