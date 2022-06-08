from fastapi import FastAPI, Query
from pydantic import Required


app = FastAPI()


# @app.get("/items/")
# async def read_items(
#     q: str | None = Query(default=..., min_length=3,
#                           max_length=50, regex="^fixedquery$")
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# @app.get("/items/")
# async def read_items(
#     q: str | None = Query(default=Required, min_length=3,
#                           max_length=50, regex="^fixedquery$")
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# @app.get("/items/")
# async def read_items(q: list[str] | None = Query(default=["foo", "bar"])):
#     query_items = {"q": q}
#     return query_items


@app.get("/items/")
async def read_items(
    q: str | None = Query(
        default=None,
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        alias="item-query",
        deprecated=True,
    ),
    hidden_query: str | None = Query(
        default=None,
        include_in_schema=False,
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    if hidden_query:
        results.update({"hidden_query": hidden_query})
    else:
        results.update({"hidden_query": "Not found"})
    return results
