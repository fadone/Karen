import threading
import tkinter
from karen.utils.autocomplete import AutocompleteEntry
from karen.engine import *
from karen.core import karen

output_text = None
entry = None
mic_btn = None

listen_thread = None
process_thread = None


def on_click_mic():
    global listen_thread
    if listen_thread is not None and listen_thread.is_alive():
        print("Listen Thread Running...")
    else:
        listen_thread = threading.Thread(target=karen.listen_process_thread())


def on_click_entry(event):
    global process_thread
    print("Entry clicked")
    if process_thread is not None and process_thread.is_alive():
        print("Process Thread Running...")
    else:
        process_thread = threading.Thread(target=karen.process_thread())


def init():
    global output_text, entry, mic_btn
    main_window = tkinter.Tk()
    mic_img = tkinter.PhotoImage(file="images/mic.png")
    mic_image = mic_img.subsample(10, 10)
    main_window.title("Karen")
    main_window.geometry("320x480-8+60")

    main_frame = tkinter.Frame(main_window, border=1, background='green')
    main_frame.pack(fill="both", expand=True)
    bottom_frame = tkinter.Frame(main_window)
    bottom_frame.pack(side="bottom", anchor="w", fill="x")

    output_text = tkinter.Label(main_frame)
    output_text.config(font=("Calibri", 12, "bold"), wraplength="250")
    output_text.pack(fill="both", expand=True)
    # controller.set_output_text(output_text)

    input_entry = AutocompleteEntry(bottom_frame,  width="34")
    # input_entry.set_completion_list(util.commands_list)
    input_entry.config(font="Calibri, 11")
    input_entry.pack(side="left", ipady=7)
    input_entry.focus_set()

    mic_btn = tkinter.Button(bottom_frame, image=mic_image, width="50", height="30", relief="flat", command=on_click_mic)
    mic_btn.pack(side="right")

    input_entry.bind('<Return>', on_click_entry)

    # wake_word_thread = threading.Thread(target=listen_wake_word)
    # wake_word_thread.setDaemon(True)
    #
    # start_thread = threading.Thread(target=start)
    # start_thread.setDaemon(True)
    #
    #
    # def start_threads():
    #     start_thread.start()
    #     wake_word_thread.start()


    # main_window.after(1000, start_threads)
    # main_window.mainloop()
    return main_window


def set_mic_btn_color(color):
    global mic_btn
    mic_btn.config(bg=color)


def set_output_text(text):
    global output_text


def get_entry(text):
    global entry

