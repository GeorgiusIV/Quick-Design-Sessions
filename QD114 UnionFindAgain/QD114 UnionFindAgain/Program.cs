


class DisjointSet
{ 
    public char name;
    public DisjointSet(char name)
    {
        this.name = name;
    }
}

class Vertex
{
    public char name;
    public DisjointSet set;
    public Vertex[] connections;
    public Vertex(char name)
    {
        this.name = name;
        this.set = new DisjointSet(name);
        //this.connections = connections;
    }

    public Vertex TravelTo(char destination)
    {
        return this.connections[destination];
    }

}


class Graph
{
    public Vertex[] Verts;
    public Tuple<char, char>[] Edges;

    public void NewEdge(Tuple<char,char>[] edges)
    {
        char name = new char();
        foreach (Tuple<char, char> edge in edges)
            name = edge.Item1;
            this.Verts[name] = new Vertex(name);

    }
}




