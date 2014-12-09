from lxml import html
import requests

inputfile = open('url3.otd', 'r')
urls = inputfile.readlines()

import csv
with open('scrapefromurls.csv', 'w') as fp:

    a = csv.writer(fp, delimiter=',')
    a.writerow(["Title","Description","Body"])
    
    for url in urls:
        
        print '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - '
        
        page = requests.get(url)
        tree = html.fromstring(page.text)
        
        #This will get the post title
        posttitle = tree.xpath('//h1[@id="post-title"]/text()')
      
        #This will get the post description
        postdesc = tree.xpath('//p[@class="description"]/b/text()')
       
        postdescencoded = []
        for desc in postdesc:
            postdescencoded.append(desc.encode('utf-8').strip())

        # OK but needs to improve:
        postbody = tree.xpath('//span[@class="buzz_superlist_number_inline"]/text() | //h2/text() | //p/text()')
        
        postbodyencoded = []
        for content in postbody:
            postbodyencoded.append(content.encode('utf-8').strip())
        
        a.writerow([posttitle[0].encode('utf-8'),postdescencoded,postbodyencoded])

