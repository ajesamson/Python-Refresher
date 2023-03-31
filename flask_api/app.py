import uuid
from flask import Flask, request
from db import items, stores

app = Flask(__name__)

# stores = [{"name": "Lagos Store", "items": [{"name": "My Item", "price": 15.99}]}]


@app.route("/")
def hello_world():
    return {"message": "Welcome to flask store"}


@app.get("/store")
def get_stores():
    return {"stores": list(stores.values())}


@app.get("/items")
def get_all_items():
    return {"items": list(items.values())}


@app.post("/store")
def create_store():
    data = request.get_json()
    store_id = uuid.uuid4().hex
    store = {**data, "id": store_id}
    stores[store_id] = store
    return store, 201


def find_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return None


@app.post("/item")
def create_store_item(name):
    data = request.get_json()
    if data["store_id"] not in stores:
        return {"error": "Store not found"}, 404

    item_id = uuid.uuid4.hex
    new_item = {**data, "id": item_id}
    items[item_id] = new_item
    return new_item, 201


@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        return {"error": "Store not found"}, 404


@app.get("/<string:name>/item_id")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        return {"error": "Store not found"}, 404
