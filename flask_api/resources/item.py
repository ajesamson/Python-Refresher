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
        item = ItemModel.query.get_or_404(item_id)
        return item

    def delete(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Item deleted."}

    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    def put(self, validated_data, item_id):
        item_data = validated_data

        item = ItemModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = ItemModel(id=item_id, **item_data)

        db.session.add(item)
        db.session.commit()

        return item


@blp.route("/item")
class ItemList(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        items = ItemModel.query.all()
        return items

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
