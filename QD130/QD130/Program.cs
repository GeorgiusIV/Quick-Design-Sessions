

class program
{
    public static void Main()
    {
        int[,] adjmat = new int[,] { { 0, Int32.MaxValue, -2, Int32.MaxValue },
                                     { 4, 0, 3, Int32.MaxValue },
                                     { Int32.MaxValue, Int32.MaxValue, 0, 2 },
                                     { Int32.MaxValue, -1, Int32.MaxValue, 0 } };

        FloydWarshall(adjmat);


    }
    public static void FloydWarshall(int[,] adjmat){

        int l = 4;

        
        int ukv;

        // intializing costs and path with infinities as necessary
        int[,] costs = new int[l,l];
        string[,] path = new string[l,l];
        for (int u = 0; u < l; u++)
            for (int v = 0; v < l; v++)
            {
                if (u == v)
                    costs[u,v] = 0;
                else if (adjmat[u,v] == 0)
                {
                    costs[u,v] = Int32.MaxValue;
                    path[u,v] = u.ToString();
                }
                else
                {
                    costs[u,v] = adjmat[u,v];
                    path[u,v] = u.ToString();
                }
            }

        // perform the algorithm
        for (int k = 1; k < l; k++)
            for (int v = 1; v < l; v++)
                for (int u = 0; u < l; u++)
                {
                    ukv = costs[u,k] + costs[k,v];
                    if (costs[u,v] < ukv)
                    {
                        costs[u,v] = ukv;
                        path[u,v] += v.ToString();

                    }
                }

        System.Console.WriteLine(path[0,3]);
    }

}






