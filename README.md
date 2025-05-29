# 🌤️ Streamlit Weather Forecast App

This interactive web app allows users to visualize temperature trends and sky conditions for the upcoming days in any specified location. Built with Streamlit and Plotly, it fetches real-time forecast data using the OpenWeatherMap API.

---

## 🚀 Features

- View weather forecasts for up to 5 days into the future
- Choose between temperature plots or sky condition icons
- Input any city worldwide
- Dynamic line chart using Plotly
- Live weather data fetched from OpenWeatherMap API
- Streamlit-powered responsive UI

---

## 🛠 Technologies Used

- Python
- `Streamlit` for the interactive UI
- `Plotly Express` for temperature visualizations
- `pandas` for data manipulation
- `requests` for API calls
- `python-dotenv` for environment variable management

---

📂 File Overview
- main.py: Frontend and interaction logic (Streamlit + Plotly)
- get_data.py: Fetches and cleans forecast data from the API
- .env: Stores your secret API key (excluded from version control)
- sky_images/: Folder containing sky condition icons

🌍 Real-World Applications
- Personal or travel weather planning
- Educational dashboards for meteorology
- Lightweight weather display for digital signage
