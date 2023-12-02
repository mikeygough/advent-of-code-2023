# set file
fname = "puzzle_input.txt"

# read in file
with open(fname, "r") as file:
    puzzle_input = file.readlines()
    file.close()

sum = 0

for line in puzzle_input:
    # get game number
    game_line = line.split(":")
    game_number = int(game_line[0][4:])
    print(f"Game Number: {game_number}")

    # split off individual games
    games = game_line[1].split(";")
    print(f"Full Game Draw: {games}")

    # initialize counter for colored cubes
    counter = {
        "red": [],
        "green": [],
        "blue": [],
    }
    
    # check each game
    for game in games:
        # clean up strings
        game = game.replace(" ", "")  # remove spaces
        game = game.replace("\n", "")  # remove newlines
        cube_draw = game.split(",")  # split into cube draws

        print(f"Cube Draw {cube_draw}")

        # check each draw, update counter
        for cube in cube_draw:
            if "red" in cube:
                counter["red"].append(int(cube.replace("red", "")))
            elif "green" in cube:
                counter["green"].append(int(cube.replace("green", "")))
            elif "blue" in cube:
                counter["blue"].append(int(cube.replace("blue", "")))
    
    print(counter)
    sum += (max(counter['red']) * max(counter['green']) * max(counter['blue']))
    
print(sum)