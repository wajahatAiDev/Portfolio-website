"""
AI Student Portfolio Website
=============================
Main Flask application file.

HOW TO CUSTOMIZE:
- Edit the data near the top of this file (PROFILE, SKILLS, EDUCATION,
  CERTIFICATIONS, EXPERIENCE, PROJECTS, ACHIEVEMENTS, BLOG_POSTS, SOCIAL_LINKS).
- Everything is marked with "# CUSTOMIZE" comments.
"""

from flask import Flask, render_template, url_for
from datetime import datetime

app = Flask(__name__)
app.secret_key = "replace-this-with-a-random-secret-key"  # CUSTOMIZE: change for production


# ---------------------------------------------------------------------------
# EDITABLE DATA — replace everything below with your own information
# ---------------------------------------------------------------------------

# CUSTOMIZE: your basic profile info, shown on the Home page and footer
# CUSTOMIZE: cover/banner photo shown at the top of these pages.
# Just drop an image at each path (or leave it — a placeholder shows automatically
# if the file doesn't exist yet).
PAGE_COVERS = {
    "resume": "images/covers/resume-cover.jpg",
    "projects": "images/covers/projects-cover.jpg",
    "achievements": "images/covers/achievements-cover.jpg",
    "blog": "images/covers/blog-cover.jpg",
}

PROFILE = {
    "name": "Muhammad Wajahat khan",
    "title": "Artificial Intelligence Student",
    "tagline": "Building intelligent systems, one model at a time.",
    "intro": (
        "I am 21 year old, currently in 5th semester  (Graduation 2028) "
        "Pushing a career in Artificial Intelligence from Gomal University , DI khan, Pakistan."
        " Born and brought up in Mianwali, Pakistan. I have done my Intermediate from MLW Higher Secondary"
        "school Makkarwal Mianwali in 2023, with ICS.<br><br>"

        "My idea behind  taking up Artificial Intelligence is  my love for programming and the"
        "fact that, given the knowledge, i can make a computer do almost anything i want it to do.<br><br>"
        "i have a keen interest in the field of Machine Learning and Data Science, and i'm"
        "presently learning and working on the skills required to expertise in the same.<br><br>"

        "My hobbies include playoing simulation games, such as Microsoft Flight Simulator X,"
        "Euro Truck Simulator 2, and Tower 3D pro; reading articles, browsing YouTube"
        "recommendations, traveling, and binge watching series.<br>"

        "i am a firm believer of passion and determination"
    ),
    "profile_image": "images/IMG_1993.jpg",  # CUSTOMIZE: replace with your photo
    "location": "Faisalabad, Punjab, Pakistan",
    "email": "wajahat.aidev@gmail.com",
    "resume_file": "resume/resume.pdf",  # CUSTOMIZE: place your resume PDF here
}

# CUSTOMIZE: skills shown as badges on Home & Resume pages
SKILLS = {
    "Programming Languages": ["Python", "C++", "SQL", "JavaScript"],
    "AI / ML": ["Scikit-learn", "TensorFlow", "PyTorch", "Pandas", "NumPy"],
    "Tools & Technologies": ["Git & GitHub", "Jupyter Notebook", "Flask", "VS Code", "Linux"],
    "Other": ["Data Visualization", "REST APIs", "Problem Solving"],
}

# CUSTOMIZE: education timeline (most recent first)
EDUCATION = [
    {
        "degree": "BS Artificial Intelligence",
        "institution": "Your University Name",
        "duration": "2024 - 2028",
        "description": "Coursework in machine learning, deep learning, data structures, and algorithms.",
    },
    {
        "degree": "Intermediate (Pre-Engineering)",
        "institution": "Your College Name",
        "duration": "2021 - 2023",
        "description": "Focused on mathematics, physics, and computer science fundamentals.",
    },
]

