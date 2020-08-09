def set_dpi_awareness():
    try:
        from ctypes import windll
        windll.schore.SetProcessDpiAwareness(1)
    except:
        pass