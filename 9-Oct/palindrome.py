def is_palindrome(user_inp):
    user_inp = ''.join(user_inp.split()).lower()
    return user_inp == user_inp[::-1]

if __name__ == "__main__":
    user_inpt = input("Enter the String: ")
    result = is_palindrome(user_inpt)
    print(result)
