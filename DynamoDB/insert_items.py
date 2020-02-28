import boto3
from botocore.exceptions import ClientError
# boto3 is the AWS SDK library for Python.
# The "resources" interface allow for a higher-level abstraction than the low-level client interface.
# More details here: http://boto3.readthedocs.io/en/latest/guide/resources.html
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('yelp-restaurants')

import requests
import json
from decimal import Decimal
import datetime


# Define a business ID
# business_id = '6wZ69a8haumqd5xRJQM6-A'

# Define the API key, Define the endpoint, and define the header
API_KEY = '4iI2XEZzHvBgStXyaWKc2KWq2C2LNL_BoXBX30B0q0_kqhhvDUCPUZjrPqVwKwjWVCLpFvu1D79-qq-dt1RgZDX70I4f4ERRwYvp4FF_4TNj28v-OomnHzhOtBhSXnYx'
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' % API_KEY}


cuisine_types = ['indian']

for cuisine_type in cuisine_types:
    offset = 0
    for i in range(0, 40):
        offset += 50
        PARAMETERS = {
            'term': 'restaurant',
            'location': 'New York',
            'radius': 40000,
            'categories': cuisine_type,
            'limit': 50,
            'offset': offset,
            'sort_by': 'best_match'
        }
        response = requests.get(url=ENDPOINT, params=PARAMETERS, headers=HEADERS)
        business_data = response.json()
        
        for biz in business_data['businesses']:
            try:
                table.put_item(
                    Item={
                        'businessId': biz['id'],
                        'name': biz['name'],
                        'category': biz['categories'][0]['alias'],
                        'address': biz['location']['address1'],
                        'city': biz['location']['city'],
                        'zipcode': biz['location']['zip_code'],
                        'latitude': Decimal(str(biz['coordinates']['latitude'])),
                        'longitude': Decimal(str(biz['coordinates']['longitude'])),
                        'reviewCount': biz['review_count'],
                        'rating': Decimal(str(biz['rating'])),
                        'insertedAtTimestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    },
                    ConditionExpression='attribute_not_exists(businessId) AND attribute_not_exists(insertedAtTimestamp)'
                )
            except ClientError as e:
                print(e.response['Error']['Code'])