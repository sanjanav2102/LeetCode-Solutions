class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        candidates.sort()

        def dfs(start, path, remaining):
            if remaining == 0:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):
                num = candidates[i]

                # 🔥 IMPORTANT PRUNING
                if num > remaining:
                    break

                path.append(num)
                dfs(i, path, remaining - num)
                path.pop()

        dfs(0, [], target)
        return result