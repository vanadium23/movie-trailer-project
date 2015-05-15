import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Vanadium23 Movie Trailers</title>

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.96.1/css/materialize.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.96.1/js/materialize.min.js"></script>
    <style type="text/css" media="screen">
        #trailer.modal {
          max-height: 100%;
        }
        #trailer .modal-content {
          height: 480px;
          padding: 0px;
        }
        #trailer-video {
          width: 100%;
          height: 100%;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.modal-trigger', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        $(document).ready(function () {
          $('.modal-trigger').leanModal({
            complete: function() {
              // Delete video when modal closes
              $("#trailer-video-container").empty();
            }
          });
          // Searching code
          $movies = $('span.movie-title');
          $('#search').keyup(function() {
              // Delete two or more spaces in a row
              var val = $.trim($(this).val()).replace(/ +/g, ' ').toLowerCase();
              $movies.parents('.movie').show();
              $movies.filter(function() {
                  var text = $(this).text().replace(/\s+/g, ' ').toLowerCase();
                  return !~text.indexOf(val);
              }).parents('.movie').hide();
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
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    <!-- Navbar with search -->
    <div class="navbar-fixed">
      <nav>
        <div class="nav-wrapper">
          <form>
            <div class="input-field">
              <input id="search" type="search" required placeholder="You can search title here...">
              <label for="search"><i class="mdi-action-search"></i></label>
              <i class="mdi-navigation-close"></i>
            </div>
          </form>
        </div>
      </nav>
    </div>
    <!-- Main Page Content -->
    <div class="container">
     <div class="row">
      {movie_tiles}
    </div>
    </div>
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
    <div class="col s6 m4 movie">
        <div class="card">
        <div class="card-image waves-effect waves-block waves-light">
          <img class="activator" src="{poster_image_url}" >
        </div>
            <div class="card-content">
              <span class="card-title activator grey-text text-darken-4"><i class="mdi-navigation-more-vert right"></i></span>
               <a class="waves-effect waves-light btn modal-trigger" href="#trailer" data-trailer-youtube-id={trailer_youtube_id}>View trailer</a>
            </div>
            <div class="card-reveal">
              <span class="card-title grey-text text-darken-4"><span class="movie-title">{movie_title}</span>({movie_year}) <i class="mdi-navigation-close right"></i></span>
              <p>{movie_description}</p>
              <p><a class="waves-effect waves-light btn modal-trigger" href="#trailer" data-trailer-youtube-id={trailer_youtube_id}>View trailer</a></p>
            </div>
        </div>
    </div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            movie_year=movie.year,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            movie_description=movie.description
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the placeholder for the movie tiles with the actual dynamically generated content
    rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser
    url = os.path.abspath(output_file.name)
    # open in a new tab, if possible
    webbrowser.open('file://' + url, new=2)
