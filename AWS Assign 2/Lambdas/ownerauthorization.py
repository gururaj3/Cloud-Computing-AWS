import json
import boto3
import random as r
import logging
import time
def lambda_handler(event, context):
    # TODO implement
    print(event)
    print(event['phonenumber'])
    print(event['name'])
    print("fid:", event['faceid'])
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('visitors')
    authorization_link="http://otpauthorization.s3-website-us-east-1.amazonaws.com"
    response = table.get_item(
                        TableName='visitors',
                        Key={
                            'faceId': event['faceid']
                            }
                    )
    my_visitor_entry = {'faceId' : event['faceid'], 'name' : event['name'] , 'phoneNumber' : event['phonenumber'] , "photos": [
    {
      "bucket": "bucketforvisitors",
      "createdTimestamp": "Apr 14, 2020 4:29:100",
      "objectKey": "frame.jpg"
    }
  ]}
    table.put_item(Item=my_visitor_entry)
    otp=""
    for i in range(4):
        otp+=str(r.randint(1,9))
    dynamo_passcodes_table = dynamodb.Table("passcodes")
    my_string = {'faceId' : event["faceid"], 'otp': otp, 'expiration' : str(int(time.time() + 300))}
    dynamo_passcodes_table.put_item(Item=my_string)
    mobile=event["phonenumber"]
    msg='Hi, here is your otp. Enter this and you can go through the front door! : ' +otp + ' Please enter the otp here ' + authorization_link
    sns = boto3.client('sns')
    print("msg:", msg)
    response = sns.publish(
        PhoneNumber=mobile,
        Message=msg # this should include link to submit visitor info
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
