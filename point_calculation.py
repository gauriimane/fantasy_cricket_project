"""
This file contains code to calculate the points for a player according to the
rules given in the problem statement file.
"""

import sqlite3


def get_team_score(team):
    """
    This function takes in the names of players of a team as a list and
    returns their scores (points) in a list.

    Parameters
    ----------
    team : list
        Names of players of the team.

    Returns
    -------
    scores : list
        List of scores of players in list team.

    """
    game = sqlite3.connect('player_database.db')
    cur = game.cursor()
    scores = []
    for i in team:
        player_name = i
        # Access database and get stats of the player
        command = "SELECT * FROM match WHERE player = '{}';".format(player_name)
        stats = []
        cur.execute(command)
        record = cur.fetchall()
        for i in record[0]:
            stats.append(i)
        stats.remove('{}'.format(player_name))
        scores.append(score(stats))
    game.close()
    return scores


def score(player_stat):
    """
    This function takes in the player stats in the form of a list and outputs
    the player score according to the rules mentioned in the problem statement.

    Parameters
    ----------
    player_stat : list
        List of player stats.

    Returns
    -------
    score : int
        Score (points) of player accordint to the rules.

    """
    score = 0
    score += player_stat[0] // 2
    if player_stat[0] >= 100:
        score += 15
    elif player_stat[0] >= 50:
        score += 5
    try:
        strike = player_stat[0] / player_stat[1] * 100
        if strike > 100:
            score += 6
        elif strike > 80:
            score += 2
    except:
        pass
    score += player_stat[2] + player_stat[3] * 2
    score += player_stat[7] * 10
    if player_stat[7] >= 5:
        score += 15
    elif player_stat[7] >= 3:
        score += 5
    try:
        economy = player_stat[6] / (player_stat[4] / 6)
        if economy < 2:
            score += 10
        elif economy < 3.5:
            score += 7
        elif economy < 4.5:
            score += 4
    except:
        pass
    score += 10 * (player_stat[8] + player_stat[9] + player_stat[10])
    return score
