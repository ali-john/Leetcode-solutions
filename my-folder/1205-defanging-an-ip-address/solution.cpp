class Solution {
public:
    string defangIPaddr(string address) {
        int n = address.size();
        string new_address = "";
        for (int i =0; i<n; i++)
        {
            if ( address[i] == '.')
                new_address+="[.]";
            else
                new_address+=address[i];
        }
        return new_address;
    }
};
