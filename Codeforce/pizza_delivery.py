test_cases = int(input())

for _ in range(test_cases):
    n, Ax, Ay, Bx, By = map(int,input().split())
    x_coordinates = list(map(int,input().split()))
    y_coordinates = list(map(int,input().split()))
    x_coordinates.append(Bx)
    y_coordinates.append(By)
    time = 0
    while len(x_coordinates)>0:
        min_ = 0
        for i in range(1,len(x_coordinates)):
            if x_coordinates[min_]>x_coordinates[i]:
                min_ = i
            elif x_coordinates[min_] == x_coordinates[i]:
                if y_coordinates[min_] > y_coordinates[i]:
                    min_ = i
        time += (x_coordinates[min_]-Ax)
        time += (abs(Ay-y_coordinates[min_]))
        Ax = x_coordinates[min_]
        Ay = y_coordinates[min_]
        x_coordinates.remove(Ax)
        y_coordinates.remove(Ay)

        
    print(time)
    