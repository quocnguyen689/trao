from datetime import datetime
from exchange_items import db

class Collection(db.Model):
    __tablename__ = 'collections'
    __table_args__ = {'extend_existing': True}  # Allow table redefinition

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    icon_url = db.Column(db.String)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship
    ads = db.relationship('Ad', backref='collection', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'icon_url': self.icon_url,
            'created_date': self.created_date.isoformat() if self.created_date else None,
            'total_number_ads': 11111
        } 