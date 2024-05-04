from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_item(name: str, message: str):
    data = f"Hello {name}! {message}!"
    return Response(content=data, media_type="text/plain")
    return {"name": name, "mes": message}
