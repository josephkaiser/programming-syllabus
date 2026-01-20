# DEFAULT_MESSAGE = "Tell me something, and I will repeat it back to you: "
# HIDDEN_MESSAGE = "return"
#
# message = DEFAULT_MESSAGE
# message = input(message)
# if message == HIDDEN_MESSAGE:
#     while message == HIDDEN_MESSAGE:
#         message = input(DEFAULT_MESSAGE)
#         print(message)
# print(message)

# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

user_prompt = "\nUser:\t\t\t"
agent_prompt = "\nChat:\t"

active = True # Flag
while active:

    user_query = input(user_prompt)
    if user_query == 'quit':
        active = False # Exit
    else:
        # Add function to call vllm chat response with user_query string
        print(agent_prompt +"\t\t" + user_query)
