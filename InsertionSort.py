
def insertion_sort(data, draw_dataset, wait_time, sort_canvas):
    for i in range(1, len(data)):
        border = i
        draw_dataset(
            data, ["#FF0033" if x < i else "#98fb98" for x in range(len(data))])
        sort_canvas.after(int(wait_time*1000), sort_canvas.update())

        while data[i-1] > data[i] and i > 0:
            draw_dataset(data, get_clrd_data(len(data), border, i))
            sort_canvas.after(int(wait_time*1000), sort_canvas.update())
            data[i], data[i - 1] = data[i - 1], data[i]
            draw_dataset(data, get_clrd_data(len(data), border, i))
            sort_canvas.after(int(wait_time*1000), sort_canvas.update())
            i -= 1


def get_clrd_data(len_data, border_sorted_data, crnt_val):
    clrd_data = []
    for index in range(0, len_data):
        if index <= border_sorted_data:
            if index == crnt_val or index == crnt_val - 1:
                clrd_data.append("#0099FF")
            else:
                clrd_data.append("#FF0033")
        else:
            clrd_data.append("#98fb98")
    return clrd_data
