from datetime import datetime
from exchange_items import db

class Offer(db.Model):
    __tablename__ = 'offers'
    __table_args__ = {'extend_existing': True}  # Allow table redefinition

    id = db.Column(db.Integer, primary_key=True)
    ads_id = db.Column(db.Integer, db.ForeignKey('ads.id'))
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    status = db.Column(db.String)  # New, Accepted, Rejected, Cancelled, ...
    created_date = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'ads_id': self.ads_id,
            'ads_name': self.ad.name if self.ad else None,
            'owner_id': self.owner_id,
            'owner_name': self.owner.name if self.owner else None,
            'status': self.status,
            'created_date': self.created_date.isoformat() if self.created_date else None
        } 