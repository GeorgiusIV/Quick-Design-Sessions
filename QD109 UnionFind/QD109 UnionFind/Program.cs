





class DisjointSet
{
    public int _ids = 1;
    public DisjointSet parent;
    public char repr;

    public DisjointSet(char r = 'X')
    {
        _ids += 1;
        parent = this;
        repr = r;
    }

    public DisjointSet Find()
    {
        if (this == parent)
            return this;
        else
            return parent.Find();
    }

    public void Union(DisjointSet y)
    {
        parent = y;
    }
}

class Graph
{
    public bool[,] matrix;

    public Graph(bool[,] m)
    {
        matrix = m;
    }
}

class Program
 {

    public static bool UnionFind(Graph G)
    {

        for (int i = 0; i < 5; i++)
            return G.matrix[0, i];

        return false;
    }

    public static void Main()
    {
        bool[,] G1 = new bool[6,6] {
        { false, true, true, false, false, false },
        { true, false, false, true, false, false },
        { true, false, false, true, false, false },
        { false, true, true, false, true, true },
        { false, false, false, true, false, false },
        { false, false, false, true, false, false } };

        Graph G = new Graph(G1);

        System.Diagnostics.Debug.WriteLine(UnionFind(G));

    }



 }