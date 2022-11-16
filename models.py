from datetime import datetime
from config import db, ma
from sqlalchemy import Column, Integer, String

class Widget(db.Model):
    __tablename__ = "widgets"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    number_of_parts = db.Column(db.Integer)
    created_date = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    updated_date = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

def __init__(self, **kwargs):
    super(Widget, self).__init__(**kwargs)

# def __init__(self, name, number_of_parts):
#    self.name = name
#    self.number_of_parts = number_of_parts
   # self.created_date = created_date
   # self.updated_date = updated_date

# db.create_all()

# class Widget(Base):
#     __tablename__ = "widgets"
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     number_of_parts = Column(Integer)
#     created_date = Column(
#         DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
#     )
#     updated_date = Column(
#         DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
#     )
    

class WidgetSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Widget
        load_instance = True
        sqla_session = db.session

widget_schema = WidgetSchema()
widgets_schema = WidgetSchema(many=True)