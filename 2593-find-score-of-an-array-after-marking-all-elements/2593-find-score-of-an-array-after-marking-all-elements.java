class Solution {
    public long findScore(int[] nums) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> 
            a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]
        );
        Set<Integer> indexs = new HashSet<>();
        
        for (int i = 0; i < nums.length; i++) {
            pq.add(new int[] {nums[i], i});
            indexs.add(i);
        }
        
        long result = 0;
        while(!indexs.isEmpty()) {
            int[] target = pq.poll();
            
            int targetIdx = target[1];
            if (!indexs.contains(targetIdx)) {
                continue;
            }
        
            result += target[0];
            
            indexs.remove(targetIdx);
            indexs.remove(targetIdx - 1);
            indexs.remove(targetIdx + 1);
        }
        
        return result;
    }
}