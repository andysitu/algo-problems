// Thought python might run differently with bin numbers
// it's never ending loop because it can exceed max
class Solution {
    public int getSum(int a, int b) {
        int carry;
        while (b != 0) {
            carry = a & b;
            a = a ^ b;
            b = (carry) << 1;
        }
        return a;
    }
}