public class Palindrome {
	public boolean isPalindrome(String word) {
		int frontIndex = 0;
		int backIndex = word.length() - 1;

		while (frontIndex < backIndex) {
			if (word.charAt(frontIndex) != word.charAt(backIndex)) {
				return false;
			}
			frontIndex++;
			backIndex--;
		}
		return true;
	}
}