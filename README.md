# MediAssistAI (Web Edition) - Cloud-Ready & Serverless

[![UN SDG Goal 3](https://img.shields.io/badge/SDG-Goal%203%3A%20Good%20Health%20%26%20Well--Being-emerald?style=for-the-badge)](https://sdgs.un.org/goals/goal3)

This directory contains the **Web Edition** of **MediAssistAI**. It is a serverless, single-file static web application designed to run completely inside the browser without requiring a backend server. 

Data (medications, logs, symptoms, and vitals) is permanently stored in the browser's database using the **LocalStorage API**.

---

## 🚀 How to Run Locally

You do not need to install anything or run any commands!
1. Open the folder.
2. Double-click on **`index.html`** to open it instantly in Chrome, Safari, Edge, or Firefox.

---

## ☁️ How to Host Online for Free (In Under 60 Seconds)

You can publish this website on the live internet so anyone can access it via a link (without running on localhost).

### Option A: Netlify Drop (Easiest - Drag & Drop)
1. Open your web browser and go to **[netlify.com/drop](https://www.netlify.com/drop)** (no login required to start).
2. Drag and drop the folder containing your `index.html` file into the upload box on the screen.
3. In 5 seconds, Netlify will publish your site and give you a live public link (e.g. `https://random-name.netlify.app`).
4. (Optional) Sign up to rename your site (e.g. `https://mediassist-ai.netlify.app`).

### Option B: GitHub Pages (Recommended for College Portfolios)
1. Create a new repository on your GitHub account named `MediAssistAI-Web`.
2. Upload the `index.html` file into your repository.
3. Go to the repository **Settings** tab.
4. On the left sidebar, click on **Pages**.
5. Under **Build and deployment**, change the Source dropdown to **`Deploy from a branch`**, select the **`main`** branch, and click **`Save`**.
6. Refresh the page in 1 minute. GitHub will provide you with a live link (e.g. `https://your-username.github.io/MediAssistAI-Web/`).

---

## 🗂️ Project Directory Structure
```
MediAssistAI_Web/
├── index.html           # Standalone Serverless App (HTML + CSS + JS)
├── README.md            # Hosting guide
└── zip_web.py           # Zipping script to generate MediAssistAI_Web.zip
```
