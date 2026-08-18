# AI Student Portfolio Website

A complete, responsive personal portfolio website built with **Flask**, **HTML5**, and **CSS3** —
designed for an Artificial Intelligence / Machine Learning student to showcase skills,
education, projects, achievements, blog posts, and contact info.

## Features

- Home page with hero section, skills, and featured projects
- Resume page with education/experience timeline, skills, and certifications
- Projects page with cards (title, description, tech stack, GitHub + demo links)
- Achievements page (certificates, awards, hackathons, competitions)
- Blog with a listing page and individual post pages
- Contact page with a working form (server-side validated, flash success message)
- Fully responsive, with a mobile hamburger menu
- Dark, modern, "AI/tech" themed design
- Clean Flask structure using Jinja2 template inheritance
- All content lives in plain Python data structures in `app.py` — easy to edit, no database needed

## Project Structure

```text
portfolio/
│
├── app.py                  # Flask app: routes + all editable content
├── requirements.txt
├── README.md
│
├── static/
│   ├── css/style.css       # All styling (single file, uses CSS variables)
│   ├── js/script.js        # Hamburger menu + flash message auto-dismiss
│   ├── images/             # Put your profile photo & project images here
│   └── resume/             # Put your resume.pdf here
│
└── templates/
    ├── base.html           # Shared navbar + footer (all pages extend this)
    ├── index.html          # Home
    ├── resume.html
    ├── projects.html
    ├── achievements.html
    ├── blog.html
    ├── post.html            # Single blog post
    └── contact.html
```

## 1. Installation

Make sure you have **Python 3.9+** installed. Then, from the `portfolio` folder:

```bash
# (Recommended) create a virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# macOS / Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## 2. Running the app

```bash
python app.py
```

Then open your browser at: **http://127.0.0.1:5000**

The app runs in debug mode by default (auto-reloads on code changes). Turn this off
before deploying (see `app.run(debug=True)` at the bottom of `app.py`).

## 3. Running it in VS Code

1. Open the `portfolio` folder in VS Code (`File > Open Folder`).
2. Open a terminal in VS Code (`` Ctrl+` ``).
3. Create/activate a virtual environment and install requirements as shown above.
4. Run `python app.py` in the terminal, or use the built-in "Run Python File" button.
5. Ctrl+Click the `http://127.0.0.1:5000` link in the terminal to open it in your browser.
6. Recommended extensions: **Python** and **Jinja** (for template syntax highlighting).

## 4. Customizing the site (do this!)

Everything you need to personalize is marked with `# CUSTOMIZE` comments in **`app.py`**:

| What to change              | Where |
|------------------------------|-------|
| Your name, title, bio, email | `PROFILE` dict |
| Skills                       | `SKILLS` dict |
| Education                    | `EDUCATION` list |
| Certifications               | `CERTIFICATIONS` list |
| Internships / experience     | `EXPERIENCE` list |
| Projects                     | `PROJECTS` list |
| Achievements / awards        | `ACHIEVEMENTS` list |
| Blog posts                   | `BLOG_POSTS` list |
| GitHub / LinkedIn links      | `SOCIAL_LINKS` dict |

Also replace these placeholder files:

- `static/images/IMG_1993.jpg` — your photo (shown on the Home page)
- `static/images/project-placeholder.jpg` — project thumbnail images
- `static/images/achievements/*.jpg` — one photo per achievement (certificate/award photo)
- `static/images/blog/*.jpg` — one cover photo per blog post
- `static/resume/resume.pdf` — your actual resume PDF (used by the "View Resume" / "Download Resume" buttons)

> If an image file is missing, the site automatically falls back to a placeholder
> image so nothing breaks — just add your real files when ready.

## 5. Resume page

The Resume page has two buttons: **View Resume** opens `resume.pdf` in a new browser
tab (so it reads like flipping through a PDF), and **Download Resume** saves it to
the visitor's device. Both point at `profile.resume_file` in `app.py` — just drop
your PDF into `static/resume/resume.pdf`.

## 6. Achievements page

Each achievement card shows a photo and a **View Achievement** button. Clicking it
opens a lightbox with the full-size image, title, category, date, and description —
no extra page/route needed. Add each achievement's image path in the `ACHIEVEMENTS`
list in `app.py`.

## 7. Contact page

The contact page is info-only: icon cards linking directly to Email, Location,
GitHub, and LinkedIn — no form to submit or backend to wire up. Update the values
in `PROFILE` and `SOCIAL_LINKS` in `app.py` to change what's shown.

## 8. Deployment notes

This app is ready to deploy to any platform that supports Flask (Render, Railway,
PythonAnywhere, Heroku, etc.):

- Set `debug=False` before deploying.
- Set a real, secret value for `app.secret_key` (used for flash messages).
- Use a production WSGI server such as `gunicorn` instead of the Flask dev server:
  ```bash
  pip install gunicorn
  gunicorn app:app
  ```

## License

Free to use and modify for your own personal portfolio.
