class Song:
    count = 0
    genres = []
    artists = []
    
    def __init__(self, name,artist,genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(self.genre)
       

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls,genre):
        if genre not in cls.genres: 
            cls.genres.append(genre)

    @classmethod

    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1  
        else:
            cls.artist_count[artist] = 1 
    def add_to_artists(self):
        self.add_to_artist_count(self.artist)