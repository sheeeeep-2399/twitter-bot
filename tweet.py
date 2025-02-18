import tweepy
import os
import random
from datetime import datetime
import pytz

# 環境変数から API キーを取得
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")  # API v2 に必要

# 認証（API v2）
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# 現在時刻（JST）
JST = pytz.timezone('Asia/Tokyo')
now = datetime.now(JST)
date_str = now.strftime("%m月%d日").lstrip("0")  # 0埋めを削除

# ランダムツイートリスト（通常の日用）
random_tweets = [
    "愛してるぞ月ノ美兎",
    "愛してるぞ月ノ美兎",
    "愛してるぞ月ノ美兎",
    "愛してるぞ月ノ美兎",
    "愛してるぞ月ノ美兎",
    "愛してるぞ月ノ美兎",
    "愛してるぞ月ノ美兎",
    "愛してるぞ月ノ美兎",
    "愛してるぞ月ノ美兎",
    "愛してるぞ月ノ美兎",
    "かわいいぞ月ノ美兎",
    "おもしろいぞ月ノ美兎",
]

tweet_content = random.choice(random_tweets) + "\n" + f"{date_str}" # ランダムツイート

# ツイートを投稿
response = client.create_tweet(text=tweet_content)

# 投稿成功のログを表示
print(f"✅ 投稿完了: {tweet_content}")
