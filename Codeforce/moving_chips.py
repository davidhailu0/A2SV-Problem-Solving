test_cases = int(input())

for _ in range(test_cases):
    number_cells = int(input())
    cells = list(map(int,input().split()))
    total_one = cells.count(1)
    if total_one == 1 or total_one == number_cells:
        print(0)
    else:
        index_one = cells.index(1)
        cells.reverse()
        index_last_one = cells.index(1)
        cells.reverse()
        count_zero = cells[index_one:-(index_last_one+1)].count(0)
        print(count_zero)

