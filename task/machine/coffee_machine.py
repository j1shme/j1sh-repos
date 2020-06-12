class Coffee_Machine:

    water, milk, coffee_beans, disposable_cups, money = 0, 0, 0, 0, 0

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.disposable_cups = 9
        self.money = 550

    def buy(self, coffee_type):
        if coffee_type == 1:
            if self.water - 250 < 0:
                print('Sorry, not enough water')
            else:
                self.water -= 250
                if self.coffee_beans - 16 < 0:
                    print('Sorry, not enough coffee beans')
                else:
                    self.coffee_beans -= 16
                    if self.disposable_cups - 1 < 0:
                        print('Sorry, not enough cups')
                    else:
                        self.disposable_cups -= 1
                        self.money += 4
                        print('I have enough resources, making you a coffee!')
        elif coffee_type == 2:
            if self.water - 350 < 0:
                print('Sorry, not enough water')
            else:
                self.water -= 350
                if self.milk - 75 < 0:
                    print('Sorry, not enough milk')
                else:
                    self.milk -= 75
                    if self.coffee_beans - 20 < 0:
                        print('Sorry, not enough beans')
                    else:
                        self.coffee_beans -= 20
                        if self.disposable_cups - 1 < 0:
                            print('Sorry, not enough cups')
                        else:
                            self.disposable_cups -= 1
                            self.money += 7
                            print('I have enough resources, making you a coffee!')
        elif coffee_type == 3:
            if self.water - 200 < 0:
                print('Sorry, not enough water')
            else:
                self.water -= 200
                if self.milk - 100 < 0:
                    print('Sorry, not enough milk')
                else:
                    self.milk -= 100
                    if self.coffee_beans - 12 < 0:
                        print('Sorry, not enough beans')
                    else:
                        self.coffee_beans -= 12
                        if self.disposable_cups - 1 < 0:
                            print('Sorry, not enough water')
                        else:
                            self.disposable_cups -= 1
                            self.money += 6
                            print('I have enough resources, making you a coffee!')
        return self.water, self.milk, self.coffee_beans, self.disposable_cups, self.money

    def fill(self, water_, milk_, coffee_beans_, disposable_cups_):
        self.water += water_
        self.milk += milk_
        self.coffee_beans += coffee_beans_
        self.disposable_cups += disposable_cups_

    def take(self):
        print('I gave you {}'.format(self.money))
        self.money -= self.money

    def remaining(self):
        return print("""The coffee machine has:
        {0} of water
        {1} of milk
        {2} of coffee beans
        {3} of disposable cups
        ${4} of money
        """.format(self.water, self.milk, self.coffee_beans, self.disposable_cups, self.money))


instance = Coffee_Machine()
action = ""
while action != "exit":
    action = input("Write action (buy, fill, take, remaining, exit): ")
    if action != 'exit':
        if action == 'buy':
            coffee_type_ = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - capuccino, back - to main menu:')
            if coffee_type_ != 'back':
                coffee_type_ = int(coffee_type_)
                instance.buy(coffee_type_)
        elif action == 'fill':
            water_inp = int(input("Write how many ml of water do you want to add:"))
            milk_inp = int(input("Write how many ml of milk do you want to add:"))
            coffee_beans_inp = int(input("Write how many grams of coffee beans do you want to add:"))
            disposable_cups_inp = int(input("Write how many disposable_cups of coffee do you want to add:"))
            instance.fill(water_inp, milk_inp, coffee_beans_inp, disposable_cups_inp)
        elif action == 'take':
            instance.take()
        elif action == 'remaining':
            instance.remaining()
