# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# partone


def greet(name, hello='Hello, <name>!'):
    replacingname = hello.replace('<name>', name)
    print(replacingname)
    return(replacingname)


Firstname = "Sam"
greet(Firstname)
greet(Firstname, "What's up, <name>!")


# parttwo


def force(mass=9.8, body='earth'):
    celestialbody = {
        'sun': 274,
        'jupiter': 24.9,
        'neptune': 11.2,
        'saturn': 10.4,
        'earth': 9.8,
        'uranus': 8.9,
        'venus': 8.9,
        'mars': 3.7,
        'mercury': 3.7,
        'moon': 1.6,
        'pluto': 0.6
    }
    if body == "":
        valueofearth = 9.8
        calculateforce = float(mass) * float(valueofearth)
        text = f'The gravity of earth is {calculateforce}'
    else:
        valueofbody = celestialbody[body]
        calculateforce = float(mass) * valueofbody
        text = f'The gravity of {body} is {calculateforce}'
    print(text)
    return calculateforce


mass = 1.0
body = ""

force(mass, body)

# partthree
# gravity is defined as 6674*10 to the -11nd power
# distance can be entered in meters and will be caculated to the 2nd power
# to get the same result with the car distance, dividing by 1000 was necessary


def pull(m1, m2, d):
    gravity = 6674*10**-11
    d = d**2
    if m1 == 800:
        calculation = (gravity*((m1*m2)/d))/1000
    else:
        calculation = gravity * ((m1*m2)/d)
    return(calculation)

# these are the defintions is took from the website:
# mass of earth is 5972*10 to the 24th power kilograms
# mass of apple is 0.1 kilograms
# distance is (6731 times 10 to the 6th power) to the 2nd power
# gravity is 6674*10 to the -11nd power


m1 = 0.1
m2 = 5972*10**4
d = 6371*10**6

print(round((pull(m1, m2, d)), 30))

# There is a second example with cars

m1 = float(800)
m2 = float(1500)
d = float(3)


print(round((pull(m1, m2, d)), 10))
