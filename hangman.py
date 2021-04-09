import random
from challenges import *


class Hangman:
	def __init__(self):
		self.__challenge_object = random.choice(challenges)
		
		word_length = len(self.__challenge_object["word"])
		
		self.__answer = "- " * word_length

		self.__letters_left = word_length
		
		self.__errors_left = int(word_length * 0.3)

		self.__letters_tried = []

	def try_letter(self, letter):	
		# verifies if the letter was already tried
		if letter in self.__letters_tried:
			return False

		self.__letters_tried.append(letter)

		# verifies if the char exists in the word. If not, just stop the function.
		if self.__challenge_object["word"].count(letter) == 0:
			self.__errors_left = self.__errors_left - 1
			return False

		# verifies the position of the ocurrency, and changes the answer text.
		list_answer = list(self.__answer)
		index = 0
		for char in self.__challenge_object["word"]:
			if char == letter:
				self.__letters_left = self.__letters_left - 1
				list_answer[index] = letter
			index = index + 2

		self.__answer = "".join(list_answer)
	
		return True

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

	@property
	def letters_tried(self):
		return self.__letters_tried
