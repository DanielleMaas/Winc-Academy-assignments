# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
#Deel 1 speler scoort in minuut
Spelermetgoal1='Ruud Gullit'
Spelermetgoal2='Marco van Basten'
goal_0=32
goal_1=54
scorers= f'{Spelermetgoal1} {goal_0}, {Spelermetgoal2} {goal_1}'
report= f'{Spelermetgoal1} scored in the {goal_0}nd minute\n{Spelermetgoal2} scored in the {goal_1}th minute'
print(report)

#deel 2 chant voor andere speler
player="Wim Kieft"
first_name=player[0:3]
last_name=player[4:9]
name_short="W. Kieft"
first_name_len=len(first_name)
last_name_len=len(last_name)
first_namechant=f'{first_name}! '
chant=(first_namechant*first_name_len)[:-1]
good_chant=chant[-1]!= " "
print(good_chant)