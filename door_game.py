
import random

winner_door = random.sample(['fizz', 'foo', 'bar'], 1)
print winner_door

def try_door(test_door):
	choose_door = test_door

	if choose_door == winner_door:
		return 'You win!'
	else:
		print('Too bad, try again')
		return try_door(input())

print("\n Door 1: fizz \n Door 2: foo \n Door 3: bar \n Choose one:")
print(try_door(input()))

