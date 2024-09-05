/*Hudson Stovall
Assignment 2
Rope-A-Dope*/

#include <iostream>
#include <memory>
#include <string>

using namespace std;

class RopeNode 
{
public:
    int weight;
    shared_ptr<RopeNode> left;
    shared_ptr<RopeNode> right;
    string str;
    RopeNode(int weight, shared_ptr<RopeNode> left, shared_ptr<RopeNode> right)
        : weight(weight), left(left), right(right) {}

    RopeNode(const string &str) : weight(str.length()), str(str), left(nullptr), right(nullptr) {}
};

class Rope 
{
private:
    shared_ptr<RopeNode> root;
    char indexHelper(shared_ptr<RopeNode> node, int i) 
    {
        if (!node) return '\0';
        if (!node->left && !node->right) 
        {
            return node->str[i];
        }
        if (i < node->weight) 
        {
            return indexHelper(node->left, i);
        } 
        else 
        {
            return indexHelper(node->right, i - node->weight);
        }
    }

    shared_ptr<RopeNode> concatHelper(shared_ptr<RopeNode> left, shared_ptr<RopeNode> right) 
    {
        int leftWeight = left ? left->weight : 0;
        return make_shared<RopeNode>(leftWeight, left, right);
    }

public:
    Rope(const string &str) 
    {
        root = make_shared<RopeNode>(str);
    }

    char index(int i) 
    {
        return indexHelper(root, i);
    }

    void concat(Rope &other) 
    {
        root = concatHelper(root, other.root);
    }

    pair<Rope, Rope> split(int i) 
    {
        return {Rope(""), Rope("")};
    }

    void insert(int i, const string &s) 
    {
        auto parts = split(i);
        Rope newRope(s);
        parts.first.concat(newRope);
        parts.first.concat(parts.second);
        root = parts.first.root;
    }

    void deleteRange(int start, int length) 
    {
        auto parts1 = split(start);
        auto parts2 = parts1.second.split(length);
        parts1.first.concat(parts2.second);
        root = parts1.first.root;
    }

    Rope subrope(int i, int j) 
    {
        auto parts = split(i);
        auto subparts = parts.second.split(j - i);
        return subparts.first;
    }

    void print(shared_ptr<RopeNode> node) 
    {
        if (!node) return;
        if (!node->left && !node->right) 
        {
            cout << node->str;
        } 
        else 
        {
            print(node->left);
            print(node->right);
        }
    }

    void print() 
    {
        print(root);
        cout << endl;
    }
};

int main() 
{
    Rope rope("Hello ");
    Rope rope2("World!");
    rope.concat(rope2);
    rope.print();
    cout << "A character at the index of 4: " << rope.index(4) << endl;
    rope.insert(6, "Amazing ");
    rope.print();
    rope.deleteRange(6, 8);
    rope.print();
    Rope sub = rope.subrope(0, 5);
    sub.print();
    return 0;
}
