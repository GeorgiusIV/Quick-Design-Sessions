
using System.Collections.Generic;



class Prog
{
    public Queue<char> DFS(char p, IDictionary<char, List<char>> G)
    {
        Stack<char> tovisit = new Stack<char>();
        Queue<char> visited = new Queue<char>();

        // begin loop at the parent node p
        tovisit.Push(p);
        while (tovisit.Count > 0)
        {

            // get p and if it is not visited:
            p = tovisit.Pop();
            if (visited.Contains(p) is false)
            {
                // visit p and add its children to tovisit
                visited.Enqueue(p);
                foreach (char child in G[p])
                    tovisit.Push(child);
            }
        }

        return visited;
    }

    public static void Main() 
    {
        IDictionary<char, List<char>> Graph = new Dictionary<char, List<char>>();
        Graph.Add('a', new List<char> { 'b', 'c', 'd' });
        Graph.Add('b', new List<char> { 'e', 'f' });
        Graph.Add('c', new List<char> { });
        Graph.Add('d', new List<char> { 'g', 'h' });
        Graph.Add('e', new List<char> { 'i', 'j' });
        Graph.Add('f', new List<char> { });
        Graph.Add('g', new List<char> { 'k', 'l' });
        Graph.Add('h', new List<char> { });
        Graph.Add('i', new List<char> { });
        Graph.Add('j', new List<char> { });
        Graph.Add('k', new List<char> { });
        Graph.Add('l', new List<char> { });

        Prog prog = new Prog();
        foreach (char q in prog.DFS('a', Graph))
            Console.WriteLine(q);
    }
}






