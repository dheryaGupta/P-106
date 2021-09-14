import csv
import plotly.express as px
import pandas as pd
import numpy as np

def plotFigure(data_path) :
    with open(data_path,encoding="utf-8") as f:
        df = csv.DictReader(f)
        fig = px.scatter(df,x = "Temperature",y ="Ice-cream Sales( ₹ )")
        fig.show()


def getDataSource(data_path):
    ice_cream_sales=[]
    cold_drink_sales=[]
    with open(data_path,encoding="utf-8") as d:
        sf = csv.DictReader(d)
        for row in sf:
            ice_cream_sales.append(float(row["Temperature"]))
            cold_drink_sales.append(float(row["Cold drink sales( ₹ )"]))
    return {"x":ice_cream_sales,"y":cold_drink_sales}


def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation between Temperature v/s Ice ceam sales",correlation[0,1])

def setup():
    data_path="data1.csv"
    datasource=getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()