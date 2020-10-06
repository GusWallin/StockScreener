from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def dashboard():
    """
    displays the stock screener dashboard
    """
    return {"dashboard": "Home Page"}


@app.post("/stock")
def create_stock():
    """
    Creates a stock and stores it in the database
    """
    return {
        "code": "Success",
        "message": "stock created"
    }

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}
