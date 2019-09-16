import re
import urllib.request
import subprocess

arrayofStocks=["FB","AMZN","GOOG","AAPL","TSLA"]
###stock=input("enter stock: ")
##url="https://finance.yahoo.com/quote/"+stock+"?p="+stock
###print(url)
##data=urllib.request.urlopen(url).read()
##data1=data.decode("UTF-8")
###print(data1)
##m=re.search("regularMarketPrice",data1)
###print(m)
##start=m.start()
##end= start+40
##newString=data1[start:end]
###print(newString)
##n=re.findall("\d+.+\d",newString)
##str1=''.join(n)
##print(stock + " are valoarea " + str1)

def timp():
    cmd="date"
    ret=subprocess.check_output(cmd)
    return ret.decode("utf-8")

def obtainStock(stock):
    url="https://finance.yahoo.com/quote/"+stock+"?p="+stock
    data=urllib.request.urlopen(url).read()
    data1=data.decode("UTF-8")
    m=re.search("regularMarketPrice",data1)
    start=m.start()
    end= start+40
    newString=data1[start:end]
    n=re.findall("\d+.+\d",newString)
    str1=''.join(n)
    print(stock + " are valoarea " + str1 + "$ la " + str(timp()) )

for element in arrayofStocks:
    obtainStock(element)

