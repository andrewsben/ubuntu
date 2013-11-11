#!/usr/bin/python

import random


# deck = [
	# "2H","3H","4H","5H","6H","7H","8H","9H","10H","JH","QH","KH","AH",
	# "2D","3D","4D","5D","6D","7D","8D","9D","10D","JD","QD","KD","AD",
	# "2C","3C","4C","5C","6C","7C","8C","9C","10C","JC","QC","KC","AC",
	# "2S","3S","4S","5S","6S","7S","8S","9S","10S","JS","QS","KS","AS"
	# ]

starting_deck = [
	1,2,3,4,5,6,7,8,9,10,11,12,13,
	1,2,3,4,5,6,7,8,9,10,11,12,13,
	1,2,3,4,5,6,7,8,9,10,11,12,13,
	1,2,3,4,5,6,7,8,9,10,11,12,13
	]

pot = 1000
bankroll = 1000
deck = starting_deck[:]

while pot > 0 and bankroll > 0:
	if len(deck) < 3:
		deck = starting_deck[:]
	print "shuffeling the deck!"
	random.shuffle(deck)
	left = deck.pop()
	right = deck.pop()

	print "\n\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
	print "Pot = $%d \tBankroll = $%d \nLeft: %s \tRight: %s\n" % (pot, bankroll, left, right)
	print "--------------------------------------------------"

	while True:
		try:
			bet = int(raw_input("Type the amount you want to bet (enter 0 to PASS): "))
			break
		except ValueError:
			print "Oops, that's not a valid bet. Try again..."
		print "--------------------------------------------------"
		pot = pot + bet

	bankroll = bankroll - bet
	print "The pot is $%d and your bankroll is: $%d" % (pot, bankroll)

	if bet == 0:
		print "PASSED - thanks for playing!"
		print "--------------------------------------------------"
	else:
		middle = deck.pop()
		print "Your card: %s" % (middle)
		if (middle < left and middle > right) or (middle > left and middle < right):
			pot = pot - ( bet * 2 )
			bankroll = bankroll + ( bet * 2 )
			print "----------\n|        |\n|  WIN!  |\n|        |\n----------"
			print "Bankroll = $%d" % bankroll
			print "Thanks for playing!"
			print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n\n"
		else:
			print "\t\t----------\n\t\t|        |\n\t\t|  LOST  |\n\t\t|        |\n\t\t----------"
			print "Bankroll = $%d" % bankroll
			print "Thanks for playing!"
			print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n\n"

