public class Main {
	public static void main(String[] args) {
		Palindrome palindrome = new Palindrome();

		String wordToCheck = "racecar";

		if (palindrome.isPalindrome(wordToCheck)) {
			System.out.println("Yes, it's a palindrome.");
		} else {
			System.out.println("Nope, it's not a palindrome.");
		}
	}
}