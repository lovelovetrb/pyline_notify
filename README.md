# pyline-notify

Python で書かれたスクリプトにたった 2 行追加することで、Python スクリプトの開始と終了を通知してくれるライブラリです。

機械学習などの時間のかかるコードを実行する際に追加しておくことで、スクリプトの終了やエラーをいち早く検知することができます。

## 必要なもの

- LINE アカウント
- LINE Notify のアクセストークン

## 使い方

1. [LINE Notify のページ](https://notify-bot.line.me/my/)にアクセスし、ログイン後アクセストークンを取得します。
2. お使いの Python パッケージ管理ツールで `pyline-notify` をインストールします。

   pip

   ```
   pip install git+https://github.com/lovelovetrb/pyline_notify
   ```

   rye

   ```
   rye add pyline-notify --git=https://github.com/lovelovetrb/pyline_notify
   ```

   poetry(未検証)
   ```
   poetry add git+https://github.com/lovelovetrb/pyline_notify
   ```

3. LINE 通知を行いたいスクリプトで`pyline-notify`をインポートして、デコレーターをつけます。
4. スクリプトの開始と終了時にご自身の LINE アカウントに通知が飛びます！

## wiki

使い方は[サンプルコード](./demo)をご覧下さい。

## このスクリプトに関する記事

参考にさせていただいたもの、作成の動機などをまとめています。

[Zenn](https://zenn.dev/misora/articles/8853137fd74212)

## LICENSE

[MIT LICENSE](./LICENSE)

## Auther

RISUman

mail: mbaba@kanolab.com

[Twitter](https://twitter.com/lovelovetrb)
