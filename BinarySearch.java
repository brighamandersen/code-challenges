/*
Modify the BinarySearch program given in the textbook (program 4.2.3) 
so that if the search key is in the array, it returns the largest index i
 for which a[i] is equal to key, but, otherwise, returns –i where i is the
 largest index such that a[i] is less than key. It should also be modified
 to deal with integer arrays rather than string arrays. [MO5.2, MO5.3]

Note: The program should take two command-line arguments,
 (1)an input file that contains a sorted integer array; and 
(2)an integer to search for in that array.

Sample runs would be as follows.

>more input.txt
2 3 4 5 6 6 6 7 8 9 11

>java BinarySearch input.txt 10
-9

>java BinarySearch input.txt 6
6      
*/
 
 public class BinarySearch
{
   public static int search(String key, String[] a)
   {  return search(key, a, 0, a.length);  }

   public static int search(String key, String[] a, int lo, int hi)
   {  // Search for key in a[lo, hi).
      if (hi <= lo) return -1;
      int mid = lo + (hi - lo) / 2;
      int cmp = a[mid].compareTo(key);
      if      (cmp > 0) return search(key, a, lo, mid);
      else if (cmp < 0) return search(key, a, mid+1, hi);
      else              return mid;
   }

   public static void main(String[] args)
   {  // Print keys from standard input that
      // do not appear in file args[0].
      In in = new In(args[0]);
      String[] a = in.readAllStrings();
      while (!StdIn.isEmpty())
      {
         String key = StdIn.readString();
         if (search(key, a) < 0) StdOut.println(key);
      }
   }
}
