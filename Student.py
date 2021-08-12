import numpy as np
import csv
import plotly.express as plot

def getdata(datapath):
    ice_cream_sale = []
    temperature = []
    with open(datapath) as file:
        reader = csv.DictReader(file)
        for i in reader:
            temperature.append(float(i["Marks"]))
            ice_cream_sale.append(float(i["Present"]))

    return {"x":temperature,"y":ice_cream_sale} 


def corr(soure):
    correlationindex = np.corrcoef(soure["x"],soure["y"])
    print("correlation between Student marksin persentage and days present =" , correlationindex[0,1]) 

def main() :
    path = ".\data\Student.csv"
    data  = getdata(path)
    corr(data)

main()
