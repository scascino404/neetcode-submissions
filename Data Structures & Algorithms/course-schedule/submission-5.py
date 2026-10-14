class Solution:
    def canFinish(self, num_courses: int, prereqs: List[List[int]]) -> bool:
        adj = [[] for _ in range(num_courses)]
        for a, b in prereqs:
            adj[a].append(b)
        
        results = {}
        def can_complete(course, seen=set()):
            if course in seen:
                results[course] = False

            if course in results:
                return results[course]

            results[course] = True

            for prereq in adj[course]:
                if not can_complete(prereq, seen.union([course])):
                    results[course] = False
                    break

            return results[course]

        for course in range(num_courses):
            can_complete(course)

        return all(results.values())