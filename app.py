# encoding: utf-8
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# you can replace by load env file
handler = WebhookHandler('389ce10ba891b591a20990c157d8f3bd') 
line_bot_api = LineBotApi('j+zMhs8S9AyS8G+ufT731SOvXRM/9ySEFrKfgW6+yvcFwBzcYdBLMe/ZDXWCGU+8s0VTiqywkXmBlOWCEdvZ46kPTqbEoe3uyW2A2KcG5ihOi8enMnM2g4+bWUsYDkkYDhbDr7kENWvFLvJFaji9BQdB04t89/1O/w1cDnyilFU=') 


@app.route('/')
def index():
    return "<p>Hello World!</p>"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


# ========== handle user message ==========
@handler.add(MessageEvent, message=TextMessage)  
def handle_text_message(event):
    # message from user                  
    msg = event.message.text

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=msg))


    


if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    # --- original code ---
    # arg_parser.add_argument('-p', '--port', type=int, default=8000, help='port')
    # arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    # options = arg_parser.parse_args()
    # app.run(debug=options.debug, port=options.port)
    
    # --- new code ---
    http_port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=http_port)
