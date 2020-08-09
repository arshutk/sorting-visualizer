
def selection_sort(data, draw_dataset, wait_time, sort_canvas):
    for i in range(0, len(data) - 1):
        min_value_index = i
        for j in range(i+1, len(data)):
            if data[j] < data[min_value_index]:
                min_value_index = j
                draw_dataset(data, ["#0099FF" if counter == min_value_index or counter ==
                                    i else "#98fb98" for counter in range(len(data))])
                sort_canvas.after(int(wait_time*1000), sort_canvas.update())

        if min_value_index != i:
            data[min_value_index], data[i] = data[i], data[min_value_index]
            draw_dataset(data, ["#0099FF" if counter == min_value_index or counter ==
                                i else "#98fb98" for counter in range(len(data))])
            sort_canvas.after(int(wait_time*1000), sort_canvas.update())
