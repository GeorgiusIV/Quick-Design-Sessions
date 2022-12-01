
class DisjointSet
{
    private DisjointSet parent;
    public char name;

    public DisjointSet(char name)
    {
        this.parent = this;
        this.name = name;
    }

    public DisjointSet Find()
    {
        if (this.parent == this)
            return this;
        else
            return this.Find();
    }

    public void Union(DisjointSet newParent)
    {
        this.parent = newParent;
    }
}



class Vertex
{
    public DisjointSet[] Edge;
    public DisjointSet self; 
    public char name;
    public Vertex(char v, params char[] E)
    {
        this.name = v;
        this.self = DisjointSet(v);
        foreach (char e in E)
            this.Edge[v] = DisjointSet(e);
    }
}

class Program
{
    public static void Main()
    {
        Vertex[] G = new Vertex[12];
        G['a'] = new Vertex('a', 'b', 'g', 'h');
        G['b'] = new Vertex('b', 'a', 'c', 'f');
        G['c'] = new Vertex('c', 'b', 'd', 'e');
        G['d'] = new Vertex('d', 'c');
        G['e'] = new Vertex('e', 'c');
        G['f'] = new Vertex('f', 'b');
        G['g'] = new Vertex('g', 'a');
        G['h'] = new Vertex('h', 'a', 'j', 'l');
        G['i'] = new Vertex('i', 'j', 'k', 'h');
        G['j'] = new Vertex('j', 'i');
        G['k'] = new Vertex('k', 'i', 'l');
        G['l'] = new Vertex('l', 'h', 'k');

        System.Diagnostics.Debug.WriteLine(UnionFind(G));
    }

    public static bool UnionFind(Vertex[] G)
    {

        List<Tuple<char, char>> travelled_edges = new List<Tuple<char, char>>();

        // search the edge set of u
        foreach (Vertex V in G)
        {
            // retrieve the DisjointSets from the Vertex
            DisjointSet v = V.self;
            foreach (DisjointSet u in V.Edge)
            {
                // initialize variables to check if the edge has been visited
                bool edge_travelled = false;
                Tuple<char, char> edge = new Tuple<char, char>(v.name, u.name);

                // check if the edge has already been visited in reverse
                foreach (Tuple<char, char> travelled_edge in travelled_edges)
                {
                    if (edge == travelled_edge)
                        edge_travelled = true;
                }

                // if the edge has not been travelled before, proceed with UnionFind
                if (!edge_travelled)
                    if (v.Find() == u.Find())
                        return true;
            }
        }

        return false;
    }

}


