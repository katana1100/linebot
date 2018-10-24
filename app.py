from flask import Flask, request, abort
import os
import sys
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import (
    MessageEvent, TextMessage,
    TextSendMessage,
    ImageSendMessage,
    TemplateSendMessage,
    ButtonsTemplate, ConfirmTemplate, CarouselTemplate,
    PostbackTemplateAction, MessageTemplateAction, URITemplateAction,
    CarouselColumn
)

app = Flask(__name__)

LINE_CHANNEL_ACCESS_TOKEN = 'fcpqJvbf0JbHmEWbUyzMKqwoe2rGrty1UZ6uG9SaAuRZO6P/CU5wuU/f/RR5SRQiwRtoaOaugFAFHEwjpoEDSg0NqI6fF0mLy+BYLsae1upv0LqjmDfWfdf/4q8Fy1bZLkBfya2uHjCImkfFpASPfAdB04t89/1O/w1cDnyilFU='
SECRET = '497bc40894efdc359bf439bdfc61d34f'

# Channel Access Token
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
# Channel Secret
handler = WebfromhookHandler(SECRET)


@app.route("/")
def hello_world():
    return "hello world!"


# 監聽所有來自 /callback 的 Post Request
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

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text='This is a rare pepe and feels post only in 100 000 posts. If u dont upvote this in 10 seconds you will have bad luck and suffer from the dank meme curse!')
    message2 = TextSendMessage(text=(event.source.user_id)) #reply userid
    image_url = 'https://i.imgur.com/bCBt6ga.jpg'
    message3 = ImageSendMessage(original_content_url=image_url, preview_image_url=image_url))
    line_bot_api.reply_message(event.reply_token, message)  

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
