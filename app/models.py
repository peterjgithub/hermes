from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID 
from sqlalchemy.sql.schema import Column, Index
from sqlalchemy.sql.sqltypes import Integer, Numeric, String, DateTime
import uuid


print("initiate models.py")

print("starting db = SQLAlchemy()")
db = SQLAlchemy()
print("finished db = SQLAlchemy()")

class Quote(db.Model):
    print("initiate class models.Quote(db.Model)")
    __tablename__ = 'quotes'
    print("__tablename__ = 'quotes' ok")
    __table_args__ = (
        Index('quotes_ticker_date_time_idx', "ticker", "date_time", unique=True),
        )
    print("Index('quotes_ticker_date_time_idx', ticker, date_time, unique=True ) ok")

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    ticker = Column(String())
    date_time = Column(DateTime)
    open = Column(Numeric)
    high = Column(Numeric)
    low = Column(Numeric)
    close = Column(Numeric)
    adj_close = Column(Numeric)
    volume = Column(Integer)
    volume_weighted_avg_price = Column(Numeric)
    print("Columns def ok")


    def __init__(self, id, ticker, date_time, open, high, low, close, adj_close, volume, volume_weighted_avg_price):
        print("starting models.py Quote() __init__")
        self.id = id
        self.ticker = ticker
        self.date_time = date_time
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.adj_close = adj_close
        self.volume = volume
        self.volume_weighted_avg_price = volume_weighted_avg_price
        print("finished __init__")

    def __repr__(self):
        print("initiate models.py Quote() __repr__(self)")
        return '<id {}>'.format(self.id)
