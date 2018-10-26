from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Test")

conv = [
    "Ola",
    "kk eae man",
    "opa eai blz",
    "Tudo bem?",
    "Tudo e você?",
    "Na boa. Que tipo de música você gosta?",
    "Eu gosto de funk.",
    "kkk favelado.",
    "política",
    "ciro gomes",
    "inflação",
    "bolsonaro",
    "MITOOO",
]

chatbot = ChatBot(
    "Test",
    filters=["chatterbot.filters.RepetitiveResponseFilter"]
)

chatbot.set_trainer(ListTrainer)
chatbot.train(conv)

while True:
	msg = input("Você: ")
	response = chatbot.get_response(msg)
	print("Bot: ", response)