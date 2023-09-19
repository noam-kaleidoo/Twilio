# import os
# import requests
# from flask import Flask, request
# from twilio.twiml.messaging_response import MessagingResponse
# from google.cloud import storage
# import logging

# # Setting up logging to capture and display informational messages
# logging.basicConfig(level=logging.INFO)

# # Authenticate with Google Cloud Storage using the default service account
# storage_client = storage.Client()
# bucket_name = 'me-west1-test-bd0df372-bucket'  # Name of the Google Cloud Storage bucket
# bucket = storage_client.bucket(bucket_name)

# app = Flask(__name__)

# # Function to generate a Twilio response message
# def respond(message):
#     response = MessagingResponse()
#     response.message(message)
#     return str(response)

# @app.route("/whatsapp", methods=['POST','GET'])
# def whatsapp_reply():
#     logging.info("Received a request from Twilio")

#     # Extract sender information and message content from the request
#     sender = request.values.get('From')
#     message = request.values.get('Body')
#     media_url = request.values.get('MediaUrl0')
    
#     # Check if the incoming message contains a media URL (e.g., an image)
#     if media_url:
#         # Fetch the media content using Twilio credentials for authentication
#         r = requests.get(media_url, auth=(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN']))
#         content_type = r.headers['Content-Type']
#         # Extract the sender's phone number (without the "whatsapp:" prefix)
#         username = sender.split(':')[1]
        
#         # Determine the file type and set the filename accordingly
#         if content_type == 'image/jpeg':
#             filename = f'uploads/{username}/{message}.jpg'
#         elif content_type == 'image/png':
#             filename = f'uploads/{username}/{message}.png'
#         elif content_type == 'image/gif':
#             filename = f'uploads/{username}/{message}.gif'
#         else:
#             filename = None
        
#         # If a valid filename is set, upload the image directly to Google Cloud Storage
#         if filename:
#             blob = bucket.blob(filename)
#             blob.upload_from_string(r.content, content_type=content_type)
#             logging.info("Image saved to Google Cloud Storage bucket")
            
#             return respond('Thank you! Your image was received.')
#         else:
#             return respond('The file that you submitted is not a supported image type.')
#     else:
#         # If no media is attached, send a response asking for an image
#         return respond('Please send an image!')

# # Run the Flask app
# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5000, debug=True)


import datetime
import os
import requests
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from google.cloud import storage
import logging

# Setting up logging to capture and display informational messages
logging.basicConfig(level=logging.INFO)

# Authenticate with Google Cloud Storage using the default service account
storage_client = storage.Client()
bucket_name = 'me-west1-test-bd0df372-bucket'  # Name of the Google Cloud Storage bucket
bucket = storage_client.bucket(bucket_name)

app = Flask(__name__)

# Function to generate a Twilio response message
def respond(message):
    response = MessagingResponse()
    response.message(message)
    return str(response)

@app.route("/whatsapp", methods=['POST','GET'])
def whatsapp_reply():
    logging.info("Received a request from Twilio")

    # Extract sender information and message content from the request
    sender = request.values.get('From')
    message = request.values.get('Body')
    media_url = request.values.get('MediaUrl0')
    
    # Check if the incoming message contains a media URL (e.g., an image)
    if media_url:
        # Fetch the media content using Twilio credentials for authentication
        r = requests.get(media_url, auth=(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN']))
        content_type = r.headers['Content-Type']

        logging.info(f"Content Type: {content_type}")
        logging.info(f"Message: {message}")
        # Extract the sender's phone number (without the "whatsapp:" prefix)
        username = sender.split(':')[1]
        
        # Determine the file type and set the filename accordingly
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        if content_type == 'image/jpeg':
            filename = f'uploads/{username}/{message}_{timestamp}.jpg'
        elif content_type == 'image/png':
            filename = f'uploads/{username}/{message}_{timestamp}.png'
        elif content_type == 'image/gif':
            filename = f'uploads/{username}/{message}_{timestamp}.gif'
        elif content_type == 'image/webp':
            filename = f'uploads/{username}/{message}_{timestamp}.webp'
        elif content_type == 'video/mp4':
            filename = f'uploads/{username}/{message}_{timestamp}.mp4'
        else:
            filename = None
        
        # If a valid filename is set, upload the image directly to Google Cloud Storage
        if filename:
            blob = bucket.blob(filename)
            blob.upload_from_string(r.content, content_type=content_type)
            logging.info("Image saved to Google Cloud Storage bucket")
            
            return respond('Thank you! Your image was received.')
        else:
            return respond('The file that you submitted is not a supported image type.')
    else:
        # If no media is attached, send a response asking for an image
        return respond('Please send an image!')

# Run the Flask app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)





