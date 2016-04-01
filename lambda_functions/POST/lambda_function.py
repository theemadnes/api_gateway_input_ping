## this function updates an item to a shopping cart (identified by cart_id)

from __future__ import print_function
import boto3
import json
import datetime

print('Loading function')

def lambda_handler(event, context):

    print('Dumping input: ' + json.dumps(event)) # print out the contents of the event sent to the lambda function

    # add timestamp to event
    event['time_stamp'] = datetime.datetime.isoformat(datetime.datetime.now())

    return event
