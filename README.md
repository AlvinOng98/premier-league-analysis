
# ⚽ Premier League Sports Analytics Dashboard

![Project Banner](https://img.shields.io/badge/Status-Complete-success?style=flat-square)
![Tool](https://img.shields.io/badge/Built%20with-Python%20%7C%20SQL%20%7C%20Tableau-blue?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square)

## 📘 Project Overview

This project is a comprehensive sports analytics case study focused on the **English Premier League**, one of the most prestigious football leagues globally. Leveraging historical data over six seasons, it explores player and team performances through a structured analytics pipeline — from data collection and processing, to modeling, visualization, and dashboarding.

## 🎯 Business Context

The project is rooted in the growing impact of **data-driven decision making** in professional sports. With clubs investing in analytics to gain competitive edges on the pitch and in recruitment, this analysis simulates what clubs or analysts might use internally for strategic planning.

## 📌 Business Goals

This project seeks to:
- Identify **top-performing players and teams** across multiple seasons.
- Analyze correlations between **possession, scoring, and discipline**.
- Understand how **team and player metrics evolve over time**.
- Segment players based on playing styles using **clustering**.
- Build predictive models for **goal output** using regression.
- Deliver a clean and insightful **Tableau dashboard** for stakeholders.

## 📦 Dataset & Schema

Data was sourced from **FBref.com**, scraped using the `soccerdata` Python package, and structured into an SQLite database. Two main datasets were created:

- **PlayerStatistics**
- **TeamStatistics**

> Each dataset includes performance metrics like:  
> `Goals`, `Assists`, `xG`, `Progressive Passes`, `Yellow Cards`, and more.

## 🛠️ Tech Stack

| Tool/Language | Purpose |
|---------------|---------|
| **Python** (Pandas, Matplotlib, Seaborn) | Data cleaning, analysis, and visualization |
| **SQLite** | Structured data storage |
| **SQL** | Data querying and aggregation |
| **Tableau** | Dashboard creation and interactive visualization |
| **Jupyter Notebook** | EDA, clustering, regression, and insights |

## 🔍 Analytical Workflow

### 1. **Exploratory Data Analysis (EDA)**
- Trends in goals, assists, possession, and xG
- Distribution and variability in player statistics
- Team-level performance snapshots

### 2. **Correlation Analysis**
- Examined relationships between metrics like possession and goal scoring
- Identified key predictors of team success

### 3. **Clustering**
- Used KMeans to segment players based on performance attributes
- Helped uncover hidden roles or archetypes across seasons

### 4. **Regression**
- Built models to predict **Goals Scored** using features like:
  - `xG`, `Progressive Passes`, `Non-Penalty Goals`, etc.
- Evaluated using R² and residual analysis

## 📊 Interactive Dashboard (Tableau)

The dashboard is divided into two main sections:

### 🏟️ **Team Performance Dashboard**
- League table based on goals, possession, or xG
- Head-to-head comparisons with league average
- Line charts for trend analysis
- Radar charts for metric breakdown
- Best & worst performer rankings

### 👤 **Player Performance Dashboard**
- Player-level selector with team filtering
- Individual stats and rankings
- Visual comparisons with teammates and league
- Radar chart of player profile

## 🚀 Key Takeaways

- **Player goal-scoring efficiency** and **progressive stats** are highly correlated with team success.
- **Clustering analysis** reveals tactical diversity in player styles.
- **Regression models** highlight the predictive power of `xG` and passing metrics.
- The Tableau dashboard provides a **holistic overview** of league dynamics and player value.

## 🔮 Future Work

- Expand to include **advanced stats** (e.g., pressures, tackles, shot-creating actions).
- Add **time-series modeling** for performance forecasting.
- Incorporate **transfer market data** and **injury history**.
- Build a recommendation engine for **recruitment analytics**.

## 📁 Repository Structure

```bash
📦Premier-League-Sports-Analytics
 ┣ 📁data/
 ┃ ┣ player_stats_cleaned.csv
 ┃ ┗ team_stats_cleaned.csv
 ┣ 📁notebooks/
 ┃ ┗ Sports_Analytics_Premier_League.ipynb
 ┣ 📁dashboard/
 ┃ ┗ Premier_League_Dashboard.twbx
 ┣ 📄README.md
 ┗ 📄requirements.txt
```

## 🧠 Author

**Alvin Ong**  
Aspiring Data Analyst with a passion for sports and storytelling through data.  
[GitHub](https://github.com/AlvinOng98) | [LinkedIn](https://www.linkedin.com/in/alvinong98/)
