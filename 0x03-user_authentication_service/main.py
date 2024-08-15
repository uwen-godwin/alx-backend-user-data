import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, Integer, Sequence
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///:memory:", echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, Sequence('user_id_seq'),primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (self.name, self.fullname, self.nickname)

# creates table defined on the class model to the target db
Base.metadata.create_all(engine)

ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
# print(ed_user.name)
# print(ed_user.fullname)
# print(ed_user.id)

# for column in User.__table__.columns:
#     print(f"{column}: {column.type}")
session = Session()

# adds single object at a time
session.add(ed_user)
# our_user = session.query(User).filter_by(name="ed").first()

# print(ed_user is our_user)

# adds multiple class objects at once
session.add_all([
    User(name="Wendy", fullname='Wendy Williams', nickname='windy'),
    User(name='mary', fullname="mary contrary".capitalize(), nickname="mary"),
    User(name="fred", fullname="Fred Flintstone", nickname="freddy")
    ])
ed_user.nickname = "eddie"
print(session.dirty)
print(session.new)

# saves all transaction of a database
session.commit()
# print(ed_user.id)

fake_user = User(name="fakeuser", fullname="Invalid", nickname="12345")
session.add(fake_user)
ed_user.name = "Edwardo"

# print(session.query(User).filter(User.name.in_(["Edwardo", "fakeuser"])).all())
session.rollback() # used to revert any changes made within a transaction

print(session.query(User).filter(User.name.in_(['ed', 'fakeuser'])).all())
