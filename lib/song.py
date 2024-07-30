class Song:
    count = 0 
    genres = []
    genre_count = {}
    artists= []
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.genre = genre
        self.name = name 
        self.artist = artist
        Song.add_to_song_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_artists_count(artist)
        Song.add_to_genre_count(genre)



    @classmethod 
    def add_to_song_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            Song.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            Song.artists.append(artist)

    @classmethod
    def add_to_artists_count(cls, artist):
        if artist in cls.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] =1

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] =1
        

