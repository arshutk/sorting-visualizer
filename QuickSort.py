
def quick_sort(data, start, end, draw_dataset, wait_time, sort_canvas):
    if start < end:
        partition_index = quick_sort_partitioner(
            data, start, end, draw_dataset, wait_time, sort_canvas)
    # left :
        quick_sort(data, start, partition_index - 1,
                   draw_dataset, wait_time, sort_canvas)
    # Right :
        quick_sort(data, partition_index + 1, end,
                   draw_dataset, wait_time, sort_canvas)


def quick_sort_partitioner(data, start, end, draw_dataset, wait_time, sort_canvas):
    border = start
    pivot = data[end]

    draw_dataset(data, get_clrd_data(len(data), start, end, border, border))
    sort_canvas.after(int(wait_time*1000), sort_canvas.update())

    for index in range(start, end):
        if data[index] < pivot:
            draw_dataset(data, get_clrd_data(
                len(data), start, end, border, index, True))
            sort_canvas.after(int(wait_time*1000), sort_canvas.update())

            data[border], data[index] = data[index], data[border]
            border += 1

        draw_dataset(data, get_clrd_data(len(data), start, end, border, index))
        sort_canvas.after(int(wait_time*1000), sort_canvas.update())

    # swapping pivot with border value :
    draw_dataset(data, get_clrd_data(len(data), start, end, border, end, True))
    sort_canvas.after(int(wait_time*1000), sort_canvas.update())

    data[border], data[end] = data[end], data[border]
    return border


def get_clrd_data(data_len, start, end, border, crnt_index, is_swaping=False):
    clrd_data = []
    for counter in range(data_len):
        # base colouring
        if counter >= start and counter <= end:
            clrd_data.append("#808080")
        else:
            clrd_data.append("#E0E0E0")

        if counter == end:
            clrd_data[counter] = "#3366FF"
        elif counter == border:
            clrd_data[counter] = "#FF0033"
        elif counter == crnt_index:
            clrd_data[counter] = "#FFCC33"

        if is_swaping:
            if counter == border or counter == crnt_index:
                clrd_data[counter] == "green"

    return clrd_data
