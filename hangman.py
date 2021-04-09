import random
from challenges import *


class Hangman:
	def __init__(self):
		self.__challenge_object = random.choice(challenges)
		
		word_length = len(self.__challenge_object["word"])
		
		self.__answer = "- " * word_length

		self.__letters_left = word_length
		
		self.__errors_left = int(word_length * 0.3)


	@property
	def answer(self):
		return self.__answer
	
	@answer.setter
	def answer(self, state):
		self.__answer = state
	
	@property
	def challenge_object(self):
		return self.__challenge_object

	@challenge_object.setter
	def challenge_object(self, state):
		self.__challenge_object["word"] = state["word"]
		self.__challenge_object = state["clue"]

	@property
	def letters_left(self):
		return self.__letters_left

	@letters_left.setter
	def letters_left(self, state):
		self.__letters_left = state

	@property
	def errors_left(self):
		return self.__errors_left

	@errors_left.setter
	def errors(self, state):
		self.__errors_left = state