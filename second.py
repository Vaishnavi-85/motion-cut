print("Python Programming Project 2: Word Counter.\n")

def main():  # Define the main function
    while True:
        s = input("Enter a sentence or a paragraph: ").strip() # Prompt the user to enter a sentence or paragraph, and strip leading or trailing spaces
        if not s:         # Check if the input is empty
            print("Input string cannot be empty.")
            continue  # Restart the loop for new input
        c = len(s.split()) # Calculate the word count by splitting the string into words and getting the length of the resulting list
        print(f"Word count is: {c}\n") # Print the word count result
        break # Exit the loop after successfully processing the input

if __name__ == "__main__":
    main()  # Call the main function
