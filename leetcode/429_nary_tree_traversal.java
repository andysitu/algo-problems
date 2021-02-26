import java.util.*;


// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};


class Solution {
    public List<List<Integer>> l;
    
    private void travel(Node node, int level) {
        if (l.size() < level) {
            l.add(new ArrayList<Integer>());
        }
        List<Integer> li = l.get(level - 1);
        li.add(node.val);
        if (node.children != null) {
            for (int i = 0; i < node.children.size(); i++) {
                travel(node.children.get(i), level + 1);
            }
        }
    }
    
    public List<List<Integer>> levelOrder(Node root) {
        l = new ArrayList<>();
        travel(root, 1);
        return l;
    }
}