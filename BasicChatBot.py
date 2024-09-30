import random
greetings = ["Hello! How can I help you?", "Hi! What can I do for you?", "Hey! How can I mentor?"]
goodbyes = ["Goodbye!", "Bye! Take care!", "See you soon!"]
thanks_responses = ["You're welcome!", "No problem!", "Glad I could help!"]
default_response = ["I don't understand.", "Can you explain?", "I'm not sure what you mean."]
funny= ["\"why don\'t\' skeletons fight each other.\n Because they don\'t\' have guts "]
print("AI_interaction: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ").lower()
    
    if "hello" in user_input or "hi" in user_input:
        print("AI_interaction:", random.choice(greetings))
    elif "bye" in user_input:
        print("AI_interaction:", random.choice(goodbyes))
        break
    elif "thank" in user_input:
        print("AI_interaction:", random.choice(thanks_responses))
    elif "joke" in user_input:
        print("AI_interaction:",random.choice(funny))
    else:
        print("AI_interaction:", random.choice(default_response))
