import os
import markdown
from jinja2 import Environment, FileSystemLoader
from markupsafe import Markup
import shutil
from datetime import datetime

# Setup
env = Environment(loader=FileSystemLoader("templates"))
base_template = env.get_template("base.html")
post_template = env.get_template("post.html")
tab_template = env.get_template("tabs.html")

POSTS_DIR = "posts"
TABS_DIR = "tabs"
OUTPUT_DIR = "output"
STATIC_DIR = "static"

def main():
    # Ensure output directory exists
    remove_directory_contents(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    copy_static_files()
    make_index_page()
    make_tab_pages()
    make_post_pages()

    return

# Copy static files
def copy_static_files():
    if os.path.exists(os.path.join(OUTPUT_DIR, "static")):
        shutil.rmtree(os.path.join(OUTPUT_DIR, "static"))
    shutil.copytree(STATIC_DIR, os.path.join(OUTPUT_DIR, "static"))
    return


# Generate index page
def make_index_page():
    # post_filenames = [f for f in os.listdir(POSTS_DIR) if f.endswith(".md")]
    # posts = [f[:-3] for f in post_filenames]
    with open ( "home.md", "r", encoding="utf-8" ) as f:
        content_md = f.read()
    content_html = markdown.markdown(content_md, extensions=["fenced_code", "codehilite"])
    html = post_template.render( title="Home", content=Markup(content_html), current_page="home" )
    with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    return

# Build tabs list
def make_tab_pages():
    # Ensure output directory exists
    os.makedirs(f"{OUTPUT_DIR}/tabs", exist_ok=True)
    tabs_filename = [f for f in os.listdir(TABS_DIR) if f.endswith(".md")]
    tabs = [ f[:-3] for f in tabs_filename ]
    # Generate each tabs page
    for tabname in tabs:
        with open (os.path.join(TABS_DIR, f"{tabname}.md"), "r", encoding="utf-8" ) as f:
            content_md = f.read()
        #
        content_html = markdown.markdown(content_md, extensions=["fenced_code", "codehilite"])
        final_html = tab_template.render(title=tabname,  content=Markup(content_html), current_page=tabname)
        with open(os.path.join(OUTPUT_DIR, f"tabs/{tabname}.html"), "w", encoding="utf-8") as f:
            f.write(final_html)
        #

    make_archive_page()
    return

def make_archive_page():
    # Get post names and timestamps
    post_filenames = [
                        (f[:-3], os.path.getmtime(os.path.join(POSTS_DIR, f)))
                        for f in os.listdir(POSTS_DIR)
                        if f.endswith(".md")
                        ]
    # Sort by modified time, newest first
    posts_sorted = sorted(post_filenames, key=lambda x: x[1], reverse=True)
    # Extract names only for other uses
    post_names = [name for name, _ in posts_sorted]
    # Format timestamps
    timestamp_map = {
        name: datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
        for name, ts in posts_sorted
    }
    # Render archive page
    archive_template = env.get_template("archive.html")
    archive_html = archive_template.render(posts=post_names, timestamps=timestamp_map, current_page="archive")
    with open(os.path.join(OUTPUT_DIR, "tabs/archive.html"), "w", encoding="utf-8") as f:
        f.write(archive_html)
    return

def make_post_pages():
    # Ensure output directory exists
    os.makedirs(f"{OUTPUT_DIR}/posts", exist_ok=True)
    # Build post list
    post_filenames = [f for f in os.listdir(POSTS_DIR) if f.endswith(".md")]
    posts = [f[:-3] for f in post_filenames]
    # Generate each post page
    for post_name in posts:
        with open(os.path.join(POSTS_DIR, f"{post_name}.md"), "r", encoding="utf-8") as f:
            content_md = f.read()
        content_html = markdown.markdown(content_md, extensions=["fenced_code", "codehilite"])
        final_html = post_template.render(title=post_name, content=Markup(content_html))
        with open(os.path.join(OUTPUT_DIR, f"posts/{post_name}.html"), "w", encoding="utf-8") as f:
            f.write(final_html)
    return

def remove_directory_contents(directory_path):
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        try:
            shutil.rmtree(file_path) if os.path.isdir(file_path) else os.remove(file_path)
        except Exception as e:
            print(f"Error removing {file_path}: {e}")


if __name__ == "__main__":
    main()
    print("✅ Static site generated in /output")


