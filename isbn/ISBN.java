
/* Write a well-documented (commented) program, ISBN, that takes a 9-digit integer as a 
command-line argument, computes the checksum, and prints the ISBN number. [MO4.1]

Note: You should use Java’s String data type to implement it. The International Standard
 Book Number (ISBN) is a 10-digit code that uniquely specifies a book. The rightmost digit 
 is a checksum digit that can be uniquely determined from the other 9 digits, from the 
 condition that d1 + 2d2 +3d3 + ... + 10d10 must be a multiple of 11 (here di denotes the ith digit 
 from the right).

The checksum digit d1 can be any value from 0 to 10. The ISBN convention is to use the 
character X to denote 10. The checksum digit corresponding to 032149805 is 4 since 4 is 
the only value of x between 0 and 10 (both inclusive), 
for which 10·0 + 9·3 + 8·2 + 7·1 + 6·4 + 5·9 +4·8 +3·0 + 2·5 + 1·x is a multiple of 11.

Sample runs would be as follows.

>java ISBN 013376940
The ISBN number would be 0133769402

>java ISBN 013380780
The ISBN number would be 0133807800   */

import java.util.Scanner;
	
public class ISBN {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		String numStr = input.next();
		int result = computeChecksum(numStr);

		System.out.println("The ISBN number would be " + makeIsbnNum(numStr, result));		
	}
	
	static int computeChecksum(String numStr) {

		int sum = 0;
		for (int i = 0; i <= 8; i++) {
			int multiplier = 10 - i;
			int numAtIndex = Character.getNumericValue(numStr.charAt(i));
			sum = sum + multiplier * numAtIndex;
		}

		int remainder = sum % 11;

		return 11 - remainder;
	}

	static String makeIsbnNum(String numStr, int checksum) {
		String checksumStr = stringifyChecksum(checksum);

		return numStr + checksumStr;
	}

	static String stringifyChecksum(int checksum) {
		if (checksum == 10) {
			return "X";
		}
		if (checksum == 11) {
			return "0";
		}
		return String.valueOf(checksum);
	}
}       