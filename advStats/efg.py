# Effective field goal percentage

__all__ = ['calc_efg']

def calc_efg(fg, tp, fga):
    """
    Parameters
    ----------
    fg : field goals made
    tp : 3-point field goals made
    fga : field goal attempts

    """
    return (fg + (0.5*tp))/fga
