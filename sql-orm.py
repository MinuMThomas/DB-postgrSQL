from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" db
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create class-based model for the "Artist" table
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArrtistId = Column(Integer, ForeignKey("Artist.ArtistId"))


# create a class-based model for the "Track" table
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True),
    Name = Column(String),
    AlbumId = Column(Integer, ForeignKey("album_table.AlbumId")),
    MediaType = Column(Integer, primary_key=False),
    GenerId = Column(Integer, primary_key=False),
    Composer = Column(String),
    milliseconds = Column(Integer),
    Bytes = Column(Integer),
    UnitPrice = Column(Float)



# instead of connecting to the db directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the db using declarative_base subclass
base.metadata.create_all(db)
