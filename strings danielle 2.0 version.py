# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
#First part of the assignment
scorer_0 = 'Ruud Gullit'
scorer_1 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = scorer_0+" "+str(goal_0)+","+" "+scorer_1+" "+str(goal_1)
report =  f'{scorer_0} scored in the {goal_0}nd minute\n{scorer_1} scored in the {goal_1}th minute'
print(report)
print(scorers)

#part two of the assignment
player = "Wim Kieft"
first_name = player[:player.find(" ")]
last_name = player[player.find(" "):]
name_short = f'{player[:1]}.{last_name}'
first_name_len = len(first_name)
last_name_len = len(last_name)-1    
first_namechant = f'{first_name}! '
chant = (first_namechant*first_name_len)[:-1] 
good_chant = chant[-1] != " " 
print(good_chant)
print(chant)