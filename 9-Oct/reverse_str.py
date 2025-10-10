def reverse_string(user_inp):
    return user_inp[::-1]

if __name__ == "__main__":
    user_inpt = input("Enter the string: ")
    result = reverse_string(user_inpt)
    print(result)
