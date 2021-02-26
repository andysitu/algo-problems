class Solution {
    public String addStrings(String num1, String num2) {
        int len1 = num1.length(),
            len2 = num2.length();
        int maxLength = Math.max(len1, len2);
        StringBuilder sb = new StringBuilder(maxLength + 1);

        int carry = 0,
            s,
            i1 = maxLength - len1,
            i2 = maxLength - len2;
        for (int i = maxLength - 1; i >= 0; i--) {
            s = carry;
            if (i -i1 >= 0) {
                s += num1.charAt(i - i1) - '0';
            }
            if (i - i2 >= 0) {
                s += num2.charAt(i - i2) - '0';
            }
            carry = s / 10;
            s = s % 10;
            sb.append(s);
        }
        if (carry > 0) {
            sb.append(carry);
        }
        return sb.reverse().toString();
    }
}