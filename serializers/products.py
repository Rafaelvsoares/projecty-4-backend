from marshmallow import fields
from app import ma
from models.products import ProductModel
from serializers.comments import CommentSchema


class ProductSchema(ma.SQLAlchemyAutoSchema):
    comments = fields.Nested('CommentSchema', many=True)
    class Meta:
        include_fk = True
        model = ProductModel
        load_instance = True