
class Program
{
    public static void Main()
    {
        Graph G = new Graph(10);
        G.CreateVerts('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j');

        G.AddEdge(new Tuple<char, char, int>('a', 'b', 5));
        G.AddEdge(new Tuple<char, char, int>('a', 'd', 5));

        G.AddEdge(new Tuple<char, char, int>('b', 'a', 7));
        G.AddEdge(new Tuple<char, char, int>('b', 'c', 5));
        G.AddEdge(new Tuple<char, char, int>('b', 'd', 5));
        G.AddEdge(new Tuple<char, char, int>('b', 'e', 5));

        G.AddEdge(new Tuple<char, char, int>('c', 'b', 5));
        G.AddEdge(new Tuple<char, char, int>('c', 'e', 5));

        G.AddEdge(new Tuple<char, char, int>('d', 'a', 5));
        G.AddEdge(new Tuple<char, char, int>('d', 'b', 5));
        G.AddEdge(new Tuple<char, char, int>('d', 'e', 5));
        G.AddEdge(new Tuple<char, char, int>('d', 'f', 5));

        G.AddEdge(new Tuple<char, char, int>('e', 'b', 5));
        G.AddEdge(new Tuple<char, char, int>('e', 'c', 5));
        G.AddEdge(new Tuple<char, char, int>('e', 'd', 5));
        G.AddEdge(new Tuple<char, char, int>('e', 'f', 5));
        G.AddEdge(new Tuple<char, char, int>('e', 'g', 5));

        G.AddEdge(new Tuple<char, char, int>('f', 'b', 5));
        G.AddEdge(new Tuple<char, char, int>('f', 'b', 5));
        G.AddEdge(new Tuple<char, char, int>('f', 'b', 5));

        G.AddEdge(new Tuple<char, char, int>('g', 'b', 5));
        G.AddEdge(new Tuple<char, char, int>('g', 'b', 5));

        System.Diagnostics.Debug.WriteLine(G.Kruskal().Edges.Count);
    }
}


class DisjointSet
{
    public DisjointSet parent;
    public char name;

    public DisjointSet(char name)
    {
        this.name = name;
        this.parent = this;
    }

    public DisjointSet Find()
    {
        if (this == this.parent)
            return this;
        else
            return this.parent.Find();
    }

    public void Union(DisjointSet newParent)
    {
        this.parent = newParent;
    }
}

class Graph
{
    public DisjointSet[] Verts = new DisjointSet['z']; //this must be done in a better way by mapping 'a' to 1,
    public List<Tuple<DisjointSet, DisjointSet, int>> Edges = new List<Tuple<DisjointSet, DisjointSet, int>>();
    public int Size;

    public Graph(int size)
    {
        this.Size = size;
    }

    public void CreateVerts(params char[] names)
    {
        // construct new DisjointSets for each char
        foreach (char name in names)
        {
            this.Verts[name] = new DisjointSet(name);
        }
    }

    public void AddEdge(Tuple<char,char,int> edge)
    {
        // accept edges in the format (char,char,int)
        DisjointSet u = this.Verts[edge.Item1];
        DisjointSet v = this.Verts[edge.Item2];
        int w = edge.Item3;
         
        // construct a tuple containing the disjoint sets
        Tuple<DisjointSet, DisjointSet, int> newEdge = new Tuple<DisjointSet, DisjointSet, int>(u, v, w);

        // add the tuple to Edges
        this.Edges.Add(newEdge);
    }

    public void AddEdgeRaw(Tuple<DisjointSet, DisjointSet, int> edge)
    {
        // add the tuple to Edges
        this.Edges.Add(edge);
    }

    public void RemoveEdge(Tuple<char, char, int> edge)
    {
        // accept edges in the format (char,char,int)
        DisjointSet u = this.Verts[edge.Item1];
        DisjointSet v = this.Verts[edge.Item2];
        int w = edge.Item3;

        // construct a tuple containing the disjoint sets
        Tuple<DisjointSet, DisjointSet, int> newEdge = new Tuple<DisjointSet, DisjointSet, int>(u, v, w);

        // remove the tuple from edges
        this.Edges.Remove(newEdge);
    }

