from flask import Flask, Blueprint, request, render_template, send_from_directory
from ribbon.app import ribbon_blueprint
from post.app import post_blueprint

app = Flask(__name__)
app.register_blueprint(ribbon_blueprint)
app.register_blueprint(post_blueprint)














app.run()