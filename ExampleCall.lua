local DynamoDB = require( game.ServerScriptService.DynamoDB)
-- Example usage
local info = {
	{ID = "123", OrderID = "samsamsam1", OrderDate = "2024-07-01", OrderTotal = 200}
}

DynamoDB.write(info)
DynamoDB.read("123")
