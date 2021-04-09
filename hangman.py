import random
from challenges import *


class Hangman:
	def __init__(self):
		self.__challenge_object = random.choice(challenges)
		
		length = len(self.word_object["word"])
		self.__answer = "- " * length


	@property
	def answer(self):
		return self.__answer
	
	@answer.setter
	def answer(self, state):
		self.__answer = state
	
	@property
	def word_object(self):
		return self.__challenge_object

	@word_object.setter
	def word_object(self, state):
		self.__challenge_object["word"] = state["word"]
		self.__challenge_object = state["clue"]