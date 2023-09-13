'''
For 3 arrays representing the results of different clubs(wins, draws, goals_scored, goals, conceded) 
calculate which is the champion and the second place regarding position in the array. Use football rules. 
The final result should be a list with 2 values [ "position of the champion in the initial array", position of the runner-up in the initial array" ]
'''

# define the results of each team in separate arrays
wins = [9, 8, 35, 10, 6]
draws = [4, 7, 6, 8, 7]
goals_scored = [26, 28, 25, 22, 26]
goals_conceded = [18, 21, 22, 23, 22]

# calculate the total points for each team
points = [3 * w + d for w, d in zip(wins, draws)]
print(f"points: {points} ")

# create a list of tuples representing each team with their stats and index
teams = list(zip(points, goals_scored, goals_conceded, range(len(wins))))
print(f"teams BEFORE: {teams} ")

# sort the teams by their ranking based on football rules
teams.sort(key=lambda x: (x[0], x[1]-x[2], x[1]), reverse=True)
print(f"teams AFTER: {teams} ")

# get the champion and the runner-up
champion = teams[0]
runner_up = teams[1]

pts_champ = champion[0]
pts_runner = runner_up[0]

gpc = champion[1]-champion[2]    #saldo
gpr = runner_up[1]-runner_up[2]  #saldo

gsc = champion[1]                #goalsPRO  
gsr = runner_up[1]                #goalsPRO

if pts_champ > pts_runner:
    message = "Champion for points"
elif (pts_champ == pts_runner):
        print(f"-----------------------------------------------------------")
        if gpc < gpr:
            runner_up = teams[0]
            champion = teams[1]
            message = "Champion for goal difference"
        elif gpc == gpr:
            if gsc < gsr:
                runner_up = teams[0]
                champion = teams[1]
                message = "Champion for goals scored"
            
print(f"-----------------------------------------------------------")
print(f"POINTS champion: {champion[0]} ")
print(f"POINTS runner_up: {runner_up[0]} ")
print(f"-----------------------------------------------------------")
gpc = champion[1]-champion[2]
gpr = runner_up[1]-runner_up[2]
print(f"goals saldo champion: {gpc} ")
print(f"goals saldo runner_up: {gpr} ")

print(f"-----------------------------------------------------------")
print(f"goals SCORED champion: {gsc} ")
print(f"goals SCORED runner_up: {gsr} ")
print(f"-----------------------------------------------------------")

# get the positions of the champion and the runner-up in the initial arrays
champion_position = champion[3]
runner_up_position = runner_up[3]

# create a list with the positions of the champion and the runner-up
result = [champion_position, runner_up_position]

# print the result and the message
print("Champion position: {}".format(champion_position))
print("Runner-up position: {}".format(runner_up_position))
print("Result: {}".format(result))
print("Champion determined by: {}".format(message))

