import tweepy
import os
from datetime import datetime
import pytz

# 環境変数からAPIキーを取得
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# OAuth 1.0a 認証で Twitter API に接続
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# 現在時刻（JST）
JST = pytz.timezone('Asia/Tokyo')
now = datetime.now(JST).strftime("%Y-%m-%d %H:%M:%S")

# ツイート内容
tweet_content = f"✅ Twitter API v1.1 でツイート！\n現在時刻: {now} JST"

# ツイートを投稿（API v1.1 を使用）
api.update_status(tweet_content)

# 投稿成功のログを表示
print("✅ 投稿完了:", tweet_content)
