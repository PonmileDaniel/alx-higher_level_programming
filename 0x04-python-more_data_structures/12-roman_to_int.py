#!/usr/bin/python3
def to_sub(list_num):
    to_su = 0
    max_list = max(list_num)
    for n in list_num:
        if max_list > n:
            to_su += n
    return (max_list - to_su)


def roman_to_int(roman_string):
    if not roman_string:
        return (0)
    if not isinstance(roman_string, str):
        return (0)

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_key = list(rom_n.keys())
    num = 0
    last_rom = 0
    list_num = [0]
    for h in roman_string:
        for rnum in list_key:
            if rnum == h:
                if rom_n.get(h) <= last_rom:
                    num += to_sub(list_num)
                    list_num = [rom_n.get(h)]
                else:
                    list_num.append(rom_n.get(h))
                last_rom = rom_n.get(h)
    num += to_sub(list_num)
    return (num)
