struct Node{
    int key;
    Node* next;
    Node(){
        next = nullptr;
        key = INT_MIN;
    }
};

class MyHashSet {
public:
    int n = 10000;
    vector<Node*> table;
    MyHashSet() {
        table.resize(n,nullptr);
    }
    
    int get_hash(int val){
        return val%n;
    }

    void add(int key) {
        int hash_key = get_hash(key);
        if (table[hash_key]==nullptr){
            Node* new_node = new Node();
            new_node->key = key;
            table[hash_key] = new_node;
        }
        else{
            Node* curr = table[hash_key];
            while (curr){
                if (curr->key == key) return;
                if (curr->next == nullptr) break;
                curr = curr->next;
            }
            if (curr->key == key) return;
            Node* new_node = new Node(); new_node->key = key;
            curr->next = new_node;
            return;
        }
        
    }
    
    void remove(int key) {
        int hash_key = get_hash(key);
        if (table[hash_key] == nullptr) return;
        Node* curr = table[hash_key];
        Node* prev = nullptr;

        while (curr){
            if (curr->key == key){
                if (prev){
                    prev->next = curr->next;
                    delete curr;return; 
                }
                else{ // delete from start
                    table[hash_key] = curr->next;
                    delete curr; return;
                }
            }
            prev = curr;
            curr = curr->next;
        }
        return;

        
    }
    
    bool contains(int key) {
        int hash = get_hash(key);
        if (table[hash] == nullptr) return false;

        Node* curr = table[hash];
        while (curr){
            if (curr->key == key) return true;
            curr = curr->next;
        }
        return false;
        
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */
