class Solution {
    public String licenseKeyFormatting(String S, int K) {
        StringBuilder newS = new StringBuilder();
        int count = 0;
        for (int i=S.length()-1; i >= 0; i--) {
            if (S.charAt(i) == '-') {
                continue;
            }
            count++;
            if (count > K) {
                newS.append("-");
                count = 1;
            }
            newS.append(S.charAt(i));
        }
        return newS.reverse().toString().toUpperCase();
    }
}