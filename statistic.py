import os
import sys
import re

from consolemenu import ConsoleMenu, MultiSelectMenu
from consolemenu.items import FunctionItem, SubmenuItem, SelectionItem, MenuItem


def get_directory_content(directory: str = None, only_files: bool = False):
    directory_content = None
    result_list = []
    if not directory:
        directory_content = os.listdir(os.getcwd())
    else:
        directory_content = os.listdir(directory)
    if only_files:
        for current_item in directory_content:
            if os.path.isfile(directory + os.path.sep + current_item):
                result_list.append(current_item)
    else:
        return directory_content
    return result_list


def show_tasks_menu():
    options_list = ["Amount of lines in file",
                    "Amount of empty lines in file",
                    "Amount of lines with \"z\" in file",
                    "Amount of \"z\" in file",
                    "Amount of \"and\" in file",
                    "All of them"]
    statistic_items_menu = MultiSelectMenu("Select items, you want to do:",  exit_option_text='Continue')
    i = 0
    tasks_to_do = []
    for current_item in options_list:
        statistic_items_menu.append_item(FunctionItem(current_item,
                                                      lambda item: tasks_to_do.append(item),
                                                      [i, ],
                                                      should_exit=True))
        i += 1
    statistic_items_menu.show()

    if not tasks_to_do:
        tasks_to_do.append(5)
    return tasks_to_do


def get_statistic(file_path: str):
    tasks_to_do = show_tasks_menu()
    print("File: {0}".format(file_path))
    num_lines = 0
    num_lines_with_z = 0
    num_empty_lines = 0
    z_occurrences = 0
    and_occurrences = 0
    for line in open(file_path, 'rb'):
        z_per_line = 0
        if (5 in tasks_to_do) or (0 in tasks_to_do):
            num_lines += + 1
        if not line.strip() and ((5 in tasks_to_do) or (1 in tasks_to_do)):
            num_empty_lines += + 1
        if (5 in tasks_to_do) or (2 in tasks_to_do) or (3 in tasks_to_do):
            z_per_line = str(line).count("z")
        if (5 in tasks_to_do) or (3 in tasks_to_do):
            z_occurrences += z_per_line
        if z_per_line > 0 and ((5 in tasks_to_do) or (2 in tasks_to_do)):
            num_lines_with_z += + 1
        if (5 in tasks_to_do) or (4 in tasks_to_do):
            and_per_line = str(line).count("and")
            and_occurrences += and_per_line

    if (5 in tasks_to_do) or (0 in tasks_to_do):
        print("Amount of lines in {0}:\t{1}".format(file_path, num_lines))
    if (5 in tasks_to_do) or (1 in tasks_to_do):
        print("Amount of empty lines in {0}:\t{1}".format(file_path, num_empty_lines))
    if (5 in tasks_to_do) or (2 in tasks_to_do):
        print("Amount of lines with \"z\" in {0}:\t{1}".format(file_path, num_lines_with_z))
    if (5 in tasks_to_do) or (3 in tasks_to_do):
        print("Amount of \"z\" in {0}:\t{1}".format(file_path, z_occurrences))
    if (5 in tasks_to_do) or (4 in tasks_to_do):
        print("Amount of \"and\" in {0}:\t{1}".format(file_path, and_occurrences))
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
                                                         [current_dir_item_path, ]))
        elif os.path.isdir(current_dir_item_path):
            current_sub_menu = ConsoleMenu("Select file from:", current_dir_item_path)
            sub_directory_content = get_directory_content(current_dir_item_path, True)
            for current_subdir_item in sub_directory_content:
                current_sub_menu.append_item(FunctionItem(current_subdir_item,
                                                          get_statistic,
                                                          [current_dir_item_path + os.path.sep + current_subdir_item, ]))
            file_selection_menu.append_item(SubmenuItem(current_dir_item + os.path.sep, current_sub_menu))
    file_selection_menu.show()


def main():
    output_console_menu()


if __name__ == "__main__":
    main()
