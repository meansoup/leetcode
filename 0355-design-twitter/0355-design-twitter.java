class Twitter {
    List<int[]> twits;
    Map<Integer, Set<Integer>> follows;
    
    public Twitter() {
        twits = new ArrayList<>();
        follows = new HashMap<>();
    }
    
    public void postTweet(int userId, int tweetId) {
        twits.add(new int[]{userId, tweetId});
    }
    
    public List<Integer> getNewsFeed(int userId) {
        Set<Integer> followees = follows.get(userId);
        

        List<Integer> result = new ArrayList<>();
        
        for(int i = twits.size() -1; i >= 0; i--) {
            int[] twit = twits.get(i);
            if (userId == twit[0] ||
                (followees != null && followees.contains(twit[0]))
               ) {
                result.add(twit[1]);
            }
            if (result.size() >= 10) {
                break;
            }
        }
        
        return result;
    }
    
    public void follow(int followerId, int followeeId) {
        Set<Integer> followees = follows.getOrDefault(followerId, new HashSet<Integer>());
        followees.add(followeeId);
        follows.put(followerId, followees);
    }
    
    public void unfollow(int followerId, int followeeId) {
        Set<Integer> followees = follows.getOrDefault(followerId, new HashSet<Integer>());
        followees.remove(followeeId);
        follows.put(followerId, followees);
    }
}

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter obj = new Twitter();
 * obj.postTweet(userId,tweetId);
 * List<Integer> param_2 = obj.getNewsFeed(userId);
 * obj.follow(followerId,followeeId);
 * obj.unfollow(followerId,followeeId);
 */