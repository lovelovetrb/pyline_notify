import functools
import os
import platform
from datetime import datetime

import __main__
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


def notify(
    token,
    debug=False,
    project_name="",
):
    def _notify(func):
        @functools.wraps(func)
        def _wrapper(*args, **kwargs):
            new_project_name = project_name
            if new_project_name == "":
                new_project_name = (
                    f"{os.path.basename(__main__.__file__)} {func.__name__}"
                )

            if debug:
                try:
                    result = func(*args, **kwargs)
                except BaseException as e:
                    send(
                        f"\nError has occured😿\nError code -> {str(e)}\nproject Name -> {new_project_name}",
                        token,
                    )
                    raise e
                return result

            start_time = datetime.now()
            start_time_fmt = start_time.strftime("%Y/%m/%d %H:%M:%S")

            send(
                f"\
                  \n{start_time_fmt}: Script Start🙌\
                  \nProject Name -> {new_project_name}\
                  \nplatform -> {platform.platform(terse=True)} \
                  \n",
                token,
            )

            try:
                result = func(*args, **kwargs)
            except BaseException as e:
                end_time = datetime.now()
                send(
                    f"\
                     \nError has occured😿\
                     \nProject Name -> {new_project_name}\
                     \nError code -> {str(e)}\
                     \nelapsed time -> {format_timedelta(end_time - start_time)}\
                     \n",
                    token,
                )
                raise e
            else:
                end_time = datetime.now()
                send(
                    f"\
                      \nCode Completed Successfully🫶\
                      \nProject Name -> {new_project_name}\
                      \nelapsed time -> {format_timedelta(end_time - start_time)}\
                      \n",
                    token,
                )
            return result

        return _wrapper

    return _notify
