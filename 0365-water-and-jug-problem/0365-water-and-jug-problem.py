from collections import deque
class Solution(object):
  
    def water_jug_bfs(self, capacityA, capacityB, target):
        # Step 1: Start from (0,0)
        start = (0, 0)

        # Step 2: Create an empty queue
        queue = deque()

        # Step 3: Insert (0,0) into the queue
        queue.append(start)

        # Step 4: Mark (0,0) as visited
        visited = set()
        visited.add(start)

        # Store parent to reconstruct the path
        parent = {start: None}

        # Step 5: BFS
        while queue:
            # a. Remove the front state
            x, y = queue.popleft()

            #print(f"Current State: ({x}, {y})")

            # b. Check if goal is reached
            if x+y == target:
                #print("\nGoal Reached!")
                return True

                # Reconstruct path
                # path = []
                # state = (x, y)
                # while state is not None:
                #     path.append(state)
                #     state = parent[state]

                # path.reverse()

                # print("\nPath:")
                # for s in path:
                #     print(s)

                return True

            # c. Generate all six possible next states

            next_states = []

            # 1. Fill Jug A
            next_states.append((capacityA, y))

            # 2. Fill Jug B
            next_states.append((x, capacityB))

            # 3. Empty Jug A
            next_states.append((0, y))

            # 4. Empty Jug B
            next_states.append((x, 0))

            # 5. Pour A -> B
            transfer = min(x, capacityB - y)
            next_states.append((x - transfer, y + transfer))

            # 6. Pour B -> A
            transfer = min(y, capacityA - x)
            next_states.append((x + transfer, y - transfer))

            # d. Visit new states
            for state in next_states:
                if state not in visited:
                    visited.add(state)
                    parent[state] = (x, y)
                    queue.append(state)

        # Step 6: No solution
    # print("No solution exists.")
        return False


    # Example

    def canMeasureWater(self, x, y, target):
        ans = self.water_jug_bfs(x, y, target)
        return ans


  