# First, we import the openai library
import openai

# Next, we create an instance of the ChatGPT class
chatbot = openai.ChatGPT()

# Now we can use the generate function to generate text based on a prompt
# In this example, we are asking the chatbot to tell us a joke
response = chatbot.generate(prompt="Tell me a joke.", max_tokens=100, stop_sequence="\n")

# Finally, we print the response
print(response)

