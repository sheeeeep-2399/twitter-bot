import tweepy
import os
from datetime import datetime
import pytz

# 環境変数からAPIキーを取得
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# 認証処理
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# 現在時刻（JST）
JST = pytz.timezone('Asia/Tokyo')
now = datetime.now(JST).strftime("%Y-%m-%d %H:%M:%S")

# ツイート内容
tweet_content = f"✅ 毎日 JST 0:00 に自動投稿\n現在時刻: {now} JST"

# ツイートを投稿
api.update_status(tweet_content)
print("✅ 投稿完了:", tweet_content)