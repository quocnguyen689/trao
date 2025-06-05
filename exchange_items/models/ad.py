from datetime import datetime
from exchange_items import db

class Ad(db.Model):
    __tablename__ = 'ads'
    __table_args__ = {'extend_existing': True}  # Allow table redefinition

    id = db.Column(db.Integer, primary_key=True)
    collection_id = db.Column(db.Integer, db.ForeignKey('collections.id'))
    name = db.Column(db.String, nullable=False)
    type = db.Column(db.String)  # Bán, Cho Tặng, Trao Đổi, ...
    short_description = db.Column(db.String)
    description = db.Column(db.String)
    image_url = db.Column(db.String)
    seller_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    location_distance = db.Column(db.Float)
    status = db.Column(db.String)  # Active, Draft, Expired, ...
    created_date = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    activities = db.relationship('UserActivity', backref='ad', lazy=True)
    offers = db.relationship('Offer', backref='ad', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'collection_id': self.collection_id,
            'name': self.name,
            'type': self.type,
            'short_description': self.short_description,
            'description': self.description,
            'image_url': self.image_url,
            'seller_id': self.seller_id,
            'seller_name': self.seller.name if self.seller else None,
            'location_distance': self.location_distance,
            'status': self.status,
            'created_date': self.created_date.isoformat() if self.created_date else None,
            'total_offers': len(self.offers) if self.offers else 0
        } 