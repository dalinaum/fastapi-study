from fastapi import FastAPI, Request


app = FastAPI()


@app.get("/")
async def entry(request: Request, short: bool):
    entry = {"short": short}
    others = request.query_params.items()
    entry.update({"others": others})
    return entry
