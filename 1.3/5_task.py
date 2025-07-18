def SynchronizingTables(N, ids, salary):
     copy_ids = ids
     index_ids = []
     for i in range(N):
          index_ids.append((copy_ids[i], i))

     sorted_index_ids = sorted(index_ids)
     sorted_salary = sorted(salary)
     result = []
     for _ in range(N):
          result.append(0)
     for i in range(N):
          start_index = sorted_index_ids[i][1]
          result[start_index] = sorted_salary[i] 
     return result 