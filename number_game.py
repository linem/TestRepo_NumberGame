from random import randint

number = randint(1,25)

def try_number(test_number):
	test_number = int(test_number)
	if (test_number == number):
		return 'Correct! Good Job!'
	elif (test_number < number):
		print('Not quite, go higher')
		return try_number(input())
	else:
		print('Not quite, go lower')
		return try_number(input())

print("Can you guess the number I'm thinking of?")
print(try_number(input()))

#Funkar detta?
##Prova själv, kör det i terminalen.