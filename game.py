import os
import keyboard
import random
import platform
import time


class PointGame:
    def __init__(self):
        self.MAX_X = 38
        self.MIN_X = 1
        self.MAX_Y = 26
        self.MIN_Y = 1
        
        self.player_x = 15
        self.player_y = 15
        self.speed = 1

        self.fruit_x = random.randint(3, 38)
        self.fruit_y = random.randint(1, 26)

        self.fruit_symbol = "O"
        self.score = 0
        self.player_coins = 0
        self.score_until_5 = 0

        self.items_store = {"!": 5, "?": 10, ":D": 20, ":S": 20, ":o": 20}
        self.player_symbol = "."
        self.player_symbols_purchased = {0: ".", 1: "", 2: "", 3: "", 4: "", 5: ""}


    def play(self):
        """
        The main function
        """
        self.define_console_window()
        self.verify_system()
        self.listen()

    def verify_system(self):
        self.operating_system = platform.system()

        if self.operating_system == "Windows":
            self.clean_command = 'cls'
            
        elif self.operating_system == 'Linux':
            self.clean_command = 'clear'
            
        else:
            print("[Error] Operating system not identified")
            time.sleep(2)
            self.stop()

    def define_console_window(self):
        cmd = "mode 80, 30"
        os.system(cmd)

    def title(self, msg):
        """
        Prints a title with the msg you want
        """
        print("=" * 30)
        print(f"{msg:^30}")
        print("=" * 30)

    def draw_player(self):
        """
        Draw the player in the console
        """
        
        for i in range(self.player_y):
            print()

        for i in range(self.player_x * 2):
            print(end=" ")
        
        print(self.player_symbol)

    def draw_fruit(self):
        """
        Draw the fruit/symbol in the console
        """
        if self.player_x == self.fruit_x and self.player_y == self.fruit_y - 2:
            self.fruit_x = random.randint(1, 38)
            self.fruit_y = random.randint(3, 26)
            self.score += 1
            self.score_until_5 += 1

            if self.score_until_5 >= 5:
                self.player_coins += 1
                self.score_until_5 = 0
                
        for i in range(self.fruit_y):
            print()

        for i in range(self.fruit_x * 2):
            print(end=" ")

        print(self.fruit_symbol)

    def draw_menu(self):
        """
        A menu to the user see your score
        """
        print(f"SCORE: {self.score} - COINS: {self.player_coins} - x: {self.player_x} y: {self.player_y}")
        print("Q -> to open menu")

    def clean(self):
        """
        Clean the screen (console), to function the animation of the player walking
        """
        os.system(self.clean_command) or None

    def lobby(self):
        """
        It is a mini-lobby, to the user can choose
        """
        self.clean()
        self.title("LOBBY")
        print("1 - STORE")
        print("2 - PLAY")
        print("3 - SYMBOLS PURCHASED")
        print("q - QUIT")
        print("=" * 30)

        time.sleep(1)

        while True:
            if keyboard.is_pressed("1"):
                self.goto_store()

            elif keyboard.is_pressed("2"):
                self.play()

            elif keyboard.is_pressed("3"):
                self.goto_items_purchased()

            elif keyboard.is_pressed("q"):
                self.stop()

    def goto_store(self):
        """
        Mini-store in the game, where you can but new symbol to play
        """
        self.clean()
        self.title("STORE")
        print(f"YOU HAVE {self.player_coins} COINS")
        print("=" * 30)
        print("""1 -> ! -> 5 coins
2 -> ? -> 10 coins
3 -> :D -> 20 coins
4 -> :S -> 20 coins
5 -> :o 20 coins
q -> QUIT""")

        time.sleep(1)

        while True:
            if keyboard.is_pressed("1"):
                self.buy_item("!")

            elif keyboard.is_pressed("2"):
                self.buy_item("?")

            elif keyboard.is_pressed("3"):
                self.buy_item(":D")

            elif keyboard.is_pressed("4"):
                self.buy_item(":S")

            elif keyboard.is_pressed("5"):
                self.buy_item(":o")

            elif keyboard.is_pressed("q"):
                self.lobby()

            else:
                continue

            self.lobby()

    def goto_items_purchased(self):
        self.clean()
        self.title("SELECT ITEM")

        for k, v in self.player_symbols_purchased.items():
            if v != "":
                print(f"{k} -> {v}")

        print("q -> QUIT")

        time.sleep(1)

        while True:
            for v in self.player_symbols_purchased.values():
                if v != "":
                    if keyboard.is_pressed("0"):
                        self.player_symbol = self.player_symbols_purchased.get(0)
                        print(f"Selected symbol: {self.player_symbol}")
                        time.sleep(2)
                        self.lobby()

                    elif keyboard.is_pressed("1"):
                        self.player_symbol = self.player_symbols_purchased.get(1)
                        print(f"Selected symbol: {self.player_symbol}")
                        time.sleep(2)
                        self.lobby()

                    elif keyboard.is_pressed("2"):
                        self.player_symbol = self.player_symbols_purchased.get(2)
                        print(f"Selected symbol: {self.player_symbol}")
                        time.sleep(2)
                        self.lobby()

                    elif keyboard.is_pressed("3"):
                        self.player_symbol = self.player_symbols_purchased.get(3)
                        print(f"Selected symbol: {self.player_symbol}")
                        time.sleep(2)
                        self.lobby()

                    elif keyboard.is_pressed("4"):
                        self.player_symbol = self.player_symbols_purchased.get(4)
                        print(f"Selected symbol: {self.player_symbol}")
                        time.sleep(2)
                        self.lobby()

                    elif keyboard.is_pressed("5"):
                        self.player_symbol = self.player_symbols_purchased.get(5)
                        print(f"Selected symbol: '{self.player_symbol}'")
                        time.sleep(2)
                        self.lobby()

                    elif keyboard.is_pressed("q"):
                        self.lobby()

                    else:
                        break

            continue

    def buy_item(self, item):
        """
        Verify if you have money to buy the item
        """
        print("=" * 30)

        if self.player_coins >= self.items_store.get(item) and item not in self.player_symbols_purchased.values():
            self.player_symbol = item
            self.player_coins -= self.items_store.get(item)

            for k, v in self.player_symbols_purchased.items():
                if v == "":
                    self.player_symbols_purchased[k] = item
                    break

            print(f"Item '{item}' was bought!")

        elif item in self.player_symbols_purchased.values():
            print(f"Item '{item}' is already purchase!")

        else:
            print(f"Item '{item}' cannot be buy!")

        time.sleep(2)


    def move_up(self):
        """
        Move the player to up
        """
        self.player_y -= self.speed

    def move_down(self):
        """
        Move the player to down
        """
        self.player_y += self.speed

    def move_left(self):
        """
        Move the player to the left
        """
        self.player_x -= self.speed

    def move_right(self):
        """
        Move the player to the right
        """
        self.player_x += self.speed

    def detect_collision(self):
        if self.player_x < self.MIN_X:
            self.player_x += self.speed

        if self.player_x > self.MAX_X:
            self.player_x -= self.speed

        if self.player_y < self.MIN_Y:
            self.player_y += self.speed

        if self.player_y > self.MAX_Y:
            self.player_y -= self.speed
            
    def listen(self):
        """
        It is listener. It is listening if the user click the keyboard key (w, s, a, d), if clicked executes the function to make the player go to that direction
        w -> Up
        s -> Down
        a -> Left
        d -> Right
        """
        while True:
            try:
                if keyboard.is_pressed("w"):
                    self.move_up()

                if keyboard.is_pressed("s"):
                    self.move_down()

                if keyboard.is_pressed("a"):
                    self.move_left()

                if keyboard.is_pressed("d"):
                    self.move_right()

                if keyboard.is_pressed("q"):
                    self.lobby()

                self.draw_menu()
                self.detect_collision()
                self.draw_player()
                self.clean()
                self.draw_fruit()
                self.clean()

            except KeyboardInterrupt:
                self.stop()

    def stop(self):
        """
        Stop the game if occur some KeyBoardInterrupt
        """
        self.clean()
        print("Game finished!")
        time.sleep(0.5)
        quit()
