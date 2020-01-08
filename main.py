import logging


logging.basicConfig(level=logging.DEBUG)


def is_even(number):
    # type: (float) -> bool
    if number % 2 == 0:
        return True
    return False


def algo_for_odd(number):
    # type: (float) -> float
    return (number * 3) + 1


def algo_for_even(number):
    # type: (float) -> float
    return number/2


max_loops_number = 0
max_loops_count = 0


for _x in range(1, 999999):
    x = _x
    looper = 0
    while x != 1:
        _old = x
        looper += 1
        if is_even(x):
            x = algo_for_even(x)
        else:
            x = algo_for_odd(x)
    logging.debug(('Finish with {} in {} loops'.format(_x, looper)))
    if max_loops_count < looper:
        max_loops_count = looper
        max_loops_number = _x

logging.info(('Max loops for number [{}], with {} loops '.format(max_loops_number, max_loops_count)))
