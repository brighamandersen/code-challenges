/*
Modify the MergeSort program given in the textbook (program 4.2.6) to support 
searching subarrays. [MO5.2, MO5.3]

Note: The user would give an unsorted list of words as command-line arguments
 along with the starting and ending index of the subarray that should be sorted. 
 The program should print out a list where the strings between the given indexes 
 are sorted alphabetically.

Sample runs would be as follows.

>java MergeSort 2 4 toy apply sand bay cat dog fish
toy apply bay cat sand dog fish

>java MergeSort 0 3 was had him and you his the but
and had him was you his the but  */

public class Merge

{
   public static void sort(Comparable[] a)
   {
      Comparable[] aux = new Comparable[a.length];
      sort(a, aux, 0, a.length);
   }

   private static void sort(Comparable[] a, Comparable[] aux,
                            int lo, int hi)
   {  // Sort a[lo, hi).
      if (hi - lo <= 1) return;
      int mid = lo + (hi-lo)/2;
      sort(a, aux, lo, mid);
      sort(a, aux, mid, hi);
      int i = lo, j = mid;
      for (int k = lo; k < hi; k++)
         if      (i == mid)  aux[k] = a[j++];
         else if (j == hi)   aux[k] = a[i++];
         else if (a[j].compareTo(a[i]) < 0) aux[k] = a[j++];
         else                               aux[k] = a[i++];
      for (int k = lo; k < hi; k++)
         a[k] = aux[k];
   }

   public static void main(String[] args)
   {  /* See Program 4.2.4. */  }
}