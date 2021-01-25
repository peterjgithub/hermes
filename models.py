from app import db
from sqlalchemy.dialects.postgresql import UUID 
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, Numeric, Date, String
import uuid

class Quote(db.Model):
    __tablename__ = 'quotes'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    ticker = Column(String())
    date = Column(Date)
    open = Column(Numeric)
    high = Column(Numeric)
    low = Column(Numeric)
    close = Column(Numeric)
    adj_close = Column(Numeric)
    volume = Column(Integer)
    wvolume = Column(Integer)

    def __init__(self, id, ticker, date, open, high, low, close, adj_close, volume, wvolume):
        self.id = id
        self.ticker = ticker
        self.date = date
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.adj_close = adj_close
        self.volume = volume
        self.wvolume = wvolume

    def __repr__(self):
        return '<id {}>'.format(self.id)
