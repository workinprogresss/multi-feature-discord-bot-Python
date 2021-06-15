from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
  return "Your bot is alive!"

def run():
    app.run(host="127.0.0.1", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()