from bottle import run
from bottle import route
from bottle import request
from bottle import HTTPError

import album
x = 0


@route("/albums/<artist>")
def albums(artist):
    albums_list = album.find(artist)
    if not albums_list:
        message = "Albums {} not found".format(artist)
        result = HTTPError(404, message)
    else:
        album_len = len(albums_list)
        album_names = [album.album for album in albums_list]
        result = "Albums list {} ({}): ".format(artist, album_len)
        result += ", ".join(album_names)
    return result


@route("/albums", method="POST")
def albums():
    year = request.forms.get("year")
    artist = request.forms.get("artist")
    genre = request.forms.get("genre")
    name = request.forms.get("album")

    try:
        year = int(year)
    except ValueError:
        return HTTPError(400, "Incorrect album year: {}".format(request.forms.get("year")))

    try:
        new_album = album.save(year, artist, genre, name)
    except AssertionError as err:
        result = HTTPError(400, str(err))
    except album.AlreadyExists as err:
        result = HTTPError(409, str(err))
    else:
        result = "Album {} \"{}\" ({} year) saved".format(artist, name, year)

    return result


if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)
