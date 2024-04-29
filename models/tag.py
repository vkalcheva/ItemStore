from db import db


class TagModel(db.Model):
    __tablename__ = "tags"

    id = db.Column(db.Intiger, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    store_id = db.Column(db.Intiger, db.ForeignKey("store.id"), nullable=False)

    store = db.relationship("StoreModel", back_populates="tags")