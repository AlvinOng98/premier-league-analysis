from fetch_fbref import fetch_data

def main():
    print("🚀 Fetching Premier League data...")
    player_stats, team_stats = fetch_data()
    
    print("\nData fetching complete, storing in database...")

    # saves raw data to csv
    player_stats = player_stats.reset_index()
    team_stats = team_stats.reset_index()
    player_stats.to_csv("data/raw/player_stats.csv", index=False)  # Saves without the index column
    team_stats.to_csv("data/raw/team_stats.csv", index=False)  # Saves without the index column

if __name__ == "__main__":
    main()