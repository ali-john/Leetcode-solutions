class Solution {
public:
    bool isValid(string s) {
        stack<char> stack;

        for (auto ch: s){
            if (ch == ')'){
                if (stack.size() < 1 || stack.top() != '('){
                    return false;
                }
                else{
                    stack.pop();
                }
            }

            else if (ch == '}'){
                if (stack.size() < 1 || stack.top() != '{'){
                    return false;
                }
                else{
                    stack.pop();
                }
            }

            else if (ch == ']'){
                if (stack.size() < 1 || stack.top() != '['){
                    return false;
                }
                else{
                    stack.pop();
                }
            }
            else
                stack.push(ch);
        }

        if (stack.size() == 0)
            return true;
        else
            return false;
        
    }
};
