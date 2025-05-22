import json
import boto3
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize the SES client
ses = boto3.client('ses', region_name='us-west-1') 

def lambda_handler(event, context):
    try:
        data = json.loads(event['body'])
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')

        if not name or not email or not message:
            return {
                "statusCode": 400,
                "headers": {
                    "Access-Control-Allow-Origin": "*"
                },
                "body": json.dumps({"error": "Missing required fields"})
            }

        logger.info(f"Form submitted by: {name} <{email}>")
        logger.info(f"Message content: {message}")

        response = ses.send_email(
            Source="prakritishakya1168@gmail.com",  # Must be verified in SES
            Destination={
                "ToAddresses": ["prakritishakya1168@gmail.com"]  # Must also be verified in sandbox
            },
            Message={
                "Subject": {
                    "Data": f"New Contact Form Message from {name}"
                },
                "Body": {
                    "Text": {
                        "Data": f"You have a new contact form submission:\n\nName: {name}\nEmail: {email}\nMessage:\n{message}"
                    }
                }
            }
        )

        logger.info(f"SES sendEmail response: {response}")

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"message": "Email sent successfully!"})
        }

    except Exception as e:
        logger.error("Error sending email", exc_info=True)
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"error": "Internal Server Error"})
        }
