def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
    badges = []
    for name in names:
        badges.append(badge_maker(name))
    return badges
def assign_rooms(names):
    rooms = []
    i = 1
    for name in names:
        rooms.append(f"Hello, {name}! You'll be assigned to room {i}!")
        i += 1
    return rooms
def printer(names):
    badges = batch_badge_creator(names)
    rooms = assign_rooms(names)
    for badge in badges:
        print(badge)
    for room in rooms:
        print(room)
    return None
print(printer(["Arel", "Carol"]))
