from fastapi import FastAPI
import json

words = {}
with open("./populars.json", "r") as file:
     raw_words = json.loads(file.read())

for index,item in enumerate(raw_words):
     words[item['word']]=item


app = FastAPI()


@app.get("/")
async def read_root():
    return {"dictionary": "orca"}

@app.get("/v1/dict/{query}")
async def read_path(query):
    try:
        target = words[query]
        return {"word":query,"data":target}
    except:
        return {"word": query,"data":None}