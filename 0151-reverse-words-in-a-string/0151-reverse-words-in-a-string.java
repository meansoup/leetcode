class Solution {
    public String reverseWords(String s) {
        List<String> words = new ArrayList<>();
        
        String word = "";
        for (char c : s.toCharArray()) {
            if (c != ' ') {
                word += c;
            } else {
                if (!word.isEmpty()) {
                    words.add(word);
                    word = "";
                }
            }
        }

        if (!word.isEmpty()) {
            words.add(word);
            word = "";
        }

        String result = "";
        for (int i = words.size() - 1; i >= 0; i--) {
            System.out.println(i + " " + words.get(i));
            result += words.get(i) + " ";
        }
        
        return result.substring(0, result.length() - 1);
    }
}