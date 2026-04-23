# 🤝 Smart Volunteer Coordinator

### Data-driven resource allocation for disaster relief and social impact.

**🌐 LIVE DEMO:** [Click here to interact with the prototype!](https://smart-volunteer-coordinator-growx4oqjiwbyv5ss2xfla.streamlit.app)

> ⚠️ **Note to Judges & Reviewers:** > This live application is a proof-of-concept prototype built for this hackathon. To ensure privacy and security, the database is currently populated entirely with **mock/dummy data**. The names, locations, and incidents do not represent real people or actual emergencies. The data exists strictly to demonstrate the functionality, speed, and accuracy of the underlying matching algorithm.

## 📌 The Problem
During a crisis (like a natural disaster or community emergency), organizers are flooded with willing volunteers and urgent tasks. Matching the right person with the right skills to the right location manually is chaotic, slow, and inefficient. 

## 💡 Our Solution
The **Smart Volunteer Coordinator** is a data-driven prototype that replaces manual assignment with an automated matching algorithm. It instantly analyzes incoming task requirements (skills needed, urgency) and cross-references them with an active pool of available volunteers to deploy resources optimally.

## ✨ Key Features
* **Live Incident Dashboard:** View active emergencies sorted by urgency.
* **Volunteer Skill Tracking:** Maintain a real-time database of available personnel and their primary skills (e.g., Medical, Logistics, Heavy Lifting).
* **Smart Allocation Algorithm:** One-click deployment that instantly assigns the best-suited available volunteer to the highest-priority task.
* **Real-time Status Updates:** Automatically shifts volunteer status from "Available" to "Deployed" upon assignment.

## ⚙️ Tech Stack
* **Frontend/UI:** Streamlit (Python)
* **Data Processing:** Pandas
* **Deployment:** Streamlit Community Cloud & GitHub

---

## 🚀 How to Run the Prototype Locally

If you prefer to run this prototype on your own machine instead of using the live link, follow these steps:

1. Clone this repository to your local machine.
2. Ensure you have Python installed.
3. Open your terminal and install the required dependencies:
   ```bash
   pip install streamlit pandas
