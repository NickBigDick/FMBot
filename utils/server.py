"""
from flask import Flask, request, abort
import telebot
from loader import bot
app = Flask(__name__)


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    bot.send_message(869223233, username)
    return f'User {username}'


@app.route('/', methods=['POST'])
def webhook():
    if request.method == 'POST':
        json = request.json
        bot.send_message(869223233, json["result"])
        print(json["result"])
        return 'suc', 200
    else:
        abort(400)


# чистый код
# @app.route('/webhook', methods=['POST'])
# def webhook():
#     if request.method == 'POST':
#         json = request.json
#         file = js.loads(json)
#         print(file)
#         return 'suc', 200
#     else:
#         abort(400)



if __name__ == '__main__':
    app.run()
"""

import os
import telebot
from flask import Flask, request
from loader import bot

server = Flask(__name__)

@server.route(f"/", methods=["POST"])
def refirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


if __name__ == "__main__":
    bot.remove_webhook()
    # bot.set_webhook("http://92.255.67.180")
    bot.set_webhook("https://127.0.0.1:8443")
    # server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8443)))

