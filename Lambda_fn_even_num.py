# Lambda function in even number
li = [1,2,3,4,5,6,7,8,9,10]
final_list = list(filter(lambda x:(x%2!=0),li))
print(final_list)