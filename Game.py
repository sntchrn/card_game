import Deck
import Player

class Game:
	def __init__(self):
		name1 = input("プレイヤー1の名前：")
		name2 = input("プレイヤー2の名前：")
		self.deck = Deck.Deck()
		self.p1 = Player.Player(name1)
		self.p2 = Player.Player(name2)

	def wins(self, winner):
		w = "このラウンドは {} が勝ちました"
		w = w.format(winner)
		print(w)

	def draw(self, p1n, p1c, p2n, p2c):
		d = "{} は {}、 {} は {} を引きました"
		d = d.format(p1n, p1c, p2n, p2c)
		print(d)

	def play_game(self):
		cards = self.deck.cards
		print("ゲームを開始します")
		while len(cards) >= 2:
			m = "q で終了、それ以外のキーでPlay："
			response = input(m)
			if response == 'q':
				break
			p1c = self.deck.rm_card()
			p2c = self.deck.rm_card()
			p1n = self.p1.name
			p2n = self.p2.name
			self.draw(p1n, p1c, p2n, p2c)

			if p1c > p2c:
				self.p1.wins += 1
				self.wins(self.p1.name)
			else:
				self.p2.wins += 1
				self.wins(self.p2.name)

		win = self.winner(self.p1, self.p2)
		print("ゲーム終了  {} の勝利です！！".format(win))

	def winner(self, p1, p2):
		if p1.wins > p2.wins:
			return p1.name
		if p1.wins < p2.wins:
			return p2.name
		return "引き分け！！"

game = Game()
game.play_game()
