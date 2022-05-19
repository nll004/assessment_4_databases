from app import app
import models

models.connect_db(app)

playlist1 = models.Playlist(name='Bluegrass')
playlist2 = models.Playlist(name='Rock', description='Best of Rock')
playlist3 = models.Playlist(name='Top 5', description='Top 5 songs for the summer')

models.db.session.add(playlist1)
models.db.session.add(playlist2)
models.db.session.add(playlist3)
models.db.session.commit()

song1 = models.Song(title='Cheap Cocaine', artist='Willi Carlisle')
song2 = models.Song(title='Nose to the Grindstone', artist='Tyler Childers')
song3 = models.Song(title='Blackbird Song', artist='Jamie Commons')
song4 = models.Song(title='Evil Angel', artist='Breaking Benjamin')
song5 = models.Song(title='Dairy of Jane', artist='Breaking Benjamin')
song6 = models.Song(title='Oats in the Water', artist='Ben Howard')
song7 = models.Song(title='Into the Fire', artist='Asking Alexandria')
song8 = models.Song(title='Cold', artist='Breaking Benjamin')
song9 = models.Song(title='Black Fly', artist='Ben Howard')
song10 = models.Song(title='Tears Dont Fall', artist='Bullet for my Valentine')

models.db.session.add(song1)
models.db.session.add(song2)
models.db.session.add(song3)
models.db.session.add(song4)
models.db.session.add(song5)
models.db.session.add(song6)
models.db.session.add(song7)
models.db.session.add(song8)
models.db.session.add(song9)
models.db.session.add(song10)
models.db.session.commit()


comb1 = models.PlaylistSong(playlist_id='1', song_id='1')
comb2 = models.PlaylistSong(playlist_id='1', song_id='2')
comb3 = models.PlaylistSong(playlist_id='1', song_id='3')
comb4 = models.PlaylistSong(playlist_id='2', song_id='4')
comb5 = models.PlaylistSong(playlist_id='2', song_id='5')
comb6 = models.PlaylistSong(playlist_id='2', song_id='6')
comb7 = models.PlaylistSong(playlist_id='2', song_id='7')
comb8 = models.PlaylistSong(playlist_id='2', song_id='8')
comb9 = models.PlaylistSong(playlist_id='2', song_id='9')
comb10 = models.PlaylistSong(playlist_id='3', song_id='10')
comb11 = models.PlaylistSong(playlist_id='3', song_id='2')
comb12 = models.PlaylistSong(playlist_id='3', song_id='6')
comb13 = models.PlaylistSong(playlist_id='3', song_id='8')
comb14 = models.PlaylistSong(playlist_id='3', song_id='7')
comb15 = models.PlaylistSong(playlist_id='3', song_id='10')

models.db.session.add_all([comb1, comb2, comb3, comb4, comb5,
comb6, comb7, comb8, comb9, comb10,
comb11, comb12, comb13, comb14, comb15])

models.db.session.commit()
