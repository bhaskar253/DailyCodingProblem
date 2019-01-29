/*
# Problem Stmt.:
# An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields,
# it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; 
# it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.
# If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and 
# dereference_pointer functions that converts between nodes and memory addresses.
*/
#include <iostream>

using namespace std;

struct Node{
    int data;
    Node* both;
    Node(int data){
        this->data = data;
        both = nullptr;
    }
};

class XorLinkedList{
    Node *head;
    int size;
    Node* XOR(Node *a, Node *b) {
        return (Node*)((uintptr_t)(a) ^ (uintptr_t)(b));
    }
public:
    XorLinkedList(){
        head = nullptr;
        size = 0;
    }
    void add(int element);
    int get(int index);
    int getSize() {return size;}
    void printList(){
        Node *curr=head, *prev=nullptr, *next;
        while(curr!=nullptr){
            cout << curr->data << " ";
            next = XOR(prev, curr->both);
            prev = curr;
            curr = next;
        }
        cout << "\n";
    }
};

void XorLinkedList::add(int element){
    Node *newNode = new Node(element);
    size++;
    newNode->both = XOR(head,nullptr);
    if(head != nullptr) {
        Node *both = XOR(head->both,nullptr);
        head->both = XOR(newNode,both); 
    }
    head = newNode;
}

int XorLinkedList::get(int index) {
    index = size - (index + 1);
    Node *curr=head, *prev=nullptr, *next;
    while(curr!=nullptr && index>0) {
        next = XOR(prev, curr->both);
        prev = curr;
        curr = next;
        index--;
    }
    return curr->data;
}

int main() {
    XorLinkedList ll;
    ll.add(12);
    ll.add(21);
    ll.add(3);
    cout << ll.get(2) << endl;
    return 0;
}
