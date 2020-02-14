import song_class
import songs_website


# variable_name = ["title","description","poster_url","youtube_link"]
song1 = song_class.Song("Ed Sheeran",
"Ed Sheeran Album",
"https://jazelinnsoul.files.wordpress.com/2015/06/ed-sheeran-x-album-cover-01.jpg"
,"https://www.youtube.com/watch?v=lp-EO5I60KA")

song2 = song_class.Song("Post Malone-WOW",
"Post Malone song",
"https://i.ytimg.com/vi/P6hVhjnKZkQ/maxresdefault.jpg"
,"https://www.youtube.com/watch?v=393C3pr2ioY")


list_of_songs = [ song1,song2]

songs_website.open_songs_page(list_of_songs)

