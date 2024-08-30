def count_words(text):
    """
    Counts the number of words in the given text.

    Args:
    text (str): The text to count words in. 
    Returns:
    int: The number of words in the text.
    """

    # This line splits the text into a list of words based on spaces.
    words = text.split()

    # This returns the number of words by finding out how many items are in the list.
    return len(words)

def main():
    # This prints the title for the program.
    print("Word Counter Program")
    print("--------------------")

    # This line asks the user to type in a sentence or paragraph. 
    # It also removes any extra spaces at the beginning or end of what they typed.
    user_input = input("Please enter a sentence or paragraph: ").strip()

    # check if the user didn't type anything.
    if not user_input:
        # If they didn't type anything, we let them know that they need to enter some text.
        print("Error: No input provided. Please enter some text.")
        # The program stops here if there's no input.
        return
    
    # This calls the count_words function to count how many words are in the text the user provided.
    word_count = count_words(user_input)

    # Finally, this prints the number of words back to the user.
    print(f"Word Count: {word_count} words")
    
# This checks if the script is being run directly (not imported into another script).
if __name__ == "__main__":
    # If the script is being run directly, the main function is called to start the program.
    main()
