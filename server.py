# main.py
from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()




@app.get("/finance/{ticker}/{exchange}")
async def read_user_item(ticker: str, exchange: str):
    url = f'https://www.google.com/finance/quote/{ticker}:{exchange}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    classl = "YMlKec fxKbKc"
    price = float(soup.find(class_=classl).text.strip()[1:].replace(",",""))
    return {"nav":price}