# CUSTOMIZE: certifications list
CERTIFICATIONS = [
    {"name": "Machine Learning Specialization", "issuer": "Coursera / DeepLearning.AI", "year": "2025"},
    {"name": "Python for Data Science", "issuer": "IBM", "year": "2024"},
    {"name": "Introduction to Deep Learning", "issuer": "Coursera", "year": "2025"},
]

# CUSTOMIZE: internships / experience
EXPERIENCE = [
    {
        "role": "AI Intern",
        "organization": "Example Company",
        "duration": "Summer 2025",
        "description": "Worked on data preprocessing pipelines and helped train a classification model.",
    },
]

# CUSTOMIZE: replace with your own projects
PROJECTS = [
    {
        "id": 1,
        "title": "Titanic Survival Predictor",
        "description": "A machine learning model that predicts passenger survival on the Titanic using logistic regression and feature engineering.",
        "technologies": ["Python", "Scikit-learn", "Pandasssss", "Flask"],
        "github": "https://github.com/yourusername/titanic-predictor",
        "demo": "#",
        "image": "images/project-placeholder.jpg",
    },
    {
        "id": 2,
        "title": "Cricket Win Probability App",
        "description": "A live win-probability predictor for cricket matches, built with a trained ML model and a Flask web interface.",
        "technologies": ["Python", "Flask", "Scikit-learn", "JavaScript"],
        "github": "https://github.com/yourusername/cricket-win-probability",
        "demo": "#",
        "image": "images/project-placeholder.jpg",
    },
    {
        "id": 3,
        "title": "Terminal-Style Developer Portfolio",
        "description": "A dark, terminal-themed personal portfolio website with interactive command-line style navigation.",
        "technologies": ["HTML", "CSS", "JavaScript"],
        "github": "https://github.com/yourusername/terminal-portfolio",
        "demo": "#",
        "image": "images/project-placeholder.jpg",
    },
]

# CUSTOMIZE: achievements / awards / hackathons
# "image": path (inside static/) to a certificate/award photo. Falls back to a
# placeholder automatically if the file doesn't exist yet.
ACHIEVEMENTS = [
    {
        "title": "1st Place — University AI Hackathon",
        "date": "2025",
        "description": "Won first place for building an ML-powered solution within 24 hours.",
        "category": "Hackathon",
        "image": "images/achievements/hackathon.jpg",
    },
    {
        "title": "Dean's Honor List",
        "date": "2024",
        "description": "Recognized for outstanding academic performance.",
        "category": "Academic",
        "image": "images/achievements/deans-list.jpg",
    },
    {
        "title": "Kaggle Competition — Top 10%",
        "date": "2025",
        "description": "Ranked in the top 10% of participants in a machine learning competition.",
        "category": "Competition",
        "image": "images/achievements/kaggle.jpg",
    },
]

