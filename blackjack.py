import random

#2 - 10 as is
#J,K,Q  -10

class HumanPlayer:
	def __init__(self):
		self.money = 100
		self.bet = 0

	def betM(self,amount):
		self.bet = amount

	def subBalance(self):
		self.money = self.money - self.bet

	def addBalance(self):
		self.money = self.money * 2


class Cards:
	def __init__(self):
		self.cards = [(x,y) for x in range(2,15) for y in ['Dice','Spade','Clubs','Heart']]
		self.myshuffle()

	def hit(self):
		return self.cards.pop(0)

	def myshuffle(self):
		random.shuffle(self.cards)

def main():
	human = HumanPlayer()
	print("You start with $100")
	while True:
		while True:
			deck = Cards()
			humanValue = 0
			compValue = 0
			while True:
				try:
					betMoney = int(input("Enter amount to bet"))
				except:
					print("Enter valid input")
				else:
					if human.money < betMoney:
						print("Not enough funds")
					else:
						human.betM(betMoney)
						break
			humanCards = [deck.hit(), deck.hit()]
			compCards = [deck.hit(), deck.hit()]
			print("Computer's cards are: ")
			print(compCards[0])
			print("Your cards are: ")
			print(humanCards[0])
			print(humanCards[1])
			humanValue = getValue(humanCards)
			print("Your value is " + str(humanValue))
			compValue = getValue(compCards)
			print("Computer value is " + str(compValue))
			while True:
				res = input("HIT OR STAY?")
				if res == "HIT":
					humanCards.append(deck.hit())
					humanValue = getValue(humanCards)
					print("Your value is " + str(humanValue))
					if humanValue > 21:
						break
				elif res == "STAY":
					break
				else:
					print("Enter valid input")

			if humanValue > 21:
				print("You exceeded 21, you lost")
				human.subBalance()
				break
			print("Dealer is playing")
			while compValue < 17:
				compCards.append(deck.hit())
				compValue = getValue(humanCards)
				print("Computer value is " + str(compValue))
			if compValue > 21 or humanValue > compValue:
				human.addBalance()
				print("You won! Your total amount is now " + str(human.money))
			else:
				human.subBalance()
				print("You lost! Your total amotn is now " + str(human.money))
			break
		playAgain = input("Do you want ot play again?")
		if playAgain == 'NO':
			break

		

def getValue(cards):
	value = 0
	aceCount = 0
	for c in cards:
		if c[0] >= 2 and c[0] <= 10:
			value += c[0]
		elif c[0] >= 11 and c[0] <= 13:
			value += 10
		else:
			aceCount += 1
	for i in range(0, aceCount):
		if value + 11 <= 21:
			value += 11
		else:
			value += 1
	print(cards)
	return value
	



if __name__ == '__main__':
	main()

