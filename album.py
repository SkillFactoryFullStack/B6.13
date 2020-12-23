import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DB_PATH = "sqlite:///albums.sqlite3"
Base = declarative_base()


class Album(Base):
    """
    Describes the structure of the album table for storing music library entries
    """

    __tablename__ = "album"

    id = sa.Column(sa.INTEGER, primary_key=True)
    year = sa.Column(sa.INTEGER)
    artist = sa.Column(sa.TEXT)
    genre = sa.Column(sa.TEXT)
    album = sa.Column(sa.TEXT)


class Error(Exception):
    pass


class AlreadyExists(Error):
    pass


def connect_db():
    """
    Establishes a connection to the database, creates tables if they
    do not already exist, and returns a session object
    """
    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()


def find(artist):
    """
    Finds all albums in the database for a given artist
    """
    session = connect_db()
    albums = session.query(Album).filter(Album.artist == artist).all()
    return albums


def save(year, artist, genre, name):
    # Checking the correctness of the input
    assert isinstance(year, int), "Invalid year"
    assert isinstance(artist, str), "Incorrect performer"
    assert isinstance(genre, str), "Incorrect genre"
    assert isinstance(name, str), "Invalid album"

    # Connection to database
    session = connect_db()
    existed_album = session.query(Album).filter(Album.album == name, Album.artist == artist).first()
    if existed_album is not None:
        raise AlreadyExists("The album has already been saved earlier.")

    new_album = Album(year=year, artist=artist, genre=genre, album=name)

    session.add(new_album)
    session.commit()

    return new_album
