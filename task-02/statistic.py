import os

from consolemenu import ConsoleMenu, MultiSelectMenu
from consolemenu.items import FunctionItem, SubmenuItem

tasks_list = ["Amount of lines in file",
              "Amount of empty lines in file",
              "Amount of lines with \"z\" in file",
              "Amount of \"z\" in file",
              "Amount of \"and\" in file",
              "All of them"]


def get_directory_content(directory: str = None, only_files: bool = False):
    result_list = []
    directory_content = {True: os.listdir(os.getcwd()), False: os.listdir(directory)}[directory is None]
    if only_files:
        for current_item in directory_content:
            if os.path.isfile(directory + os.path.sep + current_item):
                result_list.append(current_item)
    else:
        return directory_content
    return result_list


def show_tasks_menu(menu_items: list):
    statistic_items_menu = MultiSelectMenu("Select items, you want to do:", exit_option_text='Continue')
    i = 0
    tasks_to_do = []
    for current_item in menu_items:
        statistic_items_menu.append_item(FunctionItem(current_item,
                                                      lambda item: tasks_to_do.append(item),
                                                      [i, ],
                                                      should_exit=True))
        i += 1
    statistic_items_menu.show()

    return {True: [0, 1, 2, 3, 4], False: tasks_to_do}[tasks_to_do in [None, []]]


def get_statistic(file_path: str, options_list: list):
    tasks_to_do = show_tasks_menu(options_list)
    tasks_to_do = {True: [0, 1, 2, 3, 4], False: tasks_to_do}[5 in tasks_to_do or len(tasks_to_do) == 5]
    print("File: {0}".format(file_path))
    num_lines = 0
    num_empty_lines = 0
    z_occurrences = 0
    num_lines_with_z = 0
    num_lines_with_and = 0
    for line in open(file_path, 'rb'):
        num_lines += {True: 1, False: 0}[0 in tasks_to_do]
        num_empty_lines += {True: int(not bool(line.strip())), False: 0}[1 in tasks_to_do]
        z_per_line = {True: str(line).count("z"), False: 0}[2 in tasks_to_do or 3 in tasks_to_do]
        z_occurrences += z_per_line
        num_lines_with_z += int(bool(z_per_line))
        num_lines_with_and += {True: int(bool(str(line).count("and"))), False: 0}[4 in tasks_to_do]

    for current_task in tasks_to_do:
        result_string = {
            0: lambda: "Amount of lines in {0}:\t{1}".format(file_path, num_lines),
            1: lambda: "Amount of empty lines in {0}:\t{1}".format(file_path, num_empty_lines),
            2: lambda: "Amount of lines with \"z\" in {0}:\t{1}".format(file_path, num_lines_with_z),
            3: lambda: "Amount of \"z\" in {0}:\t{1}".format(file_path, z_occurrences),
            4: lambda: "Amount of lines with \"and\" in {0}:\t{1}".format(file_path, num_lines_with_and),
        }[current_task]()
        print(result_string)

    input("Press Enter to continue...")


def output_console_menu():
    start_directory = os.getcwd()
    directory_content = get_directory_content(start_directory, False)
    file_selection_menu = ConsoleMenu("Select file from:", start_directory)
    for current_dir_item in directory_content:
        current_dir_item_path = start_directory + os.path.sep + current_dir_item
        if os.path.isfile(current_dir_item_path):
            file_selection_menu.append_item(FunctionItem(current_dir_item,
                                                         get_statistic,
                                                         [current_dir_item_path, tasks_list]))
        elif os.path.isdir(current_dir_item_path):
            current_sub_menu = ConsoleMenu("Select file from:", current_dir_item_path)
            for current_subdir_item in get_directory_content(current_dir_item_path, True):
                current_sub_menu.append_item(FunctionItem(current_subdir_item,
                                                          get_statistic,
                                                          [
                                                              current_dir_item_path + os.path.sep + current_subdir_item, tasks_list]))
            file_selection_menu.append_item(SubmenuItem(current_dir_item + os.path.sep, current_sub_menu))
    file_selection_menu.show()


def main():
    output_console_menu()


if __name__ == "__main__":
    main()
