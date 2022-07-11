import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;

public class WordSearch {
    private static final int[][] URDL = {{-1,0}, {0,1}, {1, 0}, {0, -1}};
    //private static Set<Spot> visited = new HashSet<>(); 

    public static boolean exist(char[][] board, String word) {
        // locate start char on board
        char[] chars = word.toCharArray();
        char start = chars[0];
        List<Spot> startSpots = new LinkedList<>();
        int rowMax = board.length, colMax = board[0].length;
        for (int i=0; i<rowMax; i++) {
            for (int j=0; j<colMax; j++) {
                if (board[i][j] == start) {
                    startSpots.add(new Spot(i, j));
                }
            }
        }
        //   each of them do:
        //     search 4 directions for next char, mark itself as visited
        for (Spot startSpot: startSpots) {
            Set<Spot> visited = new HashSet<>(); 
            visited.add(startSpot);
            int next = 1; 
            Spot curSpot = startSpot;
            while (next < chars.length) {
                Spot nextSpot = findNextCharSpot(board, curSpot, chars[next], rowMax, colMax, visited);
                if (nextSpot == null) break;
                curSpot = nextSpot;
                next ++;
            }

            if (next == chars.length - 1) return true;
        }

        return false;
    }

    private static Spot findNextCharSpot(char[][] board, Spot cur, char nextChar, int rowMax, int colMax, Set<Spot> visited) {
        int nextRow = cur.row, nextCol = cur.col;
        for (int[] d: URDL) {
            nextRow += d[0];
            nextCol += d[1];
            if (nextRow >= 0 && nextRow < rowMax && nextCol >=0 && nextCol < colMax) {
                Spot nextSpot = new Spot(nextRow, nextCol);
                if (visited.contains(nextSpot)) continue;
                visited.add(nextSpot);
                if (board[nextRow][nextCol] == nextChar) {
                    return nextSpot;
                }
            }
        }
        return null;
    }

    public static void main(String[] args) {
        System.out.println("start");
        char[][] board = {
            {'A','B','C','E'},
            {'S','F','C','S'},
            {'A','D','E','E'}
        };
        System.out.println(exist(board, "ABCCED"));
    }
}

class Spot {
    public int row;
    public int col;
    public Spot(int row, int col) {
        this.row = row;
        this.col = col;
    }
    public Spot() {}
}
