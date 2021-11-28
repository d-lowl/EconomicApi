def get_downsides(daily_profits: list) -> list:
    """return array of prices, but replacing positive profits with 0"""

    downsides = []
    for el in daily_profits:
        if el["profit"] < 0:
            downsides.append({"time": el["time"], "profit": el["profit"]})
        else:
            downsides.append({"time": el["time"], "profit": 0})

    return downsides

