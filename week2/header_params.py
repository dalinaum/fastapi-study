from fastapi import FastAPI, Header


app = FastAPI()


# @app.get("/items/")
# async def read_items(user_agent: str | None = Header(default=None)):
#     return {"User-Agent": user_agent}


# @app.get("/items/")
# async def read_items(
#     strange_header: str | None = Header(default=None, convert_underscores=False)
# ):
#     return {"strange_header": strange_header}


@app.get("/items/")
async def read_items(
    x_token: list[str] | None = Header(default=None, convert_underscores=False)
):
    return {"X Token values": x_token}