'''
    Ближайшая пятница 13
    Next Friday the 13th
'''
import time


def close_friday_13(date: time.struct_time = time.localtime()):
    import time
    seconds = time.mktime(date)
    cnt_day = 0
    date = time.localtime(seconds)
    sec = 60 * 60 * 24
    while 1 > 0:
        if date.tm_wday == 4 and date.tm_mday == 13:
            break
        else:
            cnt_day += 1
            seconds += sec
            date = time.localtime(seconds)
    print(time.strftime('%d.%m.%Y', date))
    return cnt_day


print(close_friday_13())
