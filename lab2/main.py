
# def read_data(filename):
#     contents = []
#     try:

#         with open(filename, 'r') as f:
#             entries = int(f.readline().strip())
#             print(f"number of entries: {entries}")

#             lines = [line.strip() for line in f.readlines()]
#             pairs = [(line.split(' ')) for line in lines]
#             contents = [{"key": int(pair[0]), "value": int(pair[1])} for pair in pairs]

#     except FileNotFoundError:
#         print(f"Erro: The file '{filename}' was not found.")

#     except Exception as e:
#         print(f"An error has occured: {e}")
#     return contents


# def insertion_sort_key_value_pairs(pairs):
    
#     for i in range(1,len(pairs)):
#         elem = pairs[i]
#         j = i - 1
#         while j >=0 and elem["key"] < pairs[j]["key"]:
#             pairs[j + 1 ] = pairs[j]
#             j -= 1
#         pairs[ j + 1 ] = elem


# def print_values(pairs):
#     for i in range(len(pairs)):
#         print(chr(pairs[i]["value"]), end='')


# if __name__ == "__main__":

#     data = read_data("data.txt")

#     insertion_sort_key_value_pairs(data)

#     print_values(data)


def read_data(filename):
    try:
        with open(filename, 'r') as f:
            entries = int(f.readline().strip())
            print(f"number of entries: {entries}")
            return [
                {"key": int(k), "value": int(v)}
                for k, v in (line.strip().split() for line in f)
            ]
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []
    except Exception as e:
        print(f"An error has occurred: {e}")
        return []


def insertion_sort_key_value_pairs(pairs):
    for i, elem in enumerate(pairs):
        j = i - 1
        while j >= 0 and elem["key"] < pairs[j]["key"]:
            pairs[j + 1] = pairs[j]
            j -= 1
        pairs[j + 1] = elem


def print_values(pairs):
    print(''.join(chr(pair["value"]) for pair in pairs))


if __name__ == "__main__":
    data = read_data("data.txt")
    insertion_sort_key_value_pairs(data)
    print_values(data)
