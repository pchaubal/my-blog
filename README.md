# 📝 My Static Markdown Blog

This is a simple, dark-themed static blog website built with **Python**, **Markdown**, and **Jinja2**. It supports:

- 📚 Sidebar navigation
- 🌙 Dark theme
- 📐 Math rendering with MathJax
- 🧑‍💻 Code highlighting with Pygments
- ✍️ Posts written in Markdown
- ⚡ Hosted on GitHub Pages

---

## 🚀 Live Demo

[https://pchaubal.github.io/my-blog/](https://yourusername.github.io/my-blog/)

> Replace with your actual GitHub Pages URL

---

## 📁 Project Structure

```
my_blog/
├── build.py               ← Static site generator script
├── posts/                 ← Markdown blog posts
│   └── example_post.md
├── templates/             ← Jinja2 HTML templates
│   ├── base.html
│   └── post.html
├── static/                ← CSS & other static files
│   └── css/style.css
├── output/                ← Final static site (auto-generated)
└── requirements.txt       ← Python dependencies
```

---

## 🛠️ Setup Instructions

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Build the static website

```bash
python build.py
```

This will:
- Convert all Markdown posts in `/posts` into HTML
- Generate `index.html` and post pages in `/output`

### 3. Preview locally (optional)

```bash
cd output
python -m http.server
```

Then open: [http://localhost:8000](http://localhost:8000)

---

## 🌐 Deploy to GitHub Pages

### One-time setup:

1. Create a GitHub repo (e.g., `my-blog`)
2. Push the generated site to the `gh-pages` branch:

```bash
cd output
git init
git checkout -b gh-pages
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git add .
git commit -m "Deploy static site"
git push -u origin gh-pages --force
```

3. On GitHub:
   - Go to **Settings > Pages**
   - Set Source: `gh-pages` branch, folder: `/ (root)`

---

## 🆕 Adding a New Blog Post (Workflow)

1. Create a new Markdown file in the `posts/` folder:

```bash
touch posts/my_new_post.md
```

2. Write your blog post in Markdown:

```markdown
# My New Post

This is a new blog post.

Here is math: $$E = mc^2$$

```python
def greet():
    print("Hello, Markdown!")
```
```

3. Rebuild the site:

```bash
python build.py
```

4. Deploy the new version:

```bash
cd output
git add .
git commit -m "Add new blog post: My New Post"
git push
```

That’s it! The new post will appear on your live blog site.

---

## 📚 Features

- **Markdown** for blog content
- **MathJax** for LaTeX math (`$$...$$`)
- **Pygments** for syntax-highlighted code
- **Dark theme** styling
- **GitHub Pages** deployment

---

## 🧪 Future Ideas

- Add blog post metadata (title, date, tags)
- Add search functionality
- Pagination or filtering
- RSS feed generation

---

## 📄 License

MIT License

---

Happy blogging! 🚀
