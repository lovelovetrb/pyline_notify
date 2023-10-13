import functools
import platform
from datetime import datetime

import requests


def send(message, token):
    url = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": "Bearer " + token}
    payload = {"message": message}
    requests.post(url, headers=headers, params=payload)


def format_timedelta(timedelta):
    total_sec = timedelta.total_seconds()
    m, s = divmod(total_sec, 60)
    h, m = divmod(m, 60)
    fmt = f"{h:.0f}h {m:.0f}m {s:.0f}s"
    return fmt


def notify(token, debug=False):
    def _notify(func):
        @functools.wraps(func)
        def _wrapper(*args, **kwargs):
            if debug:
                return func(*args, **kwargs)
            start_time = datetime.now()
            start_time_fmt = start_time.strftime("%Y/%m/%d %H:%M:%S")
            send(
                f"\n\
                  \n{start_time_fmt}: Script Start🙌\
                  \nwatch func name -> {func.__name__}\
                  \nplatform -> {platform.platform(terse=True)} \
                  \n",
                token,
            )
            try:
                result = func(*args, **kwargs)
            except BaseException as e:
                end_time = datetime.now()
                send(
                    f"\n\
                     \nError has occured😿\
                     \nError code -> {str(e)}\
                     \nelapsed time -> {format_timedelta(end_time - start_time)}\
                     \n",
                    token,
                )
                raise e
            else:
                end_time = datetime.now()
                send(
                    f"\n\
                      \nCode Completed Successfully🫶\
                      \nelapsed time -> {format_timedelta(end_time - start_time)}\
                      \n",
                    token,
                )
            return result

        return _wrapper

    return _notify
