class Solution:
    def maxChunksToSorted(self, arr):
        n = len(arr)
        # Deque to store the maximum elements of each chunk
        stack = deque()

        for i in range(n):
            # Case 1: Current element is larger, starts a new chunk
            if not stack or arr[i] > stack[-1]:
                stack.append(arr[i])
            else:
                # Case 2: Merge chunks
                max_element = stack[-1]
                while stack and arr[i] < stack[-1]:
                    stack.pop()
                stack.append(max_element)

        return len(stack)
