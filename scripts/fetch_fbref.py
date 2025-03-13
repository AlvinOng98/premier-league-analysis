import soccerdata as sd
import pandas as pd

def fetch_data():
    
    league = "ENG-Premier League"

    # Fetch player stats
    fbref = sd.FBref(leagues=[league])
    player_stats = fbref.read_player_season_stats(stat_type="standard")
    print("Player Stats Sample:\n", player_stats.head())

    # Fetch team stats
    team_stats = fbref.read_team_season_stats(stat_type="standard")
    print("\nTeam Stats Sample:\n", team_stats.head())

    return player_stats, team_stats

if __name__ == "__main__":
    fetch_data()