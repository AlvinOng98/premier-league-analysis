import sqlite3
import pandas as pd

# Database file
DB_FILE = 'data/FBref_football_stats.db'

# CSV files
PLAYER_CSV = 'data/cleaned/cleaned_standard_player_stats.csv'
TEAM_CSV = 'data/cleaned/cleaned_standard_team_stats.csv'

# Connect to SQLite database (creates it if it doesn't exist)
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Create tables using natural keys and composite primary keys
def create_tables():
    # Players table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Players (
            Name TEXT NOT NULL,
            BirthYear INTEGER NOT NULL,
            Nationality TEXT,
            Position TEXT,
            Age INTEGER,
            PRIMARY KEY (Name, BirthYear)
        )
    ''')

    # Teams table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Teams (
            Name TEXT PRIMARY KEY,
            UNIQUE (Name)
        )
    ''')

    # Leagues table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Leagues (
            Name TEXT PRIMARY KEY,
            UNIQUE (Name)
        )
    ''')

    # Seasons table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Seasons (
            Name TEXT PRIMARY KEY,
            UNIQUE (Name)
        )
    ''')

    # TeamStatistics table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS TeamStatistics (
            League TEXT NOT NULL,
            Season TEXT NOT NULL,
            Team TEXT NOT NULL,
            PlayersUsed INTEGER,
            AverageAge REAL,
            Possession REAL,
            MatchesPlayed INTEGER,
            GamesStarted INTEGER,
            MinutesPlayed INTEGER,
            NinetyMinutesPlayed REAL,
            Goals INTEGER,
            Assists INTEGER,
            GoalsPlusAssists INTEGER,
            NonPenaltyGoals INTEGER,
            PenaltyKickGoals INTEGER,
            PenaltyKickAttempts INTEGER,
            YellowCards INTEGER,
            RedCards INTEGER,
            ExpectedGoals REAL,
            ExpectedNonPenaltyGoals REAL,
            ExpectedAssistedGoals REAL,
            ExpectedNonPenaltyAssistedGoals REAL,
            ProgressiveCarries INTEGER,
            ProgressivePasses INTEGER,
            PRIMARY KEY (League, Season, Team),
            FOREIGN KEY (League) REFERENCES Leagues(Name),
            FOREIGN KEY (Season) REFERENCES Seasons(Name),
            FOREIGN KEY (Team) REFERENCES Teams(Name)
        )
    ''')

    # PlayerStatistics table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS PlayerStatistics (
            League TEXT NOT NULL,
            Season TEXT NOT NULL,
            Team TEXT NOT NULL,
            Player TEXT NOT NULL,
            BirthYear INTEGER NOT NULL,
            MatchesPlayed INTEGER,
            GamesStarted INTEGER,
            MinutesPlayed INTEGER,
            NinetyMinutesPlayed REAL,
            Goals INTEGER,
            Assists INTEGER,
            GoalsPlusAssists INTEGER,
            NonPenaltyGoals INTEGER,
            PenaltyKickGoals INTEGER,
            PenaltyKickAttempts INTEGER,
            YellowCards INTEGER,
            RedCards INTEGER,
            ExpectedGoals REAL,
            ExpectedNonPenaltyGoals REAL,
            ExpectedAssistedGoals REAL,
            ExpectedNonPenaltyAssistedGoals REAL,
            ProgressiveCarries INTEGER,
            ProgressivePasses INTEGER,
            ProgressivePassesReceived INTEGER,
            PRIMARY KEY (League, Season, Team, Player, BirthYear),
            FOREIGN KEY (League) REFERENCES Leagues(Name),
            FOREIGN KEY (Season) REFERENCES Seasons(Name),
            FOREIGN KEY (Team) REFERENCES Teams(Name),
            FOREIGN KEY (Player, BirthYear) REFERENCES Players(Name, BirthYear)
        )
    ''')

    conn.commit()

