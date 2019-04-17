import random

guess = ''
while guess not in ('heads', 'tails'):
	print('Guess the coin toss! Enter heads or tails:')
	guess = input()
	#assert guess == 'heads' or guess == 'tails','You must input heads or tails'

coin = ['heads','tails']
index = random.randint(0, 1) # 0 is tails, 1 is heads
toss = coin[index]

if toss == guess:
	print('You got it!')
else:
	print('Nope! Guess again!')
	guess = input()
	if toss == guess:
		print('You got it!')
	else:
		print('Nope. You are really bad at this game.')