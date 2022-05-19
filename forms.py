"""Forms for playlist app."""

from wtforms import SelectField, StringField
from wtforms.validators import Length, InputRequired
from flask_wtf import FlaskForm


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField('Playlist Name:', validators=[InputRequired(message='Name required')])
    description = StringField('Description:', validators=[Length(max=250)])


class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField('Song Title:', validators=[InputRequired(message='Enter song title')])
    artist = StringField('Artist:', validators=[InputRequired(message='Enter an artist')])


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
