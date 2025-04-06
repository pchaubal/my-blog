from flask import Flask, render_template
from markupsafe import Markup
import markdown
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Load all blog post titles from markdown files
    posts = [f[:-3] for f in os.listdir("posts") if f.endswith(".md")]
    return render_template("base.html", posts=posts)

@app.route('/post/<title>')
def post(title):
    filepath = f'posts/{title}.md'
    if not os.path.exists(filepath):
        return "Post not found", 404

    with open(filepath, 'r', encoding='utf-8') as f:
        content_md = f.read()

    # Convert markdown to HTML with code support
    content_html = markdown.markdown(content_md, extensions=['fenced_code', 'codehilite'])

    return render_template("post.html", content=Markup(content_html), title=title)

