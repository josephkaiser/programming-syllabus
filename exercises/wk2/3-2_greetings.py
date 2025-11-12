'''
3-2. Greetings

This is the accompanying code for PythonCrashCourse chapter 3 exercise 3-2.

Original Author: Joseph Kaiser
Creation Date: 11/2/2025
'''

def get_name_greeting(name):
    while True:
        greeting_mapping = {
            "jon": "Hey there, Jon, buddy.",
            "john": "How are you John, my guy?",
            "johnny": "Johnny, my man!",
            "jim": "Jim, how are you?",
            "jimbo": "Let's light these fireworks, Jimbo!",
            "jimmy": "Jimmy, go to your room.",
            "jimothy": "Jimothy can't be a real name.",
        }
        return greeting_mapping.get(name, "Invalid name.")

def main():
    names = ["jon", "john", "johnny", "jim", "jimbo", "jimmy", "jimothy"]
    for i in range(len(names)):
        print(f"{names[i].strip().title()}" + ": " + get_name_greeting(names[i]))

if __name__ == "__main__":
    main()
