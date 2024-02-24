class RandomizedSet {
public:
    unordered_map<int,int>umap;
    RandomizedSet() {}
    
    bool insert(int val) {
        bool dec = false;
        if (umap.find(val)==umap.end())
        {
            umap[val] = val;
            return true;
        }
        else
        {
            return false; 
        }

        
    }
    
    bool remove(int val) {
        if (umap.find(val)==umap.end()) //value does not exists
        {
            return false;
        }
        else
        {
            umap.erase(val);
            return true;
        }
        
    }
    
    int getRandom() {
        auto it = umap.begin();
        advance(it, rand() % umap.size());

        return it->second;
        
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */