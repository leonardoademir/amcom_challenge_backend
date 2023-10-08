days_week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]


def check_day_week(pk, day_week):
    if day_week not in days_week:
        return {
            "sucess": False,
            "data": "Error: Day week must be one of the following: MON, TUE, WED, THU, FRI, SAT, SUN.",
        }

    if int(pk) != days_week.index(day_week) + 1:
        return {"sucess": False, "data": "Error: Index of specific day wrong."}

    return {"sucess": True, "data": ""}
