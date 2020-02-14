import webbrowser


class Song():
    def __init__(self,song_title,songs_description,poster_image,song_youtube_link):
        self.title = song_title
        self.song_desc = songs_description
        self.poster_image_url = poster_image
        self.song_url = song_youtube_link
    
    def show_trailer(self):
        webbrowser.open(self.song_url)