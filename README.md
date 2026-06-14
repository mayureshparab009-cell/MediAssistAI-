# MediAssistAI (Web Edition) - Cloud-Ready & Serverless

[![UN SDG Goal 3](https://img.shields.io/badge/SDG-Goal%203%3A%20Good%20Health%20%26%20Well--Being-emerald?style=for-the-badge)](https://sdgs.un.org/goals/goal3)

This directory contains the **Web Edition** of **MediAssistAI**. It is a serverless, single-file static web application designed to run completely inside the browser without requiring a backend server. 

Data (medications, logs, symptoms, and vitals) is permanently stored in the browser's database using the **LocalStorage API**.

MediAssistAI is an AI-powered healthcare assistant application designed to combat medication non-adherence and facilitate symptom and vitals tracking. Built using **React (Vite)** on the frontend and **Flask (Python)** with **SQLite** on the backend, the application serves as a comprehensive tool to help patients, especially those with chronic diseases or elderly individuals, manage their prescriptions, monitor vital signs, and track daily symptoms.

This project is created in alignment with **United Nations Sustainable Development Goal 3 (Good Health and Well-being)**.

---

## 📸 Interface Preview
The user interface features a premium dark-themed **glassmorphic design** utilizing Outfit & Inter typography:
* **Dashboard:** Features dynamic compliance circular gauges, rolling 7-day adherence charts, recent vitals summaries, and today's schedule checklist.
* **Scheduler:** Manage medications, dosage details, custom times, and specific meal instructions.
* **Symptom Diary:** Input physical symptoms, severity ratings (1-10 slider), and monitor severity trends on an SVG coordinates line graph.
* **Vitals Tracker:** Record key health vitals (systolic/diastolic blood pressure, blood glucose levels, and heart pulse rate) and plot custom multi-line SVG charts.
* **AI Medical Companion:** Conversational chat interface to ask queries about drug summaries, side effects, and warning notifications on clinical emergencies.

---


---

## 🗂️ Project Directory Structure
```
MediAssistAI_Web/
├── index.html           # Standalone Serverless App (HTML + CSS + JS)
├── README.md            # Hosting guide
└── zip_web.py           # Zipping script to generate MediAssistAI_Web.zip
```
