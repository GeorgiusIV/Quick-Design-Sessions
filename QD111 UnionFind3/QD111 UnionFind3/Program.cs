

class DisjointSet
{
    DisjointSet parent;
    public DisjointSet()
    {
        parent = this;
    }

    public DisjointSet Find()
    {
        if (parent == this)
            return this;
        else
            return this.Find().parent;
    }

    public DisjointSet Union(DisjointSet newParent, bool inplace = false)
    {
        parent = newParent;
        if (inplace == true)
            return parent;
    }
}


class Vertex
{
    List<char> Edges = new List<char>();
    public Vertex(params char[] E)
    {
        foreach (char e in E)
        {
            Edges.Add(e);
        }
    }
}




class Program
{
    public static void Main()
    {
        int i = 0;
        Vertex[] Graph = new Vertex[10];
        // 1 = a,2 = b,3 = c,4 = d,5 = e,6 = f,7 = g,8 = h,9 = i,10 = j,11 = k
        Graph['a'] = new Vertex('b', 'g', 'h');
        Graph['b'] = new Vertex('c', 'f');
        Graph['c'] = new Vertex(4,5);
        Graph['d'] = new Vertex(3);
        Graph['e'] = new Vertex(3);
        Graph['f'] = new Vertex(2);
        Graph['g'] = new Vertex(1);
        Graph['h'] = new Vertex(1,9,12);
        Graph['i'] = new Vertex(8,10,11);
        Graph['j'] = new Vertex(9);
        Graph['k'] = new Vertex(9,12);
        Graph['l'] = new Vertex(11,8);


        // i want to index by characters, i also want a list of disjoint sets


    }
}




