import heapq

def min_connection_cost(cables):
    heapq.heapify(cables)  # Перетворюємо список у мінімальну купу
    total_cost = 0
    
    while len(cables) > 1:
        first = heapq.heappop(cables)  # Витягуємо найменший кабель
        second = heapq.heappop(cables)  # Витягуємо другий найменший кабель
        cost = first + second
        total_cost += cost
        heapq.heappush(cables, cost)  # Додаємо новий кабель назад у купу
    
    return total_cost

# Приклад використання
cables = [8, 4, 6, 12]
print("Мінімальні витрати на з'єднання:", min_connection_cost(cables))


def merge_k_lists(lists):
    min_heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst[0], i, 0))  # Додаємо перший елемент кожного списку
    
    merged_list = []
    while min_heap:
        value, list_idx, element_idx = heapq.heappop(min_heap)
        merged_list.append(value)
        
        if element_idx + 1 < len(lists[list_idx]):
            next_value = lists[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_value, list_idx, element_idx + 1))
    
    return merged_list

# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
print("Відсортований список:", merge_k_lists(lists))