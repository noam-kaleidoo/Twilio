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

# from flask import Flask, request
# from twilio.twiml.messaging_response import MessagingResponse
# import requests
# import logging
# import os

# # הגדרת ה-logging
# logging.basicConfig(level=logging.INFO)

# app = Flask(__name__)

# @app.route("/whatsapp", methods=['POST','GET'])
# def whatsapp_reply():
#     logging.info("Received a request from Twilio")

#     # בדיקה אם ההודעה היא תמונה
#     if request.values.get('NumMedia') != '0':
#         image_url = request.values.get('MediaUrl0')
#         logging.info(f"Image detected. Image URL: {image_url}")
#         # logging.info("Image detected")

#                 # הורדת התמונה
#         image_data = requests.get(image_url).content
#         with open('received_image.jpg', 'wb') as f:            
#             f.write(image_data)
#         logging.info("Image saved to Desktop")
#     else:
#         message_body = request.values.get('Body', 'No message content available')
#         logging.info(f"No image detected. Message content: {message_body}")
#         # logging.info("No image detected.")

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5000, debug=True)

# from flask import Flask, request
# from twilio.twiml.messaging_response import MessagingResponse
# import requests
# import logging
# from google.cloud import storage

# # Setting up logging
# logging.basicConfig(level=logging.INFO)

# # Authenticate with Google Cloud Storage using the default service account
# storage_client = storage.Client()
# bucket_name = 'me-west1-test-bd0df372-bucket'  # Replace with your bucket name
# bucket = storage_client.bucket(bucket_name)

# app = Flask(__name__)

# @app.route("/whatsapp", methods=['POST','GET'])
# def whatsapp_reply():
#     logging.info("Received a request from Twilio")

#     # Check if the message is an image
#     if request.values.get('NumMedia') != '0':
#         image_url = request.values.get('MediaUrl0')
#         logging.info(f"Image detected. Image URL: {image_url}")

#         # Download the image
#         image_data = requests.get(image_url).content
#         blob = bucket.blob('received_image.jpeg')  # File name in the bucket
#         blob.upload_from_string(image_data, content_type='jpeg')
#         logging.info("Image saved to Google Cloud Storage bucket")
#     else:
#         message_body = request.values.get('Body', 'No message content available')
#         logging.info(f"No image detected. Message content: {message_body}")

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5000, debug=True)

# from flask import Flask, request
# from twilio.twiml.messaging_response import MessagingResponse
# import requests
# import logging
# from google.cloud import storage

# # Setting up logging
# logging.basicConfig(level=logging.INFO)

# # Authenticate with Google Cloud Storage using the default service account
# storage_client = storage.Client()
# bucket_name = 'me-west1-test-bd0df372-bucket'  # Replace with your bucket name
# bucket = storage_client.bucket(bucket_name)

# # Twilio authentication details
# TWILIO_USERNAME = 'ACc3d9016c4e2b8238a5178a2f82be4269'
# TWILIO_PASSWORD = '3d74cff74d0784f7688c7e74db58d23c'

# app = Flask(__name__)

# @app.route("/whatsapp", methods=['POST','GET'])
# def whatsapp_reply():
#     logging.info("Received a request from Twilio")

#     # Check if the message is an image
#     if request.values.get('NumMedia') != '0':
#         image_url = request.values.get('MediaUrl0')
#         logging.info(f"Image detected. Image URL: {image_url}")

#         # Download the image with authentication
#         image_data = requests.get(image_url, auth=(TWILIO_USERNAME, TWILIO_PASSWORD)).content
#         blob = bucket.blob('received_image.jpeg')  # File name in the bucket
#         blob.upload_from_string(image_data, content_type='jpeg')
#         logging.info("Image saved to Google Cloud Storage bucket")
#     else:
#         message_body = request.values.get('Body', 'No message content available')
#         logging.info(f"No image detected. Message content: {message_body}")

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5000, debug=True)

# import os
# from twilio.rest import Client
# from flask import Flask, request
# from twilio.twiml.messaging_response import MessagingResponse
# import requests
# import logging
# from google.cloud import storage

# # Setting up logging
# logging.basicConfig(level=logging.INFO)

# # Authenticate with Google Cloud Storage using the default service account
# storage_client = storage.Client()
# bucket_name = 'me-west1-test-bd0df372-bucket'
# bucket = storage_client.bucket(bucket_name)

# # Twilio authentication and API key creation
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
# client = Client(account_sid, auth_token)
# # new_key = client.new_keys.create(friendly_name='User Joey')
# # TWILIO_USERNAME = new_key.sid
# # TWILIO_PASSWORD = new_key.secret  # Assuming the secret is accessible this way


# app = Flask(__name__)

# @app.route("/whatsapp", methods=['POST','GET'])
# def whatsapp_reply():
#     logging.info("Received a request from Twilio")

#     # Check if the message is an image
#     if request.values.get('NumMedia') != '0':
#         image_url = request.values.get('MediaUrl0')
#         logging.info(f"Image detected. Image URL: {image_url}")

#         # Download the image with authentication
#         image_data = requests.get(image_url, auth=(account_sid, auth_token)).content
#         blob = bucket.blob('received_image.jpeg')  # File name in the bucket
#         blob.upload_from_string(image_data, content_type='jpeg')
#         logging.info("Image saved to Google Cloud Storage bucket")
#     else:
#         message_body = request.values.get('Body', 'No message content available')
#         logging.info(f"No image detected. Message content: {message_body}")

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5000, debug=True)

import os
import requests
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from google.cloud import storage
import logging

# Setting up logging
logging.basicConfig(level=logging.INFO)

# Authenticate with Google Cloud Storage using the default service account
storage_client = storage.Client()
bucket_name = 'me-west1-test-bd0df372-bucket'
bucket = storage_client.bucket(bucket_name)

app = Flask(__name__)

def respond(message):
    response = MessagingResponse()
    response.message(message)
    return str(response)

@app.route("/whatsapp", methods=['POST','GET'])
def whatsapp_reply():
    logging.info("Received a request from Twilio")

    sender = request.values.get('From')
    message = request.values.get('Body')
    media_url = request.values.get('MediaUrl0')
    
    if media_url:
        r = requests.get(media_url, auth=(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN']))
        content_type = r.headers['Content-Type']
        username = sender.split(':')[1]  # remove the whatsapp: prefix from the number
        
        if content_type == 'image/jpeg':
            filename = f'uploads/{username}/{message}.jpg'
        elif content_type == 'image/png':
            filename = f'uploads/{username}/{message}.png'
        elif content_type == 'image/gif':
            filename = f'uploads/{username}/{message}.gif'
        else:
            filename = None
        
        if filename:
            # Upload directly to Google Cloud Storage
            blob = bucket.blob(filename)
            blob.upload_from_string(r.content, content_type=content_type)
            logging.info("Image saved to Google Cloud Storage bucket")
            
            return respond('Thank you! Your image was received.')
        else:
            return respond('The file that you submitted is not a supported image type.')
    else:
        return respond('Please send an image!')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)





