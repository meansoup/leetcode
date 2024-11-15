class Solution {
    public boolean isPalindrome(String s) {
        int head = 0;
        int tail = s.length() - 1;

        while (head < tail) {
            if (!Character.isLetterOrDigit(s.charAt(head))) {
                head += 1;
                continue;
            }
            if (!Character.isLetterOrDigit(s.charAt(tail))) {
                tail -= 1;
                continue;
            }

            char headChar = Character.toLowerCase(s.charAt(head));
            char tailChar = Character.toLowerCase(s.charAt(tail));

            if (headChar != tailChar) {
                return false;
            }
            head += 1;
            tail -= 1;
        }

        return true;
    }
}