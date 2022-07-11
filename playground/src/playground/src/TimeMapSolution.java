import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;

public class TimeMapSolution {
    public static void main(String[] args) {
        TimeMap timeMap = new TimeMap();
        timeMap.set("love", "high", 10);
        timeMap.set("love", "low", 20);
        timeMap.set("love", "low", 30);
        timeMap.set("love", "low", 20);
        System.out.println(timeMap.get("love", 5));
        System.out.println(timeMap.get("love", 10));
        //timeMap.set("foo", "bar2", 4); 
        System.out.println(timeMap.get("love", 15));
        System.out.println(timeMap.get("love", 20));
        System.out.println(timeMap.get("love", 25));
        
    }
}

class TimeMap {
    private final Map<String, Queue<TimeValue>> timeMap = new HashMap<>();

    public TimeMap() {
        
    }
    
    public void set(String key, String value, int timestamp) {
        Queue<TimeValue> queue = timeMap.get(key);
        if (queue == null) { // new
            TimeValue timeValue = new TimeValue(timestamp, value);
            queue = new PriorityQueue<TimeValue>();
            queue.add(timeValue);
            timeMap.put(key, queue);
        } else { // exists
            TimeValue timeValue = new TimeValue(timestamp, value);
            queue.add(timeValue); // already in queue?
        }
    }
    
    public String get(String key, int timestamp) {
        Queue<TimeValue> queue = timeMap.get(key);
        if (queue == null) {
            return "";
        } else {
            Iterator<TimeValue> iterator = queue.iterator();
            TimeValue value;
            while (iterator.hasNext()) {
                value = iterator.next();
                if (value.timestamp <= timestamp) { // exact match
                    return value.value;
                }
            }
            return ""; // no value
        }
    }
}

class TimeValue implements Comparable<TimeValue> {
    public int timestamp;
    public String value;

    public TimeValue(int timestamp2, String value2) {
        this.timestamp = timestamp2;
        this.value = value2;
    }

    @Override
    public int compareTo(TimeValue other) {
        if (this.timestamp > other.timestamp) {
            return -1;
        } else if (this.timestamp < other.timestamp) {
            return 1;
        }
        return 0;
    }
}

/**
 * 1. HashMap for each employee
 * 2. Ordered list of address history
 */