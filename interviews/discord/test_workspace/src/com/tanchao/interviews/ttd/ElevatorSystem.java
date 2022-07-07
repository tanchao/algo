package com.tanchao.ttd;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.SortedMap;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.Value;

/**
 * Hotels
 * 
 * Floor: Up & Down
 * Inside: Floor Number
 * 
 * direction as expected (up/down)
 * 
 * Multiple Elevator Cabins & Floors at hotel - one control buttons each floor
 * 
 * 
 * Entity:
 *      - ElevatorCabin (inside buttons)
 *      - Floor (outside buttons)
 *      - Direction - Enum
 *           - Status 
 *      - User (act)
 * 
 * Behavior: 
 *      - pressButton (inside/outside)
 * 
 * Algo:
 *      - request (target, source)
 *      - consider direction 
 * 
 */

public class ElevatorSystem {
    List<Floor> floors = new ArrayList<>();
    List<Cabin> cabins = new ArrayList<>();
    Hotel hotel = new Hotel(floors, cabins);

    public void processRequest(Request req) {
        Cabin cabin = null;
        while (cabin == null) {
            cabin = getCabin(req);
        }
        cabin.move(req.targetFloor);
    }
    
    private Cabin getCabin(Request req) {
        // Map<Cabin, Integer> cabinGaps = new HashMap<>();
        // for (Cabin cabin : cabins) {
        //     cabinGaps.put(cabin, req.targetFloor.level - cabin.status.floor.level);
        // }
        // pull candidate from UP status first
        for (Cabin cabin : cabins) {
            if (cabin.direction == req.direction) {
                if (req.targetFloor.level - cabin.status.floor.level > 0)
                    return cabin;
            }
            if (cabin.direction == Direction.IDLE) {
                return cabin;
            }
        }
        return null;
    }

    public static void main(String[] args) {
        User user1 = new User();
        
    }
}

@AllArgsConstructor
class Hotel {
    public Hotel(List<Floor> floors2, List<Cabin> cabins) {
    }
    List<Floor> floors;
    List<Cabin> elevators;
}

class Floor {
    int level;
    FloorButton upButton = new FloorButton(this, Direction.UP);
    FloorButton downButton = new FloorButton(this, Direction.DOWN);
}

class Cabin {
    int id;
    List<CabinButton> buttonControl;
    Direction direction;
    Status status;
    List<Floor> nextTargets;

    public void move(Floor targetFloor) {
        if (nextTargets.size() == 0) {
            nextTargets.add(targetFloor);
            move();
        } else {
            for (Floor next : nextTargets) {
                if (this.direction == Direction.UP && targetFloor.level < next.level) {
                    nextTargets.add(nextTargets.indexOf(next), targetFloor);
                    return;
                }
                if (this.direction == Direction.DOWN && targetFloor.level > next.level) {
                    nextTargets.add(nextTargets.indexOf(next), targetFloor);
                    return;
                }
            }
            nextTargets.add(targetFloor); 
        }
    }

    private void move() {
        while (nextTargets.size() > 0) {
            Floor nextFloor = nextTargets.get(0);
            this.status.direction = this.direction;
            this.status.floor = nextFloor;
        }
        this.direction = Direction.IDLE;
    }
}

interface Button {

    // abstract
    Request press();
}

// inside of elevator
class CabinButton implements Button {
    Cabin carbin; // which elevator cabin the button is in
    Floor targetFloor; // one cabin have all floor buttons

    @Override
    public Request press() {
        Direction direction = this.carbin.status.floor.level - targetFloor.level > 0 ? Direction.DOWN : Direction.UP; 
        Request req = new Request(targetFloor, this.carbin.status.floor, carbin, direction);
        return req;
    }
}

// outside of elevator
class FloorButton implements Button {
    Floor floor;
    Direction direction; // up or down only
    
    public FloorButton(Floor floor2, Direction up) {
    }

    @Override
    public Request press() {
        Request req = new Request(floor, null, null, direction);
        return req;
    }
}

enum Direction {
    UP,
    DOWN,
    IDLE
}

class Status {
    Direction direction;
    Floor floor;
}

class User {
    int userId;
}

class Request {
    public Request(Floor targetFloor, Floor fromFloor, Cabin carbin, Direction direction) {
    }
    Floor targetFloor;
    Floor fromFloor;
    Direction direction;
    Cabin cabin;
}


// floor 1 -> 5 press FButton