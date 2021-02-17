class Solution {
    public String licenseKeyFormatting(String S, int K) {
        String totalS = S.replace("-" ,"").toUpperCase();
        String newS = "";
        int curK = 0;
        for (int i=totalS.length()-1; i >= 0; i--) {
            if (curK == K) {
                newS = "-" + newS;
                curK = 0;
            }
            newS = totalS.charAt(i) + newS;
            curK++;
        }
        return newS;
    }
}