    public void RemoveEdgeRaw(Tuple<DisjointSet, DisjointSet, int> edge)
    {
        // remove the tuple from Edges
        this.Edges.Remove(edge);
    }



    public bool UnionFind()
    {
       
        foreach(Tuple<DisjointSet, DisjointSet, int> edge in this.Edges)
        {
            // collect the information for each edge, ignoring the weight
            DisjointSet u = edge.Item1;
            DisjointSet v = edge.Item2;

            // if two verts on an edge share the same parent, a cycle is found
            if (u.Find().parent == v.Find().parent)
            {
                return true;
            }
            // otherwise, union the sets
            else
                u.Union(v);
        }

        // if every edge is checked and no cycle is found, there are no cycles
        return false;
    }

    public List<int> MergeSort(List<int> lst)
    {

        // produce two pointers
        int start = 0;
        int end = lst.Count;

        // produce new lists L and R
        List<int> L = new List<int>();
        List<int> R = new List<int>();

        // if not atomic
        if (end > 1)
        {
            // find the midpoint between start and end
            decimal m = end / 2;
            int mid = (int)Math.Ceiling(m);

            // populate L and R around the midpoint
            for (int i = start; i < end; i++)
                if (i < mid)
                    L.Add(lst[i]);
                else
                    R.Add(lst[i]);

            // begin the recursion, on the way back up, follow the rest of this code
            L = MergeSort(L);
            R = MergeSort(R);

            // apply selection sort to reorder and combine the two lists
            lst = new List<int>();

            int r = R[0];
            int l = L[0];

            while (R.Count > 0 | L.Count > 0)
            {
                if (l < r)
                {
                    // if l is strictly less than r, add it to the list first
                    lst.Add(l);
                    try
                    {
                        l = L[0];
                        L.RemoveAt(0);
                    }
                    catch (ArgumentOutOfRangeException)
                    {
                        l = int.MaxValue;
                    }

                }
                else if (l == int.MaxValue & r == int.MaxValue)
                {
                    // when both values are infinity, the else would append one of them
                    break;
                }
                else
                {
                    // if r is equal to or less then l, add it to the list first
                    lst.Add(r);
                    try
                    {
                        r = R[0];
                        R.RemoveAt(0);
                    }
                    catch (ArgumentOutOfRangeException)
                    {
                        r = int.MaxValue;
                    }
                }
            }
            System.Diagnostics.Debug.WriteLine("THE LIST LENGTH IS:",lst.Count.ToString());
            // return a single list
            return lst;
        }
        // the list is length one it cannot be divided more
        else
        {
            return lst;
        }
    }

    public List<Tuple<DisjointSet, DisjointSet, int>> SortEdges()
    {

        // read the weights, w into a List W
        List<int> W = new List<int>();
        foreach(Tuple<DisjointSet,DisjointSet,int> edge in this.Edges)
        {
            int w = edge.Item3;
            W.Add(w);
        }

        // sort W
        //List<int> A = MergeSort(W);
        List<int> A = W.Sort(W);

        // take the first entry in W, for comparison in the while loop
        int a = A[0];
        A.RemoveAt(0);

        // initialize the set to return after the upcoming mapping is complete
        List<Tuple<DisjointSet, DisjointSet, int>> sortedE = new List<Tuple<DisjointSet, DisjointSet, int>>();

        // populate Sorted E in the order of A, by selecting the weight from this.Edges
        while (A.Count > 0)
        {
            foreach (Tuple<DisjointSet, DisjointSet, int> edge in this.Edges)
            {
                int w = edge.Item3;
                if (w == a)
                {
                    sortedE.Add(edge);
                    a = A[0];
                    A.RemoveAt(0);
                    break;
                }
            }
        }

        return sortedE;
    }


    public Graph Kruskal()
    {
        // make a new graph to add edges to
        Graph MST = new Graph(this.Size);

        // sort the edge set
        List<Tuple<DisjointSet, DisjointSet, int>> sortedEdges = this.SortEdges();

        // determine if each edge is sorted, mapped, and if there is a cycle
        foreach (Tuple<DisjointSet, DisjointSet, int> edge in sortedEdges)
        {
            MST.AddEdgeRaw(edge);
            if (MST.UnionFind())
                MST.RemoveEdgeRaw(edge);
        }

        return MST;
    }


}






