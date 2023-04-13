import uuid
from flask import request
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from db import items
from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint("Items", __name__, description="Operations on items")

@blp.route("/item/<string:item_id>")
class Item(MethodView):
    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, message="Store not found.")
    
    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "Item deleted."}
        except KeyError:
            abort(404, message="Item not found.")
    
    @blp.arguments(ItemUpdateSchema)
    def put(self, validated_data, item_id):
        data = validated_data

        try:
            item = items[item_id]
            item |= data

            return item
        except KeyError:
            abort(404, message="Item not found")


@blp.route("/item")
class ItemList(MethodView):
    def get(self):
        return {"items": list(items.values())}
    
    @blp.arguments(ItemSchema)
    def post(self, validated_data):
        data = validated_data     
        for item in items.values():
            if item["name"] == data["name"] and item["store_id"] == data["store_id"]:
                abort(404, message="Item already exist")

        # if data["store_id"] not in stores:
        #     abort(404, message="Store not found.")

        item_id = uuid.uuid4().hex
        new_item = {**data, "id": item_id}
        items[item_id] = new_item
        return new_item, 201