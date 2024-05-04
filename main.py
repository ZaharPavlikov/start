from typing import Optional

from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/")
def read_item(name: str=ytyty, message: str=wertyu):
    data = f"Hello {name}! {message}!"
    return Response(content=data, media_type="text/plain")
