import json
import boto3

client = boto3.client('lex-runtime')

def lambda_handler(event, context):
    
    print(event)
    print("abc")
    response = client.post_text(
        botName='DiningChatBot',
        botAlias='$LATEST',
        userId='admin',
        inputText=event["message"])
    #print("--------")
    #print(response)
    #print(response.message)
    inputText=event["message"]
    return {
        'statusCode': 200,
        'body': response#"Inside Lambda1" + inputText#response
    }