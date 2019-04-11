def suggest(product_idea):
    str(product_idea)
    if len(product_idea) < 3:
        raise ValueError("Please add more characters, dawg!")
    return product_idea + "inator"

ass = suggest("butt")

print(ass)