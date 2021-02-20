class Solution {
    public int longestPalindrome(String s) {
        int[] count = new int[58];
        for (char c: s.toCharArray()) {
            count[c-65]++;
        }
        int result = 0;
        boolean unique = false;
        for (int v: count) {
            if (v % 2 == 0) {
                result += v;
            } else {
                result += v - 1;
                unique = true;
            }
        }
        return unique ? result + 1 : result;
    }
}