url_1="https:www.detail.com/books/pucds/toc.html"
rest_of_url,sep,document=url_1.rpartition('/') #.rpartiton is used to seperate text using / , or anything
print(rest_of_url)
print(sep)
print(document)