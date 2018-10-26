from chatterbot import ChatBot
chatbot = ChatBot("Ron Obvious")

from chatterbot.trainers import ListTrainer

conversation = [
    "Ola",
    "oi!",
    "Tudo bem?",
    "Tudo e você?",
    "Na boa. Que tipo de música você gosta?",
    "Eu gosto de funk.",
    "kkk favelado."
]

chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)

while True:
	quest = input("Você: ")
	response = chatbot.get_response("Good morning!")
	print("Bot: ", response)