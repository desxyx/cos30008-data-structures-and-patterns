def read_data(filename):
    f = open(filename, "r")

    size_line = f.readline()
    size = int(size_line)

    data = []

    for i in range(size):
        line = f.readline()
        parts = line.split()

        key = int(parts[0])
        value = int(parts[1])

        data.append([key, value])

    f.close()
    return data



def insertionSort(data):
    for i in range(1,len(data)):
        temp = data[i]
        j = i -1
        
        while j >= 0 and data[j][0] > temp[0]:
            data[j + 1] = data[j]
            j -= 1
        data[j+1] = temp
        

def print_values(data):
    for item in data:
        value = item[1]
        ch = chr(value)
        print(ch, end="")

    print()

def main():
    filename = "Data.txt"
    
    data = read_data(filename)
    print(f"Number of entries: {len(data)}")
    
    insertionSort(data)
    print_values(data)
    
if __name__ == "__main__":
    main()