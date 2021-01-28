user_input = input("Type your email here: ")
# ref = user_input.index('@')
# email_name = user_input[0:ref:1]
# domain_name = user_input[ref+1::1]
# print(email_name); print(domain_name)
print(user_input.split('@')[0])
print(user_input.split("@")[1])

