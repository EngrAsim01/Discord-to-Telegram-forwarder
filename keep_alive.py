# This is flask app that you need to use with your code if you want to run your code 24/7
# You can run your code 24/7 in replit....

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
  return "Your bot is alive!"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()
