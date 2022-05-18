"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    # ADD THE NECESSARY CODE HERE


class Song(db.Model):
    """Song."""

    # ADD THE NECESSARY CODE HERE


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    # ADD THE NECESSARY CODE HERE


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
