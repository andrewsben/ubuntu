# deck = ["2H","3H","4H","5H","6H","7H","8H","9H","10H","JH","QH","KH","AH","2D","3D","4D","5D","6D","7D","8D","9D","10D","JD","QD","KD","AD","2C","3C","4C","5C","6C","7C","8C","9C","10C","JC","QC","KC","AC","2S","3S","4S","5S","6S","7S","8S","9S","10S","JS","QS","KS","AS"]
deck = [1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11,12]

pot = 1000
bankroll = 1000
while deck.count > 3 and pot > 0 and bankroll > 0:
	import random

	random.shuffle(deck)

	left = deck.pop()
	right = deck.pop()
	middle = deck.pop()

	print "--------------------------------------------------"
	print "Pot = $%d\nLeft: %s \tRight: %s" % (pot, left, right)

	print "--------------------------------------------------"
	print "Type the amount you want to bet (enter 0 to PASS):"
	bet = int(raw_input())
	print "--------------------------------------------------"

	pot = pot + bet
	bankroll = bankroll - bet

	print "The pot is $%d and your bankroll is: $%d" % (pot, bankroll)

	print "Your card: %s" % (middle)

	if (middle < left and middle > right) or (middle > left and middle < right):
		pot = pot - bet
		bankroll = bankroll + ( bet * 2)
		print "you win $%d" % bet
		print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
		print "Pot = $%d, Bankroll = $%d" % (pot, bankroll)
		print "Thanks for playing!"
		print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
	else:
		print "you lost :("
		print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
		print "Pot = $%d, Bankroll = $%d" % (pot, bankroll)
		print "Thanks for playing!"
		print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
