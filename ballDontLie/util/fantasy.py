def compute_fantasy_points(df, fp_fgm=1, fp_fga=-1, fp_ftm=1, fp_fta=-1, 
                            fp_reb=1, fp_ast=1,
                          fp_stl=1, fp_blk=1, fp_pts=1):
    """ Compute fantasy points for various metrics """
    df['FP'] = (fp_fgm*df['FGM']) + (fp_fga*df['FGA']) + (fp_ftm*df['FTM']) \
                + (fp_fta*df['FTA']) + (fp_reb*df['REB']) + (fp_ast*df['AST']) \
                + (fp_stl*df['STL']) + (fp_blk*df['BLK']) + (fp_pts*df['PTS'])
    return df
