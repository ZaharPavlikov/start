from typing import Optional

from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/")
def read_item(name: Optional[str], message: Optional[str]):
    data = f"Hello {name}! {message}!"
    return Response(content=data, media_type="text/plain")
