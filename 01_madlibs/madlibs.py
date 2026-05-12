# # #string concatenation - how can we put strings together?
# # #we can use the + operator to concatenate strings
# # #example
# # print("Hello " + "world!")

# # #we can also use variables to store strings and concatenate them
# # name = "Jewel"
# # print("Hello, " + name + "!")

# # #using format{} method to concatenate strings
# # age = 22
# # print("My name is {} and I am {} years old.".format(name, age))

# # #using f-strings to concatenate strings(most simple and recommended way)
# # print(f"My name is {name} and I am {age} years old.")

# adjective1 = input("Enter an adjective: ")
# verb1 = input("Enter a verb: ")
# verb2 = input("Enter another verb: ")
# famous_person = input("Enter the name of a famous person: ")

# madlib = f"Computer programming is so {adjective1}! It makes me so excited all the time because I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

# print(madlib)

adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
adjective3 = input("Enter one more adjective: ")
verb1 = input("Enter a verb: ")
verb2 = input("Enter another verb: ")
verb3 = input("Enter one more verb: ")
verb4 = input("Enter one more verb: ")
noun1 = input("Enter a noun: ")
noun2 = input("Enter another noun: ")
noun3 = input("Enter one more noun: ")
noun4 = input("Enter one more noun: ")
plural_noun1 = input("Enter a plural noun: ")
plural_noun2 = input("Enter another plural noun: ")
special_place = input("Enter a special place: ")
special_food = input("Enter a special food: ")
spelling_mistake = input("Enter a common spelling mistake: ")
negative_emotion = input("Enter a negative emotion: ")
positive_emotion = input("Enter a positive emotion: ")
decision = input("Enter a decision: ")
dog_breed = input("Enter a dog breed: ")
cat_breed = input("Enter a cat breed: ")
nasa_mission = input("Enter a NASA mission: ")

madlib = f"Today I went to the zoo and saw a {adjective1} {noun1} {verb1}ing in the {special_place}. It was so {adjective2}! Then I saw a {adjective3} {noun2} {verb2}ing with a {noun3}. It was the best day ever! I can't wait to go back and see the {plural_noun1} and {plural_noun2}. Maybe I'll even get to eat some {special_food} while I'm there. I hope I don't make any {spelling_mistake}s while I'm there, or else I'll feel really {negative_emotion}. But overall, I'm feeling really {positive_emotion} about this trip. I think it was a great decision to go to the zoo today! Maybe next time I'll bring my {dog_breed} or my {cat_breed} along for the fun. Or maybe I'll even go on a trip to space with NASA's next mission, {nasa_mission}!" 

print(madlib)

#output:
# Enter an adjective: fun
# Enter another adjective: exciting
# Enter one more adjective: amazing
# Enter a verb: run
# Enter another verb: jump
# Enter one more verb: swim
# Enter one more verb: fly
# Enter a noun: lion
# Enter another noun: monkey
# Enter one more noun: giraffe
# Enter one more noun: elephant
# Enter a plural noun: zebras
# Enter another plural noun: flamingos
# Enter a special place: jungle
# Enter a special food: ice cream
# Enter a common spelling mistake: definately
# Enter a negative emotion: sad
# Enter a positive emotion: happy
# Enter a decision: go to the zoo
# Enter a dog breed: golden retriever
# Enter a cat breed: siamese
# Enter a NASA mission: Artemis
# Today I went to the zoo and saw a fun lion running in the jungle. It was so exciting! Then I saw a amazing monkey jumping with a giraffe. It was the best day ever! I can't wait to go back and see the zebras and flamingos. Maybe I'll even get to eat some ice cream while I'm there. I hope I don't make any definatelys while I'm there, or else I'll feel really sad. But overall, I'm feeling really happy about this trip. I think it was a great decision to go to the zoo today! Maybe next time I'll bring my golden retriever or my siamese along for the fun. Or maybe I'll even go on a trip to space with NASA's next mission, Artemis!


