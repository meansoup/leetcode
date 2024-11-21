class Solution {
    
    int dirY[] = { -1, 1, 0, 0 };
	int dirX[] = { 0, 0, -1, 1 };
    
    public int countUnguarded(int m, int n, int[][] guards, int[][] walls) {
        int[][] map = new int[m][n];
        
        for (int[] guard: guards) {
            map[guard[0]][guard[1]] = 1; 
        }
        
        for (int[] wall: walls) {
            map[wall[0]][wall[1]] = 3;
        }
        
        for (int[] guard: guards) {
            checkGuarded(map, guard[1] + dirX[0], guard[0] + dirY[0], 0);
            checkGuarded(map, guard[1] + dirX[1], guard[0] + dirY[1], 1);
            checkGuarded(map, guard[1] + dirX[2], guard[0] + dirY[2], 2);
            checkGuarded(map, guard[1] + dirX[3], guard[0] + dirY[3], 3);
        }
        
        int result = 0;
        for (int y = 0; y < m; y++) {
            for (int x = 0; x < n; x++) {
                if (map[y][x] == 0) {
                    result += 1;
                }
            }
        }
        
        return result;
    }
    
    private void checkGuarded(int[][] map, int x, int y, int direction) {
        if (y < 0 || y >= map.length || x < 0 || x >= map[0].length) {
            return;
        }
        
        if ((map[y][x] & 1) == 1) {
            return;
        }
        
        map[y][x] = 2;
        
        checkGuarded(map, x + dirX[direction], y + dirY[direction], direction);
    }
}