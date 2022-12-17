from flask import render_template, Blueprint
import utils

ribbon_blueprint = Blueprint("ribbon_blueprint", __name__, template_folder='templates')
file_posts = "static/posts.json"
file_comments = "static/comments.json"
file_bookmarks = "templates/bookmarks.json"


@ribbon_blueprint.route("/")
#  выводит все посты
def ribbon():
    posts = utils.read_json(file_posts)

    return render_template("index.html", posts=posts)