# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
# Part 1

scorer_1 = 'Ruud Gullit'
scorer_2 = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = scorer_1 + ' ' + str(goal_0) + ', ' + scorer_2 + ' ' + str(goal_1)

report = scorer_1 + ' scored in the ' + str(goal_0) + 'nd minute' + '\n' + scorer_2 + ' scored in the ' + str(goal_1) + 'th minute'

# Part 2

player = 'Hans van Breukelen'
first_name = player[0:(player.find(' '))] # Voornaam achterhalen

last_name_len = len(player[(player.find(' ')):-1]) # Lengte van achternaam achterhalen

name_short = player[0] + '.' + player[player.find(' '):] # Voorletter met achternaam achterhalen

chant = (((first_name + '! ') * (len(player[0:player.find(' ')])-1)) + first_name + '!') # Een chant maken die de naam met uitroepteken roept keer het aantal letters in de voornaam zonder spatie op het eind

good_chant = (chant[-1] != ' ') # Controle of de chant eindigt met een spatie