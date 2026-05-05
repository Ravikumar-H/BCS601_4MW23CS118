# Cloud Scientific Calculator ☁️🧮
**Project for BCS601 - Cloud Computing**

**Student Name:** Ravikumar  
**USN:** 4MW23CS118  
**Live Application URL:** [https://bcs601-4mw23cs118.el.r.appspot.com/](https://bcs601-4mw23cs118.el.r.appspot.com/)

## 📖 Introduction
This project demonstrates the practical implementation of cloud computing concepts by developing a web application that functions as a fully interactive Scientific Calculator. The application utilizes a modern, responsive UI framework on the frontend and a secure Python evaluation engine on the backend to accurately compute complex mathematical expressions, including trigonometry, logarithms, and roots. It is deployed using Platform as a Service (PaaS) via Google Cloud App Engine.

## 🛠️ Technology Stack
* **Frontend:** HTML5, CSS3 (Modern Glassmorphism/Clean Theme), JavaScript (DOM manipulation)
* **Backend:** Python 3.12, Flask Framework
* **Cloud Platform:** Google Cloud Platform (GCP) App Engine (Standard Environment)
* **Web Server:** Gunicorn

## 🚀 Deployment Steps Executed
1. Developed the application logic and user interface locally.
2. Configured `app.yaml` for the Python 3.12 runtime and defined deployment behavior.
3. Specified Python package dependencies in `requirements.txt`.
4. Utilized Google Cloud Shell to authenticate and manage project files.
5. Granted necessary IAM permissions (`storage.admin` and `artifactregistry.admin`) to the default service account to allow Cloud Build to compile the application.
6. Deployed the application to the global web using the `gcloud app deploy` command.

## 📁 Repository Structure
* `main.py` - The core Python backend server and mathematical logic.
* `templates/index.html` - The frontend application interface, styling, and client-side scripting.
* `requirements.txt` - Python dependencies required by Google Cloud.
* `app.yaml` - Google App Engine configuration file.
* `README.md` - Project documentation.
