from db import db

class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primery_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float(orecision=2), unique=False, nullable=False)
    store_id = db.Column(db.Integer, unique=False, nullable=False)
    
