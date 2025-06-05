from datetime import datetime
from exchange_items import db

class UserActivity(db.Model):
    __tablename__ = 'user_activities'
    __table_args__ = {'extend_existing': True}  # Allow table redefinition

    id = db.Column(db.Integer, primary_key=True)
    ads_id = db.Column(db.Integer, db.ForeignKey('ads.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    action_type = db.Column(db.String)  # Thích ads, Xem ads, ...
    created_date = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'ads_id': self.ads_id,
            'ads_name': self.ad.name if self.ad else None,
            'user_id': self.user_id,
            'user_name': self.user.name if self.user else None,
            'action_type': self.action_type,
            'created_date': self.created_date.isoformat() if self.created_date else None
        } 