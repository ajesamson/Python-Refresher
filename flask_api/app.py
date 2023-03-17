from flask import Flask, request

app = Flask(__name__)

stores = [{"name": "Lagos Store", "items": [{"name": "My Item", "price": 15.99}]}]


@app.route("/")
def hello_world():
    return {"message": "Welcome to flask store"}


@app.get("/store")
def get_stores():
    return {"stores": stores}


@app.post("/store")
def create_store():
    data = request.get_json()
    new_store = {"name": data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201


def find_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return None


@app.post("/store/<string:name>/item")
def create_store_item(name):
    data = request.get_json()
    store = find_store(name)
    if store:
        new_item = {"name": data["name"], "price": data["price"]}
        store.items.append(new_item)
        return new_item, 201
    return {"error": "Store not found"}, 404


@app.get("/store/<string:name>")
def get_store(name):
    store = find_store(name)
    if store:
        return store
    return {"error": "Store not found"}, 404


@app.get("/store/<string:name>/item")
def get_store_items(name):
    store = find_store(name)
    if store:
        return {"items": store["items"]}
    return {"error": "Store not found"}, 404
