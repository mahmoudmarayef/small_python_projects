import random

class Bagels:
    def __init__(self) -> None:
        self.DIGITS_NUM = 3
        self.MAX_GUESSES = 10
        self.WELCOME = open('welcome.txt')

    def main(self) -> None:
        print(self.WELCOME.read())

        while True:
            secret_num = self.guess_num()
            print("I have thought up a number.")
            print("You have {} guesses to get it.".format(self.MAX_GUESSES))

            num_guesses = 1
            while num_guesses <= self.MAX_GUESSES:
                guess = ''
                while len(guess) != self.DIGITS_NUM or not guess.isdecimal():
                    print('Guess #{}:'.format(num_guesses))
                    guess = input('> ')

                clues = self.get_clues(guess, secret_num)
                print(clues)
                num_guesses += 1

                if guess == secret_num:
                    break
                if num_guesses > self.MAX_GUESSES:
                    print('You ran out of guesses.')
                    print('The answer was {}.'.format(secret_num))

            print('Do you want to play again? (yes or no)')
            if not input('> ').lower().startswith('y'):
                break
        print('Thanks for playing!')


    def guess_num(self) -> str:
        numbers = list('0123456789')
        random.shuffle(numbers)

        guess = ''
        for i in range(self.DIGITS_NUM):
            guess += str(numbers[i])

        return guess

    
    def get_clues(self, guess, secret_num) -> str:
        if guess == secret_num:
            return "You got it!"
        
        clues = []

        for i in range(len(guess)):
            if guess[i] == secret_num[i]:
                clues.append('Fermi')
            elif guess[i] in secret_num:
                clues.append('Pico')
        
        if len(clues) == 0:
            return 'Bagels'
        else:
            clues.sort()
            return ' '.join(clues)


game = Bagels()
game.main()