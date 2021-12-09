import os
from config import *
from starter import *

server = Flask(__name__)

def send_response(user_id, msg):
    bot.send_message(
        user_id,
        msg
    )

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/start")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=SERVER_URL + TOKEN)
    return "Tele-Escrow Bot Active!", 200


if DEBUG != True:
    server.run(host="0.0.0.0", threaded=True, port=int(os.environ.get('PORT', 5000)))
else:
    bot.remove_webhook()
    
    print("Bot polling!")
    bot.polling(none_stop=True)