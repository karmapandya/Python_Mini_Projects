import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Song Playlist!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .song-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .song-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.song-tile', function (event) {

            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            var source_url_to_open = 'http://www.youtube.com/watch?v=' + trailerYouTubeId + ''
            window.open(source_url_to_open, '_blank');
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the songs when the page loads
        $(document).ready(function () {
          $('.song-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">My Songs Playlist</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {song_tiles}
    </div>
  </body>
</html>
'''

# A single song entry html template
song_tile_content = '''
<div class="col-md-6 col-lg-4 song-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{song_title}</h2>
</div>
'''

def create_song_tiles_content(songs):
    # The HTML content for this section of the page
    content = ''
    for song in songs:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', song.song_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', song.song_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        content += song_tile_content.format(
            song_title=song.title,
            poster_image_url=song.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content

def open_songs_page(songs):
  # Create or overwrite the output file
  output_file = open('songs_playlist.html', 'w')

  rendered_content = main_page_content.format(song_tiles=create_song_tiles_content(songs))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible