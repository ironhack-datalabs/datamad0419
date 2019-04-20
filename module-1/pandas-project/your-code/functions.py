def duplicates(id_column):
    new_id_column = []
    while len(id_column) != len(set(id_column)):
        for id in id_column:
            if id not in new_id_column:
                new_id_column.append(id)
            else:
                id = str(id) + "a"
    return new_id_column


print(duplicates([1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]))