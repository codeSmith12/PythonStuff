question_dictionary = {"geo1":"What is the capital of France?",
                       "geo2": "sdlkfjslkdfjs",
                       "geo3": "lksdjflkjsdfljksd",
                       }
answer_dictionary = {"geo1": "Paris"}

question = input("What question do you want?")
answer = input(question_dictionary[question])
if answer == answer_dictionary[question]:
    print("You got it")

scores = {"geo1": 100}

def myFunction():
    print("Do thingds here ")
    
myFunction()