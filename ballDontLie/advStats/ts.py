# True shooting percentage

__all__ = ['calc_ts']

def calc_ts(pts, fga, fta):
    """
    Parameters
    ---------
    pts : points scored
    fga : field goal attempts
    fta : free throw attempts
    """
    return pts / ( 2 * (fga + (0.44*fta)))
