
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from chatterbot.conversation import Statement




bot=ChatBot('test')
conv=open('D:/AVANTAR/PythonProjects/Automation/WhatsappAutomation/chatting.txt','r').readlines()
trainer=ListTrainer(bot)
trainer.train(conv)
def get_msg(smsg):
	response=bot.get_response(text=f' {smsg} ',search_text=f' {smsg} ')
	return response

