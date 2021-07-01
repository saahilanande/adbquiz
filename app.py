import re
from flask import Flask, render_template, request,redirect,url_for

results=[]

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def home():
    alice()
    return render_template('home.html')





def alice():
    stop = addstopwords()
    count = 0
    foundcount = 0
    stopcount = 0
    file = open(r'DonQuijote.txt', encoding="utf-8")
    lines = file.readlines()
    for data in lines:
        data = data.lower()
        data = data.replace(".","")
        data = data.replace(",","")
        data = data.replace(":","")
        data = data.replace("\"","")
        data = data.replace("!","")
        data = data.replace("'","")
        data = data.replace("â€˜","")
        data = data.replace("*","")
        data = data.replace("|","")
        data = data.replace("#","")
        data = data.replace("'","")
        data = data.replace("’","")
        data = data.replace("?","")
        data = data.replace('“',"")
        data = data.replace('”',"")
        data = data.replace('_',"")
        '''for x in stop:
            data = data.replace("\\b"+x+"\\b","")'''
        
        for x in stop:
            index = str(data).find(""+x+"")
            if index != -1:
                stopcount = stopcount +1



        '''
        normalstring = str(data)
        index = normalstring.find("was")
        count = count + 1
        if index != -1:
            item1 = "FOUND IN FILE: AliceCleaner.TXT"
            item2 = "LINE NO:"+str(count)+""
            item3 = "CHARACTER NO IN LINE:"+str(index)+""
            item4 = normalstring
            results.extend([item1,item2,item3,item4])
            foundcount = foundcount + 1

    if foundcount == 0:
        fail = 'NO SEARCH FOUND IN AliceCleaner.txt'
        results.append(fail)
        return results
    else:
        return results'''
    print("Total stop word count:"+str(stopcount)+"")
    if stopcount == 0:
        print ("no match found")


def addstopwords():
    stopfile = open('stopwords.txt', encoding="utf-8")
    read = stopfile.read()
    morestop=[]
    for rem in read.lower().split():
        rem = rem.replace("\"","")
        morestop.append(rem)
    return morestop




if __name__ == '__main__':
    app.run(debug =True,host='0.0.0.0')