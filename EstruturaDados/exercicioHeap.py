import heapq

nums = [10, 4, 7, 2, 15, 1]

# 1. Transformar em heap
heapq.heapify(nums)
print("Heap inicial:", nums)

# 2. Inserir 3
heapq.heappush(nums, 3)
print("Heap depois de inserir 3:", nums)

# 3. Remover o menor
menor = heapq.heappop(nums)
print("Menor removido:", menor)
print("Heap final:", nums)
