class Solution {
    public int findChampion(int n, int[][] edges) {
        Set<Integer> ins = new HashSet<>();
        Set<Integer> outs = new HashSet<>();

        for (int i = 0; i < n; i++) {
            ins.add(i);
        }
        
        for (int[] edge: edges) {
            outs.add(edge[1]);
        }
        
        ins.removeAll(outs);
        
        if (ins.size() == 1) {
            return ins.stream().findFirst().orElse(-1);
        }
        return -1;
    }
}