# Load data from CSV into tables
def load_data():
    # Load player data
    player_df = pd.read_csv(PLAYER_CSV)
    team_df = pd.read_csv(TEAM_CSV)

    # Insert unique leagues, seasons, and teams first
    for _, row in player_df.drop_duplicates(subset=['League', 'Season', 'Team']).iterrows():
        cursor.execute('INSERT OR IGNORE INTO Leagues (Name) VALUES (?)', (row['League'],))
        cursor.execute('INSERT OR IGNORE INTO Seasons (Name) VALUES (?)', (row['Season'],))  # Insert season
        cursor.execute('INSERT OR IGNORE INTO Teams (Name) VALUES (?)', (row['Team'],))

    for _, row in team_df.drop_duplicates(subset=['League', 'Season', 'Team']).iterrows():
        cursor.execute('INSERT OR IGNORE INTO Leagues (Name) VALUES (?)', (row['League'],))
        cursor.execute('INSERT OR IGNORE INTO Seasons (Name) VALUES (?)', (row['Season'],))  # Insert season
        cursor.execute('INSERT OR IGNORE INTO Teams (Name) VALUES (?)', (row['Team'],))

    conn.commit()

    # Insert players
    for _, row in player_df.iterrows():
        cursor.execute('''
            INSERT OR IGNORE INTO Players (Name, BirthYear, Nationality, Position, Age)
            VALUES (?, ?, ?, ?, ?)
        ''', (row['Player'], row['Birth Year'], row['Nationality'], row['Position'], row['Age']))

    conn.commit()

    # Insert team statistics
    for _, row in team_df.iterrows():
        cursor.execute('''
            INSERT OR IGNORE INTO TeamStatistics (
                League, Season, Team, PlayersUsed, AverageAge, Possession,
                MatchesPlayed, GamesStarted, MinutesPlayed, NinetyMinutesPlayed,
                Goals, Assists, GoalsPlusAssists, NonPenaltyGoals, PenaltyKickGoals,
                PenaltyKickAttempts, YellowCards, RedCards, ExpectedGoals,
                ExpectedNonPenaltyGoals, ExpectedAssistedGoals, ExpectedNonPenaltyAssistedGoals,
                ProgressiveCarries, ProgressivePasses
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            row['League'], row['Season'], row['Team'], row['Players Used'], row['Average Age'], row['Possession'],
            row['Matches Played'], row['Games Started'], row['Minutes Played'], row['90 Minutes Played'],
            row['Goals'], row['Assists'], row['Goals+Assists'], row['Non-Penalty Goals'],
            row['Penalty Kick Goals'], row['Penalty Kick Attempts'], row['Yellow Cards'],
            row['Red Cards'], row['Expected Goals'], row['Expected Non-Penalty Goals'],
            row['Expected Assisted Goals'], row['Expected Non-Penalty+Assisted Goals'],
            row['Progressive Carries'], row['Progressive Passes']
        ))

    conn.commit()

    # Insert player statistics
    for _, row in player_df.iterrows():
        cursor.execute('''
            INSERT OR IGNORE INTO PlayerStatistics (
                League, Season, Team, Player, BirthYear, MatchesPlayed, GamesStarted,
                MinutesPlayed, NinetyMinutesPlayed, Goals, Assists, GoalsPlusAssists,
                NonPenaltyGoals, PenaltyKickGoals, PenaltyKickAttempts, YellowCards,
                RedCards, ExpectedGoals, ExpectedNonPenaltyGoals, ExpectedAssistedGoals,
                ExpectedNonPenaltyAssistedGoals, ProgressiveCarries, ProgressivePasses,
                ProgressivePassesReceived
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            row['League'], row['Season'], row['Team'], row['Player'], row['Birth Year'],
            row['Matches Played'], row['Games Started'], row['Minutes Played'], row['90 Minutes Played'],
            row['Goals'], row['Assists'], row['Goals+Assists'], row['Non-Penalty Goals'],
            row['Penalty Kick Goals'], row['Penalty Kick Attempts'], row['Yellow Cards'],
            row['Red Cards'], row['Expected Goals'], row['Expected Non-Penalty Goals'],
            row['Expected Assisted Goals'], row['Expected Non-Penalty+Assisted Goals'],
            row['Progressive Carries'], row['Progressive Passes'], row['Progressive Passes Received']
        ))

    conn.commit()

# Main function
def main():
    create_tables()
    load_data()
    print("Database created and data loaded successfully!")

if __name__ == '__main__':
    main()