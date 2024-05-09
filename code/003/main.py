
# create a game of find the treasure island.

print('''
               __________
        /\____;;___\\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|

    Welcome to Treasure Island.\nYour mission is to find the treasure.
      ''')

direction = input("left or right? (l, r)").lower()
if direction not in ('l', 'r'):
    print("Invalid input. Please enter 'l', or 'r'.")
else:
    if direction == 'r':
        print("Game Over.")
    else:
        action = input("swim or wait? (s, w)").lower()
        if action not in ('s', 'w'):
            print("Invalid input. Please enter 's', or 'w'.")
        elif action == 's':
            print("Game Over.")
        else:
            door_color = input("Which door? Blue, Red or Yellow? (b, r, y)").lower()
            if door_color not in ('b', 'r', 'y'):
                print("Invalid input. Please enter 'b', 'r' or 'y'.")
            elif door_color == 'r' or door_color == 'b':
                print("Game Over.")
            else:
                print("You Win!")