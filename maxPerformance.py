class Solution:
    def maxPerformance(self, n, speed, efficiency, k):
        MOD = 10**9 + 7

        # Step 1: Make pairs of (efficiency, speed)
        engineers = []
        for i in range(n):
            engineers.append((efficiency[i], speed[i]))

        # Step 2: Sort engineers by efficiency (high → low)
        engineers.sort(reverse=True)

        # Step 3: We will keep selected speeds in a list
        import heapq
        speed_list = []   # this will work like a min-heap
        speed_sum = 0
        max_perf = 0

        # Step 4: Check each engineer one by one
        for e, s in engineers:
            # Add this engineer's speed
            heapq.heappush(speed_list, s)
            speed_sum += s

            # If we have more than k engineers, remove the smallest speed
            if len(speed_list) > k:
                smallest_speed = heapq.heappop(speed_list)
                speed_sum -= smallest_speed

            # Current performance = total speed × current efficiency
            performance = speed_sum * e

            # Update best performance
            if performance > max_perf:
                max_perf = performance

        # Step 5: Return answer under modulo
        return max_perf % MOD
