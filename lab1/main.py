l_array = [23, 4, 67, 1, 0, -20, 29, -100, 32, 99, -56]

print ("[", end= "");

for i in range(len(l_array)):
    print (l_array[i], end="");
    
    if i + 1 < len(l_array):
        print (",", end = "");
        
print("]")