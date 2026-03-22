# 📊 Quotes Scraper Dashboard

A full-stack Django web application that scrapes quotes data, stores it in a database, and visualizes insights through an interactive dashboard.

## 🚀 Live Demo
https://quotes-scraping.onrender.com/

## 🔐 Features
- User authentication (Signup/Login/Logout)
- Role-based access (Admin-only scraping)
- Web scraping using BeautifulSoup
- Data storage with Django ORM
- Interactive dashboard with Chart.js
- Tag and author analytics
- Search and filtering

## 🛠️ Tech Stack
- Backend: Django
- Frontend: HTML, CSS, Bootstrap
- Data Processing: Pandas
- Visualization: Chart.js
- Web Scraping: Requests, BeautifulSoup
- Deployment: Render

## 📸 Screenshots
<img width="581" height="446" alt="image" src="https://github.com/user-attachments/assets/dd76be2b-3e95-4d30-9daa-5879d00bba4b" />
<img width="1775" height="692" alt="image" src="https://github.com/user-attachments/assets/532ce581-aa4d-43a8-9f8b-db29eed8122b" />
<img width="1795" height="883" alt="image" src="https://github.com/user-attachments/assets/9d4a25d8-2243-4165-8200-971a2570dd85" />
<img width="1705" height="889" alt="image" src="https://github.com/user-attachments/assets/932782c0-1d6f-4688-8133-494c54f298ad" />





## ⚙️ Setup Instructions

```bash
git clone https://github.com/YOUR_USERNAME/Quotes-Scraping.git
cd Quotes-Scraping
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
