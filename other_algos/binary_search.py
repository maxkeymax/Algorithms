def bin_search(seq, num):
    start_index = 0
    end_index = len(seq) - 1
    counter = 0
    
    while start_index <= end_index:
        counter += 1
        cur_index = (start_index + end_index) // 2
        
        if seq[cur_index] == num:
            return f'Индекс элемента {num}: {cur_index}, итераций поиска: {counter}'
        if seq[cur_index] > num:
            end_index = cur_index - 1
        else:
            start_index = cur_index + 1
    
    return -1
            
print(bin_search([1, 5, 7, 8, 12, 45, 67, 102, 303, 405], 1))