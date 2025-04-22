
# Premier League Sports Analytics Dashboard

![Project Banner](https://img.shields.io/badge/Status-Complete-success?style=flat-square)
![Tool](https://img.shields.io/badge/Built%20with-Python%20%7C%20SQL%20%7C%20Tableau-blue?style=flat-square)

## Project Overview

This project is a comprehensive sports analytics case study focused on the **English Premier League**, one of the most prestigious football leagues globally. Leveraging historical data over six seasons, it explores player and team performances through a structured analytics pipeline — from data collection and processing, to modeling, visualization, and dashboarding.

## Business Context

The project is rooted in the growing impact of **data-driven decision making** in professional sports. With clubs investing in analytics to gain competitive edges on the pitch and in recruitment, this analysis simulates what clubs or analysts might use internally for strategic planning.

## Business Goals

This project seeks to:
- Identify **top-performing players and teams** across multiple seasons.
- Analyze correlations between **possession, scoring, and discipline**.
- Understand how **team and player metrics evolve over time**.
- Segment players based on playing styles using **clustering**.
- Build predictive models for **goal output** using regression.
- Deliver a clean and insightful **Tableau dashboard** for stakeholders.

## Dataset & Schema

Data was sourced from **FBref.com**, scraped using the `soccerdata` Python package, and structured into an SQLite database. Two main datasets were created:

- **cleaned_standard_player_stats.csv**
- **cleaned_standard_team_stats.csv**

> Each dataset includes performance metrics like:  
> `Goals`, `Assists`, `xG`, `Progressive Passes`, `Yellow Cards`, and more.

## Tech Stack

| Tool/Language | Purpose |
|---------------|---------|
| **Python** (Pandas, Matplotlib, Seaborn) | Data cleaning, analysis, and visualization |
| **SQLite** | Structured data storage |
| **SQL** | Data querying and aggregation |
| **Tableau** | Dashboard creation and interactive visualization |

## Analytical Workflow

### 1. **Exploratory Data Analysis (EDA)**
- Trends in goals, assists, possession, and xG
- Distribution and variability in player statistics
- Team-level performance snapshots

### 2. **Correlation Analysis**
- Examined relationships between metrics like possession and goal scoring
- Identified key predictors of team success

### 3. **Clustering**
- Used KMeans to segment teams based on performance attributes
- Helped uncover team archetypes across seasons

## Interactive Dashboard (Tableau)

<div>
<div class='tableauPlaceholder' id='viz1745304988314' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pr&#47;PremierLeagueTeamStats_17453048145010&#47;TeamDashboard&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='PremierLeagueTeamStats_17453048145010&#47;TeamDashboard' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pr&#47;PremierLeagueTeamStats_17453048145010&#47;TeamDashboard&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-GB' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1745304988314');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1420px';vizElement.style.height='830px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1420px';vizElement.style.height='830px';} else { vizElement.style.width='100%';vizElement.style.height='3400px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
</div>

## Key Takeaways

- **Player goal-scoring efficiency** and **progressive stats** are highly correlated with team success.
- **Clustering analysis** reveals tactical diversity in player styles.
- **Regression models** highlight the predictive power of `xG` and passing metrics.
- The Tableau dashboard provides a **holistic overview** of league dynamics and player value.

## Future Work

- Expand to include **advanced stats** (e.g., pressures, tackles, shot-creating actions).
- Add **time-series modeling** for performance forecasting.
- Incorporate **transfer market data** and **injury history**.
- Build a recommendation engine for **recruitment analytics**.

## Repository Structure

```bash
📦Premier-League-Sports-Analytics
 ┣ 📁data/
 ┃ ┣ 📁cleaned/
 ┃ ┃ ┣ cleaned_standard_player_stats.csv
 ┃ ┃ ┗ cleaned_standard_team_stats.csv
 ┃ ┣ 📁raw/
 ┃ ┃ ┣ player_stats.csv
 ┃ ┃ ┗ team_stats.csv
 ┃ ┗ FBref_football_stats.db
 ┣ 📁notebooks/
 ┃ ┣ Sports_Analytics_Premier_League.ipynb
 ┃ ┗ standard_stats_cleaning.ipynb
 ┣ 📁scripts/
 ┃ ┣ db_create.py
 ┃ ┣ fetch_fbref.py
 ┃ ┗ main.py
 ┣ 📄README.md
 ┗ 📄requirements.txt
```

## 🧠 Author

**Alvin Ong**  
Aspiring Data Analyst with a passion for storytelling through data.  
[GitHub](https://github.com/AlvinOng98) | [LinkedIn](https://www.linkedin.com/in/alvinong98/)
