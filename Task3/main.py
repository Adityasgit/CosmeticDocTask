from gpt import *
if __name__ == "__main__":
    # Ask the user to input a prompt
    user_prompt = input("Enter a prompt to generate a story: ")

    # Generate and display the story
    generate_story(user_prompt)