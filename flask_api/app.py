import uuid
from flask import Flask, request
from flask_smorest import abort
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
    no_name = "name" not in data
    if no_name:
        abort(
            400, message="Bad request. Ensure 'name' is included in the JSON payload."
        )

    for store in stores.values():
        if store["name"] == data["name"]:
            abort(404, message="Store already exist")

    store_id = uuid.uuid4().hex
    store = {**data, "id": store_id}
    stores[store_id] = store
    return store, 201


@app.post("/item")
def create_store_item():
    data = request.get_json()
    no_price = "price" not in data
    no_store_id = "store_id" not in data
    no_name = "name" not in data
    if no_price or no_store_id or no_name:
        abort(
            400,
            message="Bad request. Ensure 'price', 'store_id', and 'name' are included in the JSON payload.",
        )

    for item in items.values():
        if item["name"] == data["name"] and item["store_id"] == data["store_id"]:
            abort(404, message="Item already exist")

    if data["store_id"] not in stores:
        abort(404, message="Store not found.")

    item_id = uuid.uuid4().hex
    new_item = {**data, "id": item_id}
    items[item_id] = new_item
    return new_item, 201


@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        abort(404, message="Store not found.")



@app.delete("/store/<string:store_id>")
def delete_store(store_id):
    try:
        del stores[store_id]
        return {"message": "Item deleted."}
    except KeyError:
        abort(404, message="Item not found.")

@app.get("/<string:name>/item_id")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404, message="Store not found.")


@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}


@app.delete("/item/<string:item_id>")
def delete_item(item_id):
    try:
        del items[item_id]
        return {"message": "Item deleted."}
    except KeyError:
        abort(404, message="Item not found.")


@app.put("item/<string:item_id>")
def update_item(item_id):
    data = request.get_json()
    if "price" not in data or "name" not in data:
        abort(
            400,
            message="Bad request. Ensure 'price' and 'name' are included in the JSON payload.",
        )

    try:
        item = items[item_id]
        item |= data

        return item
    except KeyError:
        abort(404, message="Item not found")
