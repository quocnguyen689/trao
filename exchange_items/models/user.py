from datetime import datetime
from exchange_items import db

class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}  # Allow table redefinition

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    type = db.Column(db.String)  # Seller, Buyer
    created_date = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    ads = db.relationship('Ad', backref='seller', lazy=True)
    activities = db.relationship('UserActivity', backref='user', lazy=True)
    offers = db.relationship('Offer', backref='owner', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'created_date': self.created_date.isoformat() if self.created_date else None,
            'total_ads': len(self.ads) if self.ads else 0,
            'total_activities': len(self.activities) if self.activities else 0,
            'total_offers': len(self.offers) if self.offers else 0
        } 