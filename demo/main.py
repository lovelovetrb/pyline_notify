import os
from time import sleep

from dotenv import load_dotenv

from pyline_notify import notify

load_dotenv()


# @notify をつけると、関数の実行状況が LINE に通知されます。
# 引数には LINE Notify のトークンを指定します。
# debug=True でデバッグモードになり、LINE に通知されないようになります。
@notify(os.getenv("LINE_TOKEN"), debug=False)
def main():
    print("Hello, world!")
    sleep(3)
    # raise Exception("Error!")


if __name__ == "__main__":
    main()
