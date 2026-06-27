# PMW Day 1 – AI Track GitHub Portfolio

Hi, I'm **Areeba Akmal**, a Cybersecurity student with a growing interest in **Artificial Intelligence, Machine Learning, Cloud Computing, and Software Development**. This repository is my **Day 1 submission** for the PMW AI Track and serves as the foundation for my public GitHub portfolio.

> **Note:** This portfolio was initially built by hand with HTML and CSS, then **enhanced using AI assistance in Cursor** to add new sections, improve styling, and implement fully responsive design.

---

## Track Information

| Field | Details |
|-------|---------|
| **Program** | PMW AI Track |
| **Module** | Week 1 – Foundations & Setup |
| **Repository** | [PMW-day1](https://github.com/AreebaAkmal/PMW-day1) |
| **Author** | Areeba Akmal |

---

## What I Built

- A professional public GitHub repository for the PMW AI Track
- A responsive personal portfolio website using HTML, CSS, and JavaScript
- A documented README covering setup, features, and learning goals
- A GitHub profile prepared for future AI and cybersecurity projects

---

## Portfolio Features

The portfolio website (`index.html`) includes the following sections:

| Section | Description |
|---------|-------------|
| **Hero / Header** | Introduction with name, role, and quick links to projects and GitHub |
| **About Me** | Background as a Cybersecurity student exploring AI and ML |
| **AI Interests** | Tag-style display of focus areas (ML, Deep Learning, NLP, etc.) |
| **Skills** | Responsive grid of current technical skills |
| **Projects** | Card-based project showcase with descriptions, tech tags, and links |
| **Learning Goals** | Goal cards with status badges and progress indicators |
| **Contact** | GitHub and email links |
| **Navigation** | Fixed nav bar with smooth scrolling and mobile hamburger menu |

### Design & Responsiveness

- Modern dark purple theme with gradient accents and glass-style cards
- Google Fonts (Inter, Space Grotesk) for improved typography
- CSS Grid and Flexbox layouts that adapt to all screen sizes
- Breakpoints for desktop, tablet (769–1024px), mobile (≤768px), and small phones (≤480px)
- Fluid typography using `clamp()` for readable text at any viewport width

---

## AI-Assisted Development with Cursor

This project was developed and improved using **[Cursor](https://cursor.com)** — an AI-powered code editor. AI assistance was used as a learning and productivity tool, not as a replacement for understanding the code.

### How Cursor Was Used

1. **Initial portfolio** — Built manually with HTML and CSS as the Day 1 foundation
2. **Enhancement pass** — Used Cursor Agent to add Projects and Learning Goals sections, refine styling, and make the site fully responsive
3. **Documentation** — Used Cursor to expand this README with setup instructions and project details

### What I Learned from AI-Assisted Development

- How to write clear prompts to describe desired features and layout changes
- How to review and understand AI-generated HTML/CSS before accepting changes
- How responsive design works in practice (media queries, CSS Grid, mobile navigation)
- How modern developers combine manual coding with AI tools to iterate faster

### My Approach

I treat AI as a **collaborative assistant**: I define the goals, review every change, and take responsibility for the final code in this repository. All content reflects my own background, skills, and learning path.

---

## Project Setup

No build tools or dependencies are required. This is a static site.

### Prerequisites

- A modern web browser (Chrome, Firefox, Edge, or Safari)
- [Git](https://git-scm.com/) (optional, for cloning)
- [Cursor](https://cursor.com/) (optional, for AI-assisted editing)

### Option 1: Clone and Open Locally

```bash
git clone https://github.com/AreebaAkmal/PMW-day1.git
cd PMW-day1
```

Open `index.html` in your browser:

- **Windows:** Double-click `index.html`, or right-click → Open with → your browser
- **macOS / Linux:** `open index.html` or `xdg-open index.html`

### Option 2: Download ZIP

1. Go to [github.com/AreebaAkmal/PMW-day1](https://github.com/AreebaAkmal/PMW-day1)
2. Click **Code** → **Download ZIP**
3. Extract the folder and open `index.html` in your browser

### Option 3: GitHub Pages (Optional)

To publish the portfolio online:

1. Open your repository on GitHub → **Settings** → **Pages**
2. Under **Source**, select the `main` branch and `/ (root)` folder
3. Click **Save** and wait a few minutes
4. Your site will be available at: `https://areebaakmal.github.io/PMW-day1/`

---

## 3D Reconstruction Experiment

As part of the PMW AI Track, I completed a **3D Reconstruction** research and coding assignment. This module introduced how computers build 3D models from images and the foundational math behind spatial data.

### Research Completed

Research notes in `3d-reconstruction/notes.md` cover:

- What 3D reconstruction is and why it matters
- Practical applications in computer vision, robotics, cultural heritage, AR/VR, and autonomous vehicles
- Key techniques: **Structure from Motion (SfM)**, **Multi-View Stereo (MVS)**, and **Photogrammetry**
- Popular tools: **COLMAP**, **Meshroom**, **OpenMVG**, and **Open3D**

### Python Experiment

`3d-reconstruction/experiment.py` is a beginner-friendly Python script that:

- Defines four sample 3D coordinate points `(x, y, z)`
- Prints each point with a label
- Calculates the **Euclidean distance** between two pairs of points
- Explains how 3D points and distance relate to real reconstruction pipelines

**Run the experiment:**

```bash
cd 3d-reconstruction
python experiment.py
```

Expected output is saved in `3d-reconstruction/output/result.txt`.

### Files in `3d-reconstruction/`

| File / Folder | Purpose |
|---------------|---------|
| `notes.md` | Research notes on 3D reconstruction concepts and tools |
| `experiment.py` | Python experiment with 3D points and distance calculation |
| `output/result.txt` | Expected output from running `experiment.py` |
| `screenshots/` | Folder for submission screenshots (see `screenshots/README.md`) |

### Learning Outcomes

Through this assignment, I learned that:

1. 3D reconstruction converts 2D images into 3D models using geometry and computer vision.
2. SfM, MVS, and photogrammetry work together in typical reconstruction workflows.
3. 3D points and distance calculations are foundational — even simple Python code reflects concepts used in tools like COLMAP and Open3D.
4. This field connects directly to robotics, AR/VR, autonomous systems, and cultural heritage preservation.
5. Documenting research and running small experiments is an effective way to build understanding before using advanced ML pipelines.

---

## Folder Structure

```
PMW-day1/
├── index.html                  # Portfolio website (HTML, CSS, and JavaScript)
├── README.md                   # Project documentation
└── 3d-reconstruction/          # PMW 3D Reconstruction assignment
    ├── notes.md                # Research notes
    ├── experiment.py           # Python 3D points experiment
    ├── output/
    │   └── result.txt          # Expected experiment output
    └── screenshots/
        └── README.md           # Screenshot submission guide
```

| File | Purpose |
|------|---------|
| `index.html` | Complete portfolio — structure, styling, and mobile nav script |
| `README.md` | Setup guide, feature list, AI development notes, and learning goals |
| `3d-reconstruction/` | Research notes, Python experiment, output, and screenshot folder |

---

## Skills

- Python
- HTML & CSS
- Git & GitHub
- Cybersecurity Fundamentals
- Artificial Intelligence (Learning)
- Machine Learning (Learning)
- Problem Solving
- AI-Assisted Development with Cursor

---

## Future Learning Goals

These goals are tracked on the portfolio site and will guide upcoming projects in this repository:

| Goal | Status | Focus |
|------|--------|-------|
| **Machine Learning Fundamentals** | In Progress | Supervised/unsupervised learning, model evaluation, Python libraries |
| **Deep Learning & Neural Networks** | In Progress | Architectures, backpropagation, TensorFlow / PyTorch |
| **Cloud Computing (AWS / Azure)** | Planned | Deploying ML models, cloud infrastructure, scaling AI apps |
| **Natural Language Processing** | Planned | Sentiment analysis, chatbots, language models |
| **Open Source Contributions** | In Progress | GitHub collaboration and community projects |
| **Computer Vision** | Planned | Image classification, object detection, CNNs |

### Upcoming Projects

- **ML Classification Project** — Python-based data classification with scikit-learn
- **AI & Cybersecurity Integration** — Applying ML to threat detection and security analysis

---

## Project Status

- [x] GitHub profile updated
- [x] Public repository created
- [x] Portfolio webpage completed
- [x] Projects section added
- [x] Learning Goals section added
- [x] Responsive design implemented
- [x] Portfolio enhanced with AI assistance (Cursor)
- [x] README documented
- [x] 3D Reconstruction research notes completed
- [x] 3D Reconstruction Python experiment completed

---

## Contact

- **GitHub:** [github.com/AreebaAkmal](https://github.com/AreebaAkmal)
- **Email:** areebaakmal3699@gmail.com

---

Thank you for visiting my repository! More AI and cybersecurity projects will be added as I continue learning and building.
Updated after completing the PMW Day 1 assignment.
Areeba Akmal