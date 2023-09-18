# from twilio.rest import Client

# account_sid = 'ACc3d9016c4e2b8238a5178a2f82be4269'
# auth_token = 'ee9740b99f61dadf524dfa64c6b24ff7'
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#   from_='whatsapp:+14155238886',
#   body='barrrrrrrr',
#   to='whatsapp:+972504414234'
# )

# print(message.sid)
# https://9759-94-188-166-126.ngrok.io

# from flask import Flask, request
# from twilio.twiml.messaging_response import MessagingResponse
# import io
# app = Flask(__name__)

# @app.route("/whatsapp", methods=['POST','GET'])
# def whatsapp_reply():
#     with io.open("media_url.txt","a",encoding="utf-8")as f1:
#         url = []
#         num = request.form.get("From")
#         num = num.replace("whatsapp:","")
#         msg_text = request.form.get("Body")
#         media_url = request.form.get("MediaUrl10")
#         url.append(media_url)
#         msg = MessagingResponse()
#         resp = msg.message("this image send by "+num)
#         resp.media(media_url)
#         f1.write(url[0]+"\n")
#         return (str(msg))

# if __name__ == "__main__":
#     app.run()

# from flask import Flask, request
# from twilio.twiml.messaging_response import MessagingResponse
# import io
# app = Flask(__name__)

# @app.route("/whatsapp", methods=['POST','GET'])
# def whatsapp_reply():
#     with io.open("media_url.txt","a",encoding="utf-8")as f1:
#         num = request.form.get("From")
#         print(num)
 

# if __name__ == "__main__":
#     app.run()

# from flask import Flask, request
# from twilio.twiml.messaging_response import MessagingResponse
# import requests

# app = Flask(__name__)

# @app.route("/whatsapp", methods=['POST','GET'])
# def whatsapp_reply():
#     print("Received a request from Twilio")

#     # יצירת תגובה להודעה שהתקבלה
#     resp = MessagingResponse().message("תמונה התקבלה")
#     print("noam")
#     # בדיקה אם ההודעה היא תמונה
#     if request.values.get('NumMedia') != '0':
#         # image_url = request.values.get('MediaUrl0')
        
#         # # הורדת התמונה
#         # image_data = requests.get(image_url).content
#         resp = MessagingResponse().message("heyy")
        
#         # כאן את יכולה לטפל בתמונה כפי שאת רוצה
#     else:
#         resp = MessagingResponse().message("noam123")
#     return str(resp)


# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5000, debug=True)

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests
import logging
import os

# הגדרת ה-logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route("/whatsapp", methods=['POST','GET'])
def whatsapp_reply():
    logging.info("Received a request from Twilio")

    # בדיקה אם ההודעה היא תמונה
    if request.values.get('NumMedia') != '0':
        image_url = request.values.get('MediaUrl0')
        logging.info(f"Image detected. Image URL: {image_url}")
        # logging.info("Image detected")

                # הורדת התמונה
        image_data = requests.get(image_url).content
        with open(os.path.join(os.path.expanduser('~'), 'Desktop', 'received_image.jpg'), 'wb') as f:
            f.write(image_data)
        logging.info("Image saved to Desktop")
    else:
        message_body = request.values.get('Body', 'No message content available')
        logging.info(f"No image detected. Message content: {message_body}")
        # logging.info("No image detected.")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

