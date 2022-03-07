from datetime import datetime


def get_date(stamp):
    if len(str(stamp)) == 13:
        dt_object = datetime.fromtimestamp(int(stamp) / 1000)
    else:
        dt_object = datetime.fromtimestamp(int(stamp))

    return dt_object.strftime("%Y-%m-%d %H:%M:%S")
