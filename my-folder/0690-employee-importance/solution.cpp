/*
// Definition for Employee.
class Employee {
public:
    int id;
    int importance;
    vector<int> subordinates;
};
*/

class Solution {
public:
    int getImportance(vector<Employee*> employees, int id) {
        unordered_map<int, pair<int, vector<int>>> graph; // id,importance -> subordinates
        for (auto employee:employees)
        {   int id_ = employee->id;
            int imp = employee->importance;
            vector<int> sub = employee->subordinates;
            graph[id_] = make_pair(imp,sub);
        }
        int count = 0;

        queue<int> q;
        q.push(id);
        set<int> visited;
        visited.insert(id);
        while (!q.empty())
        {
            int top = q.front();
            q.pop();
            int imp =  graph[top].first;
            vector<int> sub = graph[top].second;
            count+=imp;
            for (int i=0;i<sub.size();i++)
            {
                q.push(sub[i]);
            }
        }
        return count;
    }
};
