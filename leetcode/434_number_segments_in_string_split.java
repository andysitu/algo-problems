class Solution {
    public int countSegments(String s) {
        String new_s = s.trim();
        if (new_s.equals("")) {
            return 0;
        }
        return new_s.split("\\s+").length;
    }
}