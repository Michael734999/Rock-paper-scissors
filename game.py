import random
import time

moves = ['rock', 'paper', 'scissors']


def print_pause(msg):
    print(msg)
    time.sleep(2)


def intro():
    print_pause("Welcome to this game of Rock, paper, scissors.")
    print_pause("This game consists out of 5 rounds.")
    print_pause("There are 2 players.")
    print_pause("Player 1- That is you.\n"
                "Player 2- That is the computer.\n")


class Player:
    my_move = None
    their_move = None

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        else:
            return self.their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        elif self.my_move == moves[0]:
            return moves[1]
        elif self.my_move == moves[1]:
            return moves[2]
        else:
            return moves[0]


class HumanPlayer(Player):
    def move(self):
        while True:
            choose = self.my_move
            choose = input("Rock, paper or scissors? > ").lower()
            if 'rock' in choose:
                return moves[0]
            elif 'paper' in choose:
                return moves[1]
            elif 'scissors' in choose:
                return moves[2]
            else:
                print("Please select rock, paper or scissors.")


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"\nPlayer 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        if beats(move1, move2):
            self.p1_score += 1
            print("Player 1 wins!")
        elif beats(move2, move1):
            self.p2_score += 1
            print("Player 2 wins!")
        else:
            print("It's a tie!")

        print(f"Score:\nPlayer 1: {self.p1_score}"
              f"\tPlayer 2: {self.p2_score}\n")

    def play_game(self):
        print("Game start!\n")
        self.p1_score = 0
        self.p2_score = 0
        for round in range(1, 6):
            print(f"***\tRound {round}:\t***")
            self.play_round()
        if self.p1_score > self.p2_score:
            print("\t***PLAYER 1 WINS THE GAME!!!***")
        elif self.p1_score < self.p2_score:
            print("\t***PLAYER 2 WINS THE GAME!!!***")
        else:
            print("\t***IT'S A DRAW!!!***")
        print("Game over!")


strategy = (RandomPlayer(), ReflectPlayer(), CyclePlayer())
randomP = random.choice(strategy)

if __name__ == '__main__':
    intro()
    game = Game(HumanPlayer(), randomP)
    game.play_game()
