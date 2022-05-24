#include <iostream>
using namespace std;


struct ListNode{
    int val;
    ListNode* next;
    ListNode(int x):val(x),next(nullptr){}
};
class MyLinkedList{
public:

    MyLinkedList();
    ~MyLinkedList();

    int get(int index){
        if(index >= _size || index < 0){
            return -1;
        }
        ListNode* curr = _Head -> next;
        while(index--){
            curr = curr -> next;
        }
        return curr -> val;
    }

    void addAtHead(int val){
            ListNode * newNode = new ListNode(val);
            newNode -> next = _Head -> next;
            _Head -> next = newNode;
            _size ++;
    }
    void addAtTail(int val){
        ListNode * newNode = new ListNode(val);
        ListNode * curr = _Head;
        while (curr -> next != nullptr){
            curr = curr -> next;
        }
        _Head -> next = newNode;
        _size ++;
    }
    void addAtIndex(int index, int val){
        if (index > _size){
            return;
        }
        if (index < 0){
            index = 0;
        }
        ListNode *newNode = new ListNode(val);
        ListNode * curr = _Head;
        while (index --){
            curr = curr -> next;
        }
        newNode -> next = curr -> next;
        curr -> next = newNode;
        _size ++;
    }
    void deleteAtIndex(int index){
        if (index > _size){
            return;
        }
        ListNode *curr = _Head;
        while (index --){
            curr = curr -> next;
        }
        ListNode *temp = curr;
        curr -> next = curr -> next -> next;
        delete temp;
        _size --;
    }
    
private:
    int _size;
    ListNode* _Head;
};

MyLinkedList::MyLinkedList(){
        _size = 0;
        _Head = new ListNode(0);}
MyLinkedList::~MyLinkedList(){}

int main(){
    // a = ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
    MyLinkedList s = MyLinkedList();
    s.addAtHead(1);
    s.addAtTail(3);
    s.addAtIndex(1,2);
    cout << s.get(1) << endl;
    s.deleteAtIndex(1);
    cout << s.get(1) << endl;
}