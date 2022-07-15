# string concatentation (aka how to put strings together)
# suppose we want to create a string that says "say hello to _____"
name = "Qwas" # some string variable

# a few ways to do this
print("say hello to " + name)
print("say hello to {}".format(name))
print(f"say hello to {name}")

fname = input("Name: ")
language = input("Programing language: ")
verb2 = input("This month: ")
wish_luck = input("Finish month: ")

madlib = (f"Hey my name is {fname} ! Its so excited to programming \
I start learning {language} programing language. I started learning in {verb2} and want to finish it in {wish_luck}!")

print(madlib)