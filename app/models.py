from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID 
from sqlalchemy.sql.schema import Column, Index
from sqlalchemy.sql.sqltypes import Integer, Numeric, String, DateTime
import uuid
import sys


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

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
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

def get_aapl_quotes():
    results = None
    try:
        results = list(Quote.query.all())
    except:
        print("Unexpected error:", sys.exc_info()[0])
    return results

def bulk_upload_quotes(quotes):

    try:
        s = db.session
        s.add_all(quotes)
        s.commit
    except:
        print("Unexpected error:", sys.exc_info()[0])

    # db.session
    #     default mode of autocommit=False 
    #     = a new transaction will be begun immediately after the commit, 
    #     but note that the newly begun transaction does *not* use any connection resources 
    #     until the first SQL is actually emitted

    #    public_methods = (
    #     "__contains__",
    #     "__iter__",
    #     "add",
    #     "add_all",
    #     "begin",
    #     "begin_nested",
    #     "close",
    #     "commit",
    #     "connection",
    #     "delete",
    #     "execute",
    #     "expire",
    #     "expire_all",
    #     "expunge",
    #     "expunge_all",
    #     "flush",
    #     "get_bind",
    #     "is_modified",
    #     "bulk_save_objects",
    #     "bulk_insert_mappings",
    #     "bulk_update_mappings",
    #     "merge",
    #     "query",
    #     "refresh",
    #     "rollback",
    #     "scalar",
    # )

    # db.session.add()
    # db.session.add_all
    #     Place (an) object(s) in the Session
    #     with save_or_update_state
    #     persisted on the db on the next flush operation 
    #     repeated add() will be ignored
    #     opposite of add() is expunge()
    # db.session.expunge
    # db.session.expunge_all
    #     Remove all object instances from this ``Session
    # db.session.refresh
    #     Expire and refresh the attributes on the given instance.
    # db.session.expire
    # db.session.expire_all
    #     Marks the attributes of an instance as out of date
    # db.session.flush
    #     not intended for general use
    # db.session.commit
    #     Flush pending changes and commit the current transaction.
    #     in code: also .self.close() => closes the session?
    # db.session.autocommit
    # db.session.autoflush
    #     db.session.merge
    #     Copy the state of a given instance into a corresponding instance
    #     within this :class:`.Session`.

    #     :meth:`.Session.merge` examines the primary key attributes of the
    #     source instance, and attempts to reconcile it with an instance of the
    #     same primary key in the session.   If not found locally, it attempts
    #     to load the object from the database based on primary key, and if
    #     none can be located, creates a new instance.
    # db.session.bulk_save_objects
    #     allows mapped objects to be used as the
    #     source of simple INSERT and UPDATE operations which can be more easily
    #     grouped together into higher performing "executemany"
    #     operations
    #     ignores whether or not attributes
    #     have actually been modified in the case of UPDATEs

    #     whether the object is sent as an INSERT or an
    #      UPDATE is dependent on the same rules used by the :class:`.Session

    #      if the object has the
    #      :attr:`.InstanceState.key`
    #      attribute set, then the object is assumed to be "detached" and
    #      will result in an UPDATE.  Otherwise, an INSERT is used.

    #      :param return_defaults: when True, rows that are missing values which
    #      generate defaults !!!reduces the performance

    #      param update_changed_only: when True, UPDATE statements are rendered
    #      based on those attributes in each state that have logged changes

    # db.session.bulk_insert_mappings
    #     bulk insert feature allows plain Python dictionaries to be used as
    #     the source of simple INSERT operations which can be more easily
    #     grouped together into higher performing "executemany"
    #     operations.

    #     param render_nulls: When True, a value of ``None`` will result
    #      in a NULL value being included in the INSERT statement, rather
    #      than the column being omitted from the INSERT.
    #      allows to have the identical set of columns which
    #      allows the full set of rows to be batched to the DBAPI - cost: no server side defaults
    # db.session.bulk_update_mappings
    #     Perform a bulk update of the given list of mapping dictionaries   
    #     after updating calculated values in bulk 
    # db.session.rollback
    #     code: contains self.close?

    # db.session.execute
    #     bv result = session.execute(
    #         user_table.select().where(user_table.c.id == 5)
    #     )
    #     vb result = session.execute(
    #                     "SELECT * FROM user WHERE id=:param",
    #                     {"param":5}
    #                 )

    # db.session.invalidate
    #     like close, This can be called when
    #     the database is known to be in a state where the connections are
    #     no longer safe to be used.


    # db.session.begin
    # db.session.begin_nested
    # db.session.bind
    # db.session.bind_mapper
    # db.session.close
    # db.session.close_all
    # db.session.configure
    # db.session.connection
    # db.session.connection_callable
    # db.session.deleted
    # db.session.dirty

    # db.session.expire_on_commit    
    # db.session.identity_key
    # db.session.identity_map
    # db.session.info

    # db.session.is_active
    # db.session.is_modified

    # db.session.new
    # db.session.no_autoflush
    # db.session.object_session
    # db.session.prepare
    # db.session.prune
    # db.session.public_methods
    # db.session.query
    # db.session.query_property

    # db.session.registry
    # db.session.remove

    # db.session.scalar

    # print(f"starting bulk_upload_quotes(quotes)")

# pool_size=5
# the number of connections to keep open inside the connection pool
# pool_recycle=-1
# pool to recycle connections after the given number of seconds has passed
# example:
# from sqlalchemy import create_engine
# e = create_engine("mysql://scott:tiger@localhost/test", pool_recycle=3600)