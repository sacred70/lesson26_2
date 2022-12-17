from flask import render_template, Blueprint, request
import utils


search_blueprint = Blueprint("search_blueprint", __name__, template_folder='templates')
file_posts = "static/posts.json"
file_comments = "static/comments.json"
file_bookmarks = "templates/bookmarks.json"


@search_blueprint.route("/search")
#  выводит все посты
def search():
    s = request.args['s']
    posts = utils.search_for_posts(s)
    print(s)
    print(posts)

    return render_template("search.html")