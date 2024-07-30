# RobloxToDynamoDB
How to hook up your roblox games to Dynamo DB using a Lambda function, API Gateway, lua, and a DynamoDB table

Steps:
First, log into AWS as root user. If you don't have an account, you have to create one to access these services

Database Table Creation
--------------------------------
1. Log into AWS as root user.
2. Click the search bar and type DynamoDB
3. Click tables on the left hand bar
4. Click create table
5. Enter your table name, partition key [Remember table name]
(Partition key is a main key, so if you're saving user data you might want to use their UserID)
6. Leave the sort key alone
7. I left it with default settings and then created the table
--------------------------------

Lambda Code Setup
--------------------------------
1. Log into AWS as root user.
2. Click the search bar and type Lambda
3. Click create function
4. Enter whatever function name you want, just make sure you remember it later.
5. Click the runtime dropdown and select python. My AWS Lambda function is in Python.
6. I left the architecture as x86_64, and the execution role as "Create a new role with basic lambda permission"
7. Go to the code source, and paste the code from box 1 in.
8. On this line table = dynamodb.Table('Test') change 'Test' to be whatever database name you decided on in Database Table Creation step 5
9. Next go to the IAM console https://console.aws.amazon.com/iam/
10. Click roles on the left side
11. Under permission policies search AmazonDynamoDBFullAccess and add it, now your lambda function has access to write to your DynamoDB tables
--------------------------------

Api Gateway Setup
--------------------------------
1. Log into AWS as root user.
2. Click the search bar and type API Gateway
3. Click Create API
4. Click build under Http API
5. Click the integrations dropdown and select Lambda
6. Then in the bar with the magnifying glass, choose your lambda function
7. You can leave the method as any and click next, make sure your lambda function is chosen under integration target
8. You can leave the stage name as default and click deploy
9. Then on the left hand side under API gateway, you can click something that looks like API: apiName...(abcde123)
10. There you can find your link, which you will add to the lua script 
local apiUrl = "https://ABCDE.execute-api.us-east-2.amazonaws.com/prod/updateDB"
--------------------------------

Game implementation
--------------------------------
1. Create a module script inside serverscriptservice or wherever you want to put it
2. Paste the module script code
3. Be sure to turn on API calls in the game settings
4. Create a regular script in serverscriptservice that calls it like this: local DynamoDB = require( game.ServerScriptService.DynamoDB)
5. Test it by writing and then reading an entry like so (here my primary key name was ID):
local info = {
	{ID = "123", OrderID = "samsamsam1", OrderDate = "2024-07-01", OrderTotal = 200}
}

DynamoDB.write(info)
DynamoDB.read("123") --123 is the primary key
