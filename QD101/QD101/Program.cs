
using System;
using System.Collections.Generic;
using System.Collections;

class Program
{
    static List<char> BFS(G, char v)
    {
        // initialize a queue of to-be-visited Q, and have-been-visited V, vertices
        Queue<char> Q = new Queue<char>();
        Queue<char> V = new Queue<char>();

        // append v to Q
        Q.Enqueue(v);
        while (Q.Count > 0)
        {
            // if v has not been visited
            if (V.Contains(v)) 
            {
                // append to Q, each vertex connected connected to v
                foreach (char g in G[v])
                    Q.Enqueue(g);

                // append v to the Visited nodes
                V.Enqueue(v);
            }
            
            // get the next v from the Queue
            v = Q.Dequeue();
        }
    
        // return all Visited nodes
        return V;
    }
    static void Main()
    {
        Dictionary<char, List<char>> G = new Dictionary<char, List<char>>();
    
        G['a'] = new List<char> { 'b', 'e', 'd' };
        G['b'] = new List<char> { 'a', 'c' };
        G['c'] = new List<char> { 'b', 'f' };
        G['d'] = new List<char> { 'a', 'h' };
        G['e'] = new List<char> { 'a', 'f' };
        G['f'] = new List<char> { 'c', 'e', 'g' };
        G['g'] = new List<char> { 'f', 'h' };
        G['h'] = new List<char> { 'd', 'g' };
    
        Console.WriteLine(BFS(G, 'a'));
    }

}