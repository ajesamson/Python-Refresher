import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores

blp = Blueprint("stores", __name__, description="Operations on stores")


@blp.route("/store/<string:store_id>")
class Store(MethodView):
    def get(self, store_id):
        try:
            return stores[store_id]
        except KeyError:
            abort(404, message="Store not found.")

    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"message": "Store deleted."}
        except KeyError:
            abort(404, message="Store not found.")


@blp.route("/store")
class StoreList(MethodView):
    def get(self):
        return {"stores": list(stores.values())}

    def post(self):
        data = request.get_json()
        no_name = "name" not in data
        if no_name:
            abort(
                400,
                message="Bad request. Ensure 'name' is included in the JSON payload.",
            )

        for store in stores.values():
            if store["name"] == data["name"]:
                abort(404, message="Store already exist")

        store_id = uuid.uuid4().hex
        store = {**data, "id": store_id}
        stores[store_id] = store
        return store, 201
