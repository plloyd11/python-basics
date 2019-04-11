# attendees = ["Bob", "Steve", "Ralph"]

# print("There are", len(attendees), "attendees currently")

books = [
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]

video_games = [
    "The Legend of Zelda: Breath of the Wild",
    "Splatoon 2",
    "Super Mario Odyssey",
]

# insert to start of list: books.insert(0, "cheese")

def display_lists(display_name, wishes):
    items = wishes.copy()
    print(display_name + ":")
    suggested_gift = items.pop(0)
    print("======>", suggested_gift, "<======")
    for item in items:
        print("* " + item)
    print()

display_lists("Books", books)
display_lists("Video Games", video_games)