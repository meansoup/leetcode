class Solution {
    public int isPrefixOfWord(String sentence, String searchWord) {
        int i = 1;
        String word = "";
        
        for (char c : sentence.toCharArray()) {
            if (c == ' ') {
                word = "";
                i++;
                continue;
            }
            word += c;
            
            if (word.startsWith(searchWord)) {
                return i;
            }
        }
        if (word.startsWith(searchWord)) {
            return i;
        }
        
        return -1;
    }
}