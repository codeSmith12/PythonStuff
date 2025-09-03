'''
Python Level 3 - Lesson 8 - Objectifying our Game

Learning Objectives:
    - How can we take an existing code and "Objectify" it?
    - What are the benefits of doing this to our code? (Say goodbye to global variables!!)
    - Understand what refactoring is
    
   

Lesson Tasks:
    - Discuss what refactoring is
    - Talk about the benefits of "objectifying" our code, what the benefits are
    - Create the skeleton of the class, meaning make all of the function "signatures", this will show the desired format we are working towards
    - Begin the refactoring by creating all of the variables in the init function
    - Create a "BuildGUI" member function, have it go through the steps of building the GUI, remember that variables that aren't used outside of the function don't need to be member variables (no self.)
    - Test, then move on
    - Refactor Click, increment and update display functions.
    - Allow students to try to do the rest of the functions. It is a fairly repetetive task, they should be able to finish on their own
    - If there's extra time, talk about the dictionary data structure || Add the input field for taking in account names for saving and loading
    

Homework:
    Practice with dictionary object.
    Things to practice with dictionary
        - Syntax for creating {}
        - Adding items (during creation and after)
        - Removing items
        - Retreiving items
        - Know that dictionaries grab in O(1)-1 operation, super fast
        - Looping through dictionary
        
    Activity would probably involve a bunch of variables
    name="brian"
    age=32
    occupation="teacher"
    Now convert to dictionary
    
    human = {
        "name":"Brian",
        "age":32,
        "occupation":"Teacher"
    }
    # accessing data
    print(human["name"])
    print(human["age"])
    print(human["occupation"])

    #looping
    for key in human:
        print(human[key]) # No quotes as key == "name", "age", ect
    
    adding after creation:
        human["height"] = 70
    removing items
        print(human)
        del(human["height"]) - removes the element from the dictionary
        print(human) 

    
    

'''