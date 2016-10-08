public class Solution {
    public String toHex(int num) {
        if (num == 0) return "0";
        
        String res = "";
        
        while (num != 0) {
            int n = num & 0xf;
            
            if (n < 10) {
                res = (char)('0' + n - 0) + res;
            } else {
                res = (char)('a' + n - 10) + res;
            }
            
            num = (num >>> 4);
        }
        
        return res;
    }
}
