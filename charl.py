from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('Charlotte')
trainer = ListTrainer(chatbot)
	
def treinando():

	chatbot = ChatBot('Ron Obvious',
        logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Desculpe, mas ainda não sou capaz de responder esta questão.',
            'maximum_similarity_threshold': 0.80
        }
])
	
# change to change the training
	trainer.train([
		"Como posso te ajudar?",
		"Deseja efetuar alguam operação?",
		"sim senhor",
		"sim senhora"
	])

	trainer.train("chatterbot.corpus.portuguese")
	trainer.train("chatterbot.corpus.english")

def conversar(frase):
	response = chatbot.get_response(frase)
	return response

# code for chatterbot without graphical input bellow
#print("Charlotte, oi, me chamo charlotte. Como posso ajuda-lo? Diga sair para encerrar a conversa")
#frase = input("Eu - ")
#while frase.find("sair") < 0 and frase.find("SAIR") < 0:
#    print(frase)
#    response = chatbot.get_response(frase)
#    print("Chalotte - ",response)
#    frase = input("Eu - ")

#response = chatbot.get_response("sair")
#print("Charlotte -",response)
