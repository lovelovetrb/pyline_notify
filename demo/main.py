import os
from time import sleep

from dotenv import load_dotenv

from pyline_notify import notify

load_dotenv()

token = os.getenv("LINE_TOKEN")


# @notify デコレーターをつけると、関数の実行状況が LINE に通知されます。
# 通知されるのは、関数の実行開始と終了、エラー発生時です。
# 引数には LINE Notify のトークンを指定します。
# debug=True でデバッグモードになり、LINE に通知されないようになります。
# project_name でプロジェクト名を指定できます。
# デフォルトでは、ファイル名と監視対象の関数名がプロジェクト名になります。


@notify(token, debug=False, project_name="test")
def main():
    print("Hello, world!")
    sleep(3)
    # raise Exception("Error!")


if __name__ == "__main__":
    main()
