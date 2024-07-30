local HttpService = game:GetService("HttpService")
--Enter your API URL EXAMPLE: https://ABCDE.execute-api.us-east-2.amazonaws.com/prod/updateDB
local apiUrl = 

local DynamoDB = {}

function DynamoDB.write(items)
	local data = {
		action="WRITE",
		items = items
	}
	local jsonData = HttpService:JSONEncode(data)
	local response = HttpService:PostAsync(apiUrl, jsonData, Enum.HttpContentType.ApplicationJson)
	print(response)
end

function DynamoDB.read(userId)
	local data = {
		action="READ",
		ID=userId
	}
	local jsonData = HttpService:JSONEncode(data)
	local response = HttpService:PostAsync(apiUrl, jsonData, Enum.HttpContentType.ApplicationJson)
	local data = HttpService:JSONDecode(response)
	print(data["OrderDate"])
	return data.data
end

return DynamoDB
