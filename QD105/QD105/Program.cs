using System;

class Program
{
    static bool binarySearch(int tofind, List<int> inlist)
    {

        // if the list length is greater than one, split the list
        int length = inlist.Count;
        if (length > 1) 
        {
            // find the midpoint of the list
            int mid = System.Math.Ceiling(length / 2);

            // define two new lists for the splits, L and R
            List<int> L = new List<int>();
            List<int> R = new List<int>();

            // split the original list and populate L and R
            foreach (int num in inlist)
                if (num < mid)
                    L.Add(num); 
                else
                    R.Add(num);

            // recall the function on L and R, which will return True or False
            bool left_bool = binarySearch(tofind, L);
            bool right_bool = binarySearch(tofind, R);

            // if either L or R return True, tofind is contained within the main list
            return left_bool || right_bool;
        }

        // if the list length is one, get the last remaining value
        int x = inlist.RemoveAt(0);
        if (x == tofind)
            return true;
        else
            return false;
    }

    public static void Main()
    {
        // test 1, find 7
        List<int> test1 = new List<int> { 2, 3, 5, 7, 9 };

        // test 2, find 2
        List<int> test2 = new List<int> { 1, 4, 5, 8, 9 };

        binarySearch(7, test1);
        binarySearch(2, test2);
    }
    
}

