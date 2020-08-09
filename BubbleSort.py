
def bubble_sort(data, draw_dataset, wait_time, sort_canvas):
    for counter in range(len(data) - 1):
        for index in range(len(data) - 1):
            if data[index] > data[index + 1]:
                data[index], data[index + 1] = data[index + 1], data[index]
                draw_dataset(data, ["#0099FF" if x == index or x == (
                    index + 1) else "#98fb98" for x in range(len(data))])
                sort_canvas.after(int(wait_time*1000), sort_canvas.update())
