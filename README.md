# How to run

## docker
今回はMysqlのみをコンテナにデプロイしています。
~~~
$ docker-compose build
$ docker-compose up -d
~~~

## マイグレーション
~~~
$ cd api
# 初期化
$ alembic revision --autogenerate -m ""
$ alembic upgrade +1
~~~

## python実行
~~~
$ cd api
# ライブラリのインストール
$ pip3 install -r requirements.txt
# run
$ python3 app.py
~~~