

class program
{

    List<List<bool>> edgeMatrix = new List<List<bool>>();
    List<bool> edgeList = new List<bool> { };
    //edgeMatrix.add( )


    public static void Main()
    {
        List<DisjointSet> Graph = new List<DisjointSet> { new DisjointSet('a'), new DisjointSet('b'), new DisjointSet('c'), new DisjointSet('d'), new DisjointSet('e') };

        foreach  (DisjointSet djSet in Graph)
        {
            djSet.Union();
        }
    }

    

}
class DisjointSet
{

    public char parent;

    public DisjointSet(char x)
    {
        parent = x;
    }

    public char Find(char x)
    {
        if (x == parent)
            return x;
        else
            return Find(parent);
    }

    public void Union(DisjointSet y)
    {
        parent = y.parent;
    }
}
