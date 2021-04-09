import random
from palavras import *


class Forca:
	def __init__(self):
		self.__word_object = random.choice(palavras)
		
		length = len(self.word_object["palavra"])
		self.__answer = "- " * length


	@property
	def answer(self):
		return self.__answer
	
	@answer.setter
	def answer(self, state):
		self.__answer = state
	
	@property
	def word_object(self):
		return self.__word_object

	@word_object.setter
	def word_object(self, state):
		self.__word_object["palavra"] = state["palavra"]
		self.__word_object["dica"] = state["dica"]