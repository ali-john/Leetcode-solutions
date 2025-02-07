struct Node{
    int key;
    int value;
    Node* next;
    Node(){
        value = INT_MIN;
        key = INT_MIN;
        next = nullptr;
    }
};

class MyHashMap {
public:
    vector<Node*> table;
    int n = 10000;
    MyHashMap() {
        table.resize(10000,nullptr);
    }
    
    int find_hash(int val){
        return val%n;
    }
   
    void put(int key, int value) {
        int key_hash = find_hash(key);
        
        if (table[key_hash]==nullptr) // nothing yet
        {
            Node* new_node = new Node();
            new_node->value = value;
            new_node->key = key;
            new_node->next = nullptr;
            table[key_hash] = new_node;
        }
        else // already node exists, update the data
        {
            Node* curr = table[key_hash];
            while (curr->next)
            {
                if (curr->key == key){
                    curr->value = value;
                    return;
                }
                curr = curr->next;
            }
            if (curr->key == key){
                curr->value = value; return;
            }
            Node* new_node = new Node();
            new_node->key = key;
            new_node->value = value;
            curr->next = new_node;
            new_node->next = nullptr;
        }

    }
    
    int get(int key) {
        int hash_key = find_hash(key);
        if (table[hash_key]==nullptr) return -1;
        Node* curr = table[hash_key];
        while (curr){
            if (curr->key == key) return curr->value;
            curr = curr->next;
        }
        return -1;
    }
    
    void remove(int key) {
        int hash_key = find_hash(key);
        if (table[hash_key]==nullptr) return;
        Node* curr = table[hash_key];
        Node* prev = nullptr;

        while (curr){
            if (curr->key == key){
                if (prev) prev->next = curr->next;
                else table[hash_key] = curr->next;
                delete curr;
                return;
            }
            prev = curr;
            curr = curr->next;
        }
        
        
        
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */
