class Palindrome:        
    def get_normal_str(self, num):
        return str(num)
    
    def get_reversed_str(self, num):
        forward_str = str(num)
        reversed_str = forward_str[::-1]  # [::-1] reverses the string
        return reversed_str
    
    def run(self, num):        
        forward_str = Palindrome().get_normal_str(num)
        reversed_str = Palindrome().get_reversed_str(num)
        
        if (forward_str == reversed_str):  # Compare strings for equality
            print("Yes, {} IS a palindrome.".format(num))
        else:
            print("No, {} IS NOT a palindrome.".format(num))

if __name__ == '__main__':
    user_num = input("Enter a word or number: ")
    Palindrome().run(user_num)