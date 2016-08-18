# -*- coding: utf8 -*-

def longest_palindromic(text):
    """
    :param text: string
    :return:the longest palindromic substring, or if there are more then one
    palindromic substring it return the first from them
    """
    result = ''
    max_len = 0
    list_palind = []
    n = len(text)
    for x in range(n+1):
        for y in range(x+1, n+1):
            substr = text[x:y]
            if substr[::-1] == substr:
                list_palind.append(substr)
    for i in list_palind:
        l = len(i)
        if l > max_len:
            result = i
            max_len = l
    return result
