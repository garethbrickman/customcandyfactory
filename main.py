from fastapi import FastAPI

app = FastAPI()


@app.get("/orders")
def read_root():
    """ get all orders (redacted if no auth) """
    return {"Hello": "World"}

@app.post("/orders")
def read_root():
    """ make a new order """
    return {"Hello": "World"}

@app.get("/orders/{order_id}")
def read_item(order_id):
    """ get an order (redacted if no auth)"""
    return {"order_id": order_id}

@app.put("/orders/{order_id}")
def read_root(order_id):
    """ change an order """
    return {"Hello": "World"}

