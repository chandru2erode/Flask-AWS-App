import boto3

db = boto3.resource('dynamodb', region_name='ap-south-1')
table = db.Table('signuptable')


# get item
response = table.get_item(Key={'email':'chandrakumar3108@gmail.com'})
print(response['Item'])

# insert item
table.put_item(
    Item={
        'email': 'jane@doe.com',
        'first_name': 'jane',
        'last_name': 'doe',
        'age': 25
    }
)

# update item
table.update_item(
    Key={'email': 'jane@doe.com'},
    UpdateExpression='SET age = :val',
    ExpressionAttributeValues={':val':16}
)

# delete item
table.delete_item(Key={'email':'hara@test.com'})