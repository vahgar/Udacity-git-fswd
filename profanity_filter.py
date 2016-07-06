import urllib

def read_text():
    quotes = open("/Users/Raghav/Desktop/Nanodegree/LocalServer/quotes.txt")
    content = quotes.read()
    print(content)
    quotes.close()
    check(content)
    
     

def check(text):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)
    output = connection.read()
    print(output)
    connection.close()


read_text()


     
