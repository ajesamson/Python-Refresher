import uuid
from flask import request
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from models import ItemModel
from sqlalchemy.exc import SQLAlchemyError
from db import db
from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint("Items", __name__, description="Operations on items")


@blp.route("/item/<string:item_id>")
class Item(MethodView):
    @blp.response(200, ItemSchema)
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
    @blp.response(200, ItemSchema)
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
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return items.values()

    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, validated_data):
        item = ItemModel(**validated_data)

        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            print(SQLAlchemyError)
            abort(500, message="An error occurred while inserting the item")

        # if data["store_id"] not in stores:
        #     abort(404, message="Store not found.")

        return item
