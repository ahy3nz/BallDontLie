from nba_api.stats.static import teams, players
from nba_api.stats.endpoints import shotchartdetail, playercareerstats, playergamelog
#### A collection of utility functions for using nba_api

def find_player_id(player_name):
    all_players = players.get_players()
    found = [a['id'] for a in all_players if a['full_name']==player_name]
    return found

def get_player_season_gamelog(player_id, season_id):
    """ For a given player and given season, get the game-by-game log

    Returns pd.DataFrame"""
    gamelog = playergamelog.PlayerGameLog(player_id=player_id, season=season_id)
    return gamelog.player_game_log.get_data_frame()

def compile_player_gamelog(player_id, seasons):
    """ For a given player and list of seasons, compile all the game-by-game logs

    Returns pd.DataFrame"""
    df = get_player_season_gamelog(player_id, seasons[0])
    for season in seasons[1:]:
        df = df.append(get_player_season_gamelog(player_id, season))
    return df
