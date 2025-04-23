def is_palindrome(text):
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    user_input = input("Enter a word or sentence: ")
    if is_palindrome(user_input):
        print("It is a palindrome.")
    else:
        print("It is not a palindrome.")
