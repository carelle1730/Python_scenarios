# Display the account numbers

aws_arn = "arn:aws:iam::123456789012:user/development/product_1234/*"

my_account_id = (aws_arn[13:25])

print(my_account_id)


