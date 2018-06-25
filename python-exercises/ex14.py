from sys import argv

script , user_name = argv
prompt = '>'

print(f"{user_name},I'm the {script} script.")
print("I'd like to ask you a few questions.")
print("Do you like me {user-name}")
likes = input(prompt)

print("Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
Alright, so you said {like} about liking me.
You live in {live}.Not sure where that is.
And you have a {computer} computer. Nice.
""")
