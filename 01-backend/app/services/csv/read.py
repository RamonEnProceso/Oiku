from pandas import read_csv
from fastapi import UploadFile

def readFile (file:UploadFile):
    df = read_csv(file.file, usecols=range(6))
    df = df.where(df.notna(), None)
    
    return df