import random as r

name1 = input("Type a Name: ")
verb1 = input("Input a type of camping trip: ")
noun1 = input("Type Days: ")
noun2 = input("Type an outdoors activity: ")
adjective1 = input("Type a place to go: ")
adjective2 = input("Type a descriptive word: ")
name2 = input("Type Name:")
noun3 = input("Enter A place of business: ")
adjective3 = input(" Type A store Item: ")
noun4 = input("Enter time:")
catname = input("Type name: ")
noun5 = input("Enter place: ")
womensname = input(" Type womens name: ")
verb2 = input("Type what happened to her: ")
noun6 = input("Type a time length: ")

madlib1 = ("Summer is coming up " + name1 + " and I like to go camping at " + verb1 + ". We usually " + noun1 + ". From there we usually just build fires, relax, we also do some " +
           noun2 + ". By then we are usually almost done with our trip, we pack up, leave and stop and visit " + adjective1 + " on the way back home.")

madlib2 = ("Today is going to be a " + adjective2 + ". My friend, " + name2 + " meets me at the " + noun3 + ". We usually get " +
           adjective3 + ". After that we go hangout at the park, usually till " + noun4 + ". Then we go home and do it again the next day.")

madlib3 = ("My name is " + catname + ", I am a stray cat. I live around " + noun5 + ". I don't have owners, nor do I need them. I had one her name was " + womensname +
           ". It's been a while since I had one. She just " + verb2 + " one day, no trace,  ever since then i've been on my own. It has been what feel like " + noun6 + " but i've been wondering for a long time")


randomNumber = r.randint(1, 3)

# print(randomNumber)

if randomNumber <= 1:
    print(madlib1)
elif randomNumber <= 2:
    print(madlib2)
else:
    print(madlib3)
