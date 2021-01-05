""" from matching.games import StableMarriage
suitor_preferences = {
    "A": ["D", "E", "F"], "B": ["D", "F", "E"], "C": ["F", "D", "E"]
}

reviewer_preferences = {
    "D": ["B", "C", "A"], "E": ["A", "C", "B"], "F": ["C", "B", "A"]
}
game = StableMarriage.create_from_dictionaries(
    suitor_preferences, reviewer_preferences
)
print(game.solve())
 """


from matching.games import StableMarriage
suitor_preferences = {
    "riche": ["gentil", "beau", "intelligent"], "drôle": ["gentil", "intelligent", "beau"], "cultivée": ["intelligent", "gentil", "beau"]
}

reviewer_preferences = {
    "gentil": ["drôle", "cultivée", "riche"], "beau": ["riche", "cultivée", "drôle"], "intelligent": ["cultivée", "drôle", "riche"]
}
game = StableMarriage.create_from_dictionaries(
    suitor_preferences, reviewer_preferences
)
print(game.solve())