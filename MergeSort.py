
def merge_sort(data, draw_dataset, wait_time, sort_canvas):
    merge_sort_algorithm(data, 0, len(data) - 1,
                         draw_dataset, wait_time, sort_canvas)


def merge_sort_algorithm(data, left, right, draw_dataset, wait_time, sort_canvas):
    if left < right:
        middle = (left + right) // 2
        merge_sort_algorithm(data, left, middle,
                             draw_dataset, wait_time, sort_canvas)
        merge_sort_algorithm(data, middle + 1, right,
                             draw_dataset, wait_time, sort_canvas)
        merge(data, left, middle, right, draw_dataset, wait_time, sort_canvas)


def merge(data, left, middle, right, draw_dataset, wait_time, sort_canvas):
    draw_dataset(data, get_clrd_data(len(data), left, middle, right))
    sort_canvas.after(int(wait_time*1000), sort_canvas.update())

    left_data = data[left: middle + 1]
    right_data = data[middle + 1: right + 1]

    left_index, right_index = 0, 0

    for data_index in range(left, right + 1):
        if left_index < len(left_data) and right_index < len(right_data):
            if left_data[left_index] <= right_data[right_index]:
                data[data_index] = left_data[left_index]
                left_index += 1
            else:
                data[data_index] = right_data[right_index]
                right_index += 1

        elif left_index < len(left_data):
            data[data_index] = left_data[left_index]
            left_index += 1
        else:
            data[data_index] = right_data[right_index]
            right_index += 1

    draw_dataset(data, ["#98fb98" if counter >= left and counter <=
                        right else "#E0E0E0" for counter in range(len(data))])
    sort_canvas.after(int(wait_time*1000), sort_canvas.update())


def get_clrd_data(length, left, middle, right):
    clrd_data = []

    for index in range(length):
        if index >= left and index <= right:
            if index <= middle:
                clrd_data.append("#FFCC33")
            else:
                clrd_data.append("#3366FF")
        else:
            clrd_data.append("#E0E0E0")
    return clrd_data
