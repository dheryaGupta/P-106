import csv
import plotly.express as px
import pandas as pd
import numpy as np

def plotFigure(data_path) :
    with open(data_path,encoding="utf-8") as f:
        df = csv.DictReader(f)
        fig = px.scatter(df,x = "Marks In Percentage",y ="Days Present")
        fig.show()


def getDataSource(data_path):
    Marks_percentage=[]
    Days_Present=[]
    with open(data_path,encoding="utf-8") as d:
        sf = csv.DictReader(d)
        for row in sf:
            Marks_percentage.append(float(row["Marks In Percentage"]))
            Days_Present.append(float(row["Days Present"]))
    return {"x":Marks_percentage,"y":Days_Present}


def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation between Temperature v/s Ice ceam sales",correlation[0,1])

def setup():
    data_path="data4.csv"
    datasource=getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()