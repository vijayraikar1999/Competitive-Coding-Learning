class Solution {
public:
    bool isPalindrome(int x) {
      string str_number = to_string(x);
      int i = 0; 
      int j = str_number.size() - 1;
      while (i < j) {
        if (str_number[i] != str_number[j]) {
          return false;
        }
        i++;
        j--;
      }
      return true;
        
    }
};