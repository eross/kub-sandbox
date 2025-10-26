def handle(event, context):
    return {
        "statusCode": 200,
        "body": "{context}Hello from OpenFaaS!"
    }
