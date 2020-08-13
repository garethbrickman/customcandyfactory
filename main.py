from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

orders = [{"id": "(uuid)1", "status": "stat", "candies": "x", "user":"Joey"}]

def redact_order(data):
    """ only keep non-sensitive fields in a data object """
    new_map = {}
    new_map["status"] = data["status"]
    new_map["candies"] = data["candies"]
    return new_map


@app.get("/orders")
def read_root():
    """ get all orders (redacted if no auth) """
    new_orders = []
    for item in orders:
        new_map = redact_order(item)
        new_orders.append(new_map)
    return new_orders
@app.get("/orders/candyman")
def read_root():
    """ get all orders (redacted if no auth) """
    return orders


class Order(BaseModel):
    id: str = None
    status: str = None
    candies: str = None
    user: str = None
@app.post("/orders")
def read_root(order: Order):
    """ make a new order """
    orders.append(dict(order))
    return order


@app.get("/orders/{order_id}")
def read_item(order_id):
    """ get an order (redacted if no auth)"""
    by_id = [redact_order(x) for x in orders if x["id"] == order_id]
    if len(by_id) == 1:
        return by_id[0]
    return by_id
@app.get("/orders/{order_id}/candyman")
def read_item(order_id):
    """ get an order (redacted if no auth)"""
    by_id = [x for x in orders if x["id"] == order_id]
    if len(by_id) == 1:
        return by_id[0]
    return by_id


@app.put("/orders/{order_id}")
def read_root(order_id, order: Order):
    """ change an order """
    for x in orders:
        if x["id"] == order_id:
            for k,v in order:
                x[k] = v
    return order
