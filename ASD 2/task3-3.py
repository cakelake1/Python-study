Тесты 5.4:
print("удаление элемента, когда в результате размер буфера остаётся прежним (проверьте также размер буфера)")
arr = DynArray()
arr.append(1)
arr.append(2)
arr.append(3)
test = [arr[i] for i in range(len(arr))]
print(f"До удаления: {[arr[i] for i in range(len(arr))]}")
print(f"count={len(arr)}, capacity={arr.capacity}\n")
print("удаляем элемент с индексом 1, проверяем буфер и счётчик")
arr.delete(1)
print(f"После удаления элемента с индексом 1: {[arr[i] for i in range(len(arr))]}")
print(f"count={len(arr)}, capacity={arr.capacity}\n")

print("попытка удаления элемента в недопустимой позиции")
try:
    arr.delete(5)  
except IndexError as e:
    print(f"Ошибка: {e}\n")
arr = DynArray()
for i in range(17):
    arr.append(i)
print("удаление элемента, когда в результате понижается размер буфера (проверьте также корректное изменение размера буфера")
print(f"count={len(arr)}, capacity={arr.capacity}, {[arr[i] for i in range(len(arr))]}")
for _ in range(9):
    arr.delete(0) 
print(f"count={len(arr)}, capacity={arr.capacity}, {[arr[i] for i in range(len(arr))]}\n")
print("вставка элемента, когда в итоге размер буфера не превышен (проверьте также размер буфера)") 
arr = DynArray()
for i in range(3):
    arr.append(i)
print(f"count={len(arr)}, capacity={arr.capacity}, {[arr[i] for i in range(len(arr))]}")
arr.insert(0, -1)
print("После вставки -1 в начало:"f"count={len(arr)}, capacity={arr.capacity}, {[arr[i] for i in range(len(arr))]}\n")
print("вставка элемента, когда в результате превышен размер буфера (проверьте также корректное изменение размера буфера)") 
for _ in range(17):
    arr.insert(2, 99)
print("После вставки 99 на позицию 2-17:"f"count={len(arr)}, capacity={arr.capacity}, {[arr[i] for i in range(len(arr))]}\n")
print("попытка вставки элемента в недопустимую позицию") 
try:
    arr.insert(-1, 999)
    print("Сработало =)")
except IndexError as e:
    print(f"для индекса -1 не сработало: {e}")