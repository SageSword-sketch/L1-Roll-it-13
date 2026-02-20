
error = "please enter an integer more than / equal to 13."

try:
    game_goal = int(input("what is the game goal? "))

    if game_goal < 13:
         print(error)
    else:
        print(f"game goal: {game_goal}")

except ValueError
    print(error)