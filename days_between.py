# -*- coding: utf8 -*-

def days_diff(first_d, second_d):
    """
     Find absolute diff in days between dates
     :param first_d,second_d - tuples with integer numbers: (yyyy, m, dd)
     :return absolute value
    """
    import datetime
    delta_days = (datetime.date(*first_d) - datetime.date(*second_d)).days
    absolute_value = abs(delta_days)
    return absolute_value


print days_diff((1982, 4, 19), (1982, 4, 22))

