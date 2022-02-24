package playground.src;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Map.Entry;

public class Bonus {
    public static Map<String, Integer> allocate(int bonus, Map<String, Integer> cap) {
        Queue<Employee> expectedBonus = new PriorityQueue<>();
        Queue<Employee> actualBonus = new PriorityQueue<>();
        for (Entry<String, Integer> entry : cap.entrySet()) {
            expectedBonus.add(new Employee(entry.getKey(), entry.getValue()));
        } // ordered by cap then alphabetical
        int previousCap = 0;
        while (!expectedBonus.isEmpty()) {
            int currentSize = expectedBonus.size();
            int currentCap = expectedBonus.peek().cap;
            int currentTotalCap = currentCap * currentSize;
            if (currentTotalCap < bonus) { // partial bonus allocated 
                while (!expectedBonus.isEmpty() && expectedBonus.peek().cap == currentCap) {
                    actualBonus.add(expectedBonus.poll());
                }
                bonus = bonus - currentTotalCap;
                previousCap = currentCap;
            } else { // all bonus allocated this round
                int currentAllocation = Math.floorDiv(bonus, currentSize) + previousCap;
                int extra = bonus % currentSize;
                while (!expectedBonus.isEmpty()) {
                    Employee employee = expectedBonus.poll();
                    if (employee.cap > currentAllocation) {
                        employee.cap = currentAllocation;
                        if (extra > 0) {
                            extra--;
                            employee.cap += 1;
                        }
                    }
                    actualBonus.add(employee);
                }
            }
        }
        Map<String, Integer> result = new HashMap<>();
        Iterator<Employee> iterator = actualBonus.iterator();
        while (iterator.hasNext()) {
            Employee employee = iterator.next();
            result.put(employee.name, employee.cap);
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println("start");

        int bonus = 1003;
        Map<String, Integer> expected = new HashMap<>();
        expected.put("A", 100);
        expected.put("B", 100);
        expected.put("C", 200);
        expected.put("D", 200);
        expected.put("CA", 300);
        expected.put("BC", 300);

        Map<String, Integer> actual = allocate(bonus, expected);
        System.out.println(actual);

        System.out.println("end");
    }
}

class Employee implements Comparable<Employee> {
    public String name;
    public int cap;

    public Employee(String name, int cap) {
        this.name = name;
        this.cap = cap;
    }

    @Override
    public int compareTo(Employee other) {
        if (this.cap == other.cap) {
            return this.name.compareTo(other.name);
        }
        return this.cap - other.cap;
    }
}

/**
 * 1. Ordered list of Employee 
 * 2. Allocate bonus from start to end
 * 2.1 leveling
 */