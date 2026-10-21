def remove_negatives(matrix):
    return list(map(
        lambda row: list(filter(lambda x: x >= 0, row)),
        matrix
    ))


def sort_matrix(matrix):
    return list(map(lambda row: sorted(row), matrix))


def sort_rows_by_sum(matrix):
    return sorted(matrix, key=lambda row: sum(row))


def convert_to_tuples(matrix):
    return tuple(map(tuple, matrix))


def display(matrix, title):
    print(title)
    for row in matrix:
        print(row)


def main():
    matrix = [
        [4, -2, 7],
        [1, -5, 3],
        [9, 6, -1]
    ]

    display(matrix, "Original Matrix:")

    filtered = remove_negatives(matrix)
    display(filtered, "\nAfter Removing Negative Elements:")

    sorted_matrix = sort_matrix(filtered)
    display(sorted_matrix, "\nAfter Sorting Each Row:")

    sorted_rows = sort_rows_by_sum(sorted_matrix)
    display(sorted_rows, "\nRows Sorted by Sum:")

    result = convert_to_tuples(sorted_rows)
    print("\nFinal Tuple Matrix:", result)

def remove_negatives(matrix):
    return list(map(
        lambda row: list(filter(lambda x: x >= 0, row)),
        matrix
    ))


def sort_matrix(matrix):
    return list(map(lambda row: sorted(row), matrix))


def sort_rows_by_sum(matrix):
    return sorted(matrix, key=lambda row: sum(row))


def convert_to_tuples(matrix):
    return tuple(map(tuple, matrix))


def display(matrix, title):
    print(title)
    for row in matrix:
        print(row)


def main():
    matrix = [
        [4, -2, 7],
        [1, -5, 3],
        [9, 6, -1]
    ]

    display(matrix, "Original Matrix:")

    filtered = remove_negatives(matrix)
    display(filtered, "\nAfter Removing Negative Elements:")

    sorted_matrix = sort_matrix(filtered)
    display(sorted_matrix, "\nAfter Sorting Each Row:")

    sorted_rows = sort_rows_by_sum(sorted_matrix)
    display(sorted_rows, "\nRows Sorted by Sum:")

    result = convert_to_tuples(sorted_rows)
    print("\nFinal Tuple Matrix:", result)


if __name__ == "__main__":
    main()
