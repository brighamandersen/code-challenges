def is_palindrome(word):
	frontIndex = 0
	backIndex = len(word) - 1

	while (frontIndex < backIndex):
		if word[frontIndex] != word[backIndex]:
			return False

		frontIndex += 1
		backIndex -= 1
	return True

def main():
    wordToCheck = "racecar"

    if is_palindrome(wordToCheck):
    	print("Yes, it's a palindrome")
    else:
    	print("Nope, it's not a palindrome")

if __name__ == "__main__":
    main()