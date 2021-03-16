import os
import requests
from datetime import datetime
import time
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import time



rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%('B', 'A'), timeout = 500)


day = 0
def getprice():
    global day
    L = []
    price_file = open("Price.txt","a")
    latest_block = rpc_connection.getmininginfo()["blocks"]
    data = requests.get("https://www.bitstamp.net/api/ticker/").json()
    day = datetime.utcfromtimestamp(int(data["timestamp"])).strftime('%d')
    if day == "01sdfsdf":
        print(latest_block,data["last"],file=price_file)
    L.append(latest_block)
    L.append(data["last"])
    return L



perc = 0
def Line():
    global perc
    count = 0
    x = open("result.txt","w")
    with open("temp144","r") as f:
        for line in f:
            line = line[:-1]
            value = line.split()

            count += 1
            index = -1
            for i in range(len(value)):
                if value[i] == "0":
                    index = i
                    break
            if index == -1:
                index = count
            #print(round(float(value[index-1]),0))
            j12 = 0
            i12 = 0
            for i in range(1,25):
                if i < 13:
                    j12 += float(value[index-i])
                else:
                    i12 += float(value[index-i])
            if count > 23:
                #print(count,int(j12),int(i12))
                total = i12+j12
                print(int(round(j12/total*100)),file=x)
                #print(int(round(j12/(j12+i12)*100,2)),file=x)  
                perc = int(round(j12/total*100)) 


maanden = [2543,
    5923,
    9389,
    12831,
    16214,
    18450,
    20375,
    21939,
    24098,
    26224,
    28441,
    32489,
    37493,
    43096,
    48297,
    53875,
    58815,
    63561,
    71436,
    77452,
    82997,
    88892,
    94801,
    100409,
    105570,
    111136,
    116038,
    121126,
    127865,
    134121,
    139035,
    143408,
    147565,
    151314,
    155451,
    160036,
    164780,
    169135,
    173804,
    178014,
    182428,
    186963,
    191736,
    196615,
    201310,
    205918,
    210349,
    214562,
    219006,
    223664,
    229007,
    233974,
    238951,
    244159,
    249524,
    255361,
    260988,
    267187,
    272374,
    277995,
    283467,
    288369,
    293482,
    298512,
    303551,
    308671,
    313403,
    318530,
    323268,
    327938,
    332362,
    336860,
    341391,
    345610,
    350161,
    354415,
    358880,
    363262,
    367845,
    372440,
    376909,
    381469,
    386118,
    391181,
    396048,
    400600,
    405178,
    409637,
    414257,
    418722,
    423087,
    427736,
    432283,
    436827,
    441340,
    446032,
    450944,
    455199,
    459831,
    464269,
    469121,
    473592,
    478478,
    482884,
    487739,
    492557,
    496931,
    501960,
    507015,
    511384,
    516039,
    520649,
    525366,
    529966,
    534612,
    539415,
    543834,
    548213,
    552083,
    556458,
    560983,
    565108,
    569658,
    573996,
    578717,
    583236,
    588006,
    592682,
    597317,
    601841,
    606087,
    610690,
    615427,
    619581,
    623836,
    628349,
    632541,
    637090,
    641679,
    646200,
    650731,
    654932,
    659398,
    663912,
    668547,
    672627,999999]

list = []

def price():
    count = 0
    with open("Prices.txt","r") as f:
        for line in f:
            line = line[:-1]
            value = line.split()
            height = value[1]
            if int(height) > maanden[0]:
                maanden.pop(0)
                if value[0][-2:] == "01":
                    if count > 3:
                        print(value[1],value[2])
                    else:
                        count += 1
                

def sync():
    count = 0
    prices = []
    x = open("combi.txt","w")
    with open("Price.txt","r") as f:
        for line in f:
            line = line[:-1]
            value = line.split()

            prices.append(value[1])
    data = requests.get("https://www.bitstamp.net/api/ticker/").json()
    prices.append(float(data["last"]))
    #prices.append(1000)
    with open("result.txt","r") as f:
        for line in f:
            count+=1
            line = line[:-1]
            value = line.split()

            print(count,value[0],prices[0],file=x)
            prices.pop(0)

def combine():
    os.system("cat 144.txt > temp144")

    x = open("144_test.txt","r")
    line = x.read()[:-1]


    x = open("temp144","a")
    
    print(line,file=x)

def print_html():
    x = open("index.html","w")
    print(f"""<!DOCTYPE html>
<html>
<style>

</style>
<body style="background-color: #4b4b4b;">
<h1 style="text-align:center; color: white;">Updated at: {datetime.now().strftime('%Y-%m-%d %H:%M')} </h1>
<p style="text-align:center; color: white;">Current % dot: {perc}%</p>
<img style="display: block; margin-left: auto; margin-right: auto;" src="5000.png" width="1500" height="750" alt="Tuinbonen">
</body>
</html>""",file=x)




def run_all():

    os.system("python3 write.py")
    os.system("python3 ref3.py")
    print("Combining 144.txt and 144_test.txt into temp144...")
    combine()
    print("Calculating vectors...")
    Line()
    print("syncing price and vector into combi.txt...")
    sync()
    print("Plotting combi.txt")
    os.system("gnuplot Graph.gnuplot")
    print_html()
    os.system("git add .")
    os.system("git commit -m 'testing'")
    os.system("git push -u origin main")
run_all()