# CUSTOMIZE: blog posts — 'content' supports simple paragraphs separated by "\n\n"
# "image": path (inside static/) to a cover photo for the post. Falls back to a
# placeholder automatically if the file doesn't exist yet.
# "external_url": OPTIONAL. If you've published this post somewhere else
# (Medium, LinkedIn, Dev.to, etc.), paste that link here and the "Read More" /
# "View Post" button will redirect there instead of the built-in post page.
# Leave it as None (or remove the key) to use the built-in post page.
BLOG_POSTS = [
    {
        "id": 1,
        "title": "Getting Started with Machine Learning",
        "date": "2025-06-10",
        "category": "Machine Learning",
        "summary": "A beginner-friendly introduction to the core ideas behind machine learning.",
        "image": "images/blog/ml-basics.jpg",
        # CUSTOMIZE: if this post is actually published elsewhere (Medium, dev.to,
        # LinkedIn Articles, etc.), put that link here and "Read More" will send
        # visitors straight there instead of an internal page. Leave as None to
        # use the built-in blog post page instead.
        "external_url": None,
        "external_url": None,  # e.g. "https://medium.com/@you/your-post"
        "content": (
            "Machine learning can feel overwhelming at first, but it really comes down to "
            "a few core ideas: data, patterns, and predictions.\n\n"
            "In this post I walk through the basic workflow I follow when starting a new "
            "ML project — from cleaning data to training and evaluating a first model.\n\n"
            "The key takeaway: start simple, get something working end-to-end, then improve "
            "it step by step."
        ),
    },
    {
        "id": 2,
        "title": "Why I Chose to Study Artificial Intelligence",
        "date": "2025-04-02",
        "category": "Personal",
        "summary": "Reflecting on my journey into the field of AI and what excites me most about it.",
        "image": "images/blog/why-ai.jpg",
        "external_url": None,  # CUSTOMIZE: e.g. "https://medium.com/@you/why-i-chose-ai"
        "external_url": None,  # e.g. "https://medium.com/@you/your-post"
        "content": (
            "I've always been fascinated by how machines can learn from data instead of "
            "being explicitly programmed for every rule.\n\n"
            "Studying AI has opened my eyes to fields like computer vision, natural language "
            "processing, and reinforcement learning — and I'm excited to keep building projects "
            "in this space."
        ),
    },
    {
        "id": 3,
        "title": "Building My First Flask Web App",
        "date": "2025-02-15",
        "category": "Web Development",
        "summary": "Lessons learned from connecting a trained ML model to a simple Flask backend.",
        "image": "images/blog/first-flask-app.jpg",
        "external_url": None,  # CUSTOMIZE: e.g. link to where this post is actually hosted
        "external_url": None,  # e.g. "https://medium.com/@you/your-post"
        "content": (
            "Turning a Jupyter notebook model into an actual working web app taught me a lot "
            "about the gap between research code and production code.\n\n"
            "Flask made it straightforward to wrap my model in a few routes and a couple of "
            "HTML templates, and it's now my go-to tool for quick AI demos."
        ),
    },
]

# CUSTOMIZE: social / contact links shown on the Contact page and footer
SOCIAL_LINKS = {
    "github": "https://github.com/yourusername",
    "linkedin": "https://www.linkedin.com/in/muhammad-wajahat-khan-95a016421/",
    "email": PROFILE["email"],
}

# CUSTOMIZE: page-level cover/banner photos shown at the top of these pages.
# Falls back to a placeholder automatically if the file doesn't exist yet.
COVER_IMAGES = {
    "resume": "images/covers/resume-cover.jpg",
    "projects": "images/covers/projects-cover.jpg",
    "achievements": "images/covers/achievements-cover.jpg",
    "blog": "images/covers/blog-cover.jpg",
}


# ---------------------------------------------------------------------------
# ROUTES
# ---------------------------------------------------------------------------

@app.context_processor
def inject_globals():
    """Makes these variables available in every template automatically."""
    return {
        "profile": PROFILE,
        "social": SOCIAL_LINKS,
        "covers": COVER_IMAGES,
        "current_year": datetime.now().year,
    }


@app.route("/")
def home():
    # Show only a few featured projects on the home page
    featured_projects = PROJECTS[:3]
    return render_template("index.html", skills=SKILLS, projects=featured_projects)


@app.route("/resume")
def resume():
    return render_template(
        "resume.html",
        education=EDUCATION,
        skills=SKILLS,
        certifications=CERTIFICATIONS,
        experience=EXPERIENCE,
    )


@app.route("/projects")
def projects():
    return render_template("projects.html", projects=PROJECTS)


@app.route("/achievements")
def achievements():
    return render_template("achievements.html", achievements=ACHIEVEMENTS)


@app.route("/blog")
def blog():
    # Show most recent posts first
    posts = sorted(BLOG_POSTS, key=lambda p: p["date"], reverse=True)
    return render_template("blog.html", posts=posts)


@app.route("/blog/<int:post_id>")
def blog_post(post_id):
    post = next((p for p in BLOG_POSTS if p["id"] == post_id), None)
    if post is None:
        return render_template("post.html", post=None), 404
    return render_template("post.html", post=post)


@app.route("/contact")
def contact():
    # Contact page is info-only (icons + direct links) — no form to process.
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
