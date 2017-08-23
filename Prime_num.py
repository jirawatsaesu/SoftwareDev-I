# Prime number
# Sieve of Eratosthenes
#
# Jirawat Yuktawathin
# start : 16/8/2017
# stop  : 18/8/2017
#
# Python version : 2.7

from Tkinter import *
import time

root = Tk()

start = int(input('First number : '))
stop = int(input('Last Number   : '))

# Draw a table
table = [None] * stop
j = 0
for i in range(start, stop):
    table[i] = Label(root, width=8, height=4, bg='#e7e4e4', bd='2',\
                       text=i + 1, relief="sunken")
    if i % 20 == 0:
        j += 1
    if i == 0:
        pass
    else:
        table[i].grid(row=j, column=(i % 20))

root.update()

num_list = list(range(2, stop + 1))
color_list = ['green', 'blue', 'red', 'yellow', 'brown', 'pink', 'purple']

# Remove all number if it's can divine by prime num.
for num in num_list:
    if num ** 2 > num_list[-1]:
        break
    print
    print('Divine by {} : '.format(num))

    i = 2
    while num * i <= num_list[-1]:
        try:
            num_list.remove(num * i)
            print(num * i),

            time.sleep(0.1)
            table[(num * i) - 1].config(bg = color_list[0])
            root.update()
        except ValueError:
            pass
        except AttributeError:
            pass

        i += 1
    color_list.append(color_list.pop(0))

for num in num_list:
    if num < start:
        num_list.remove(num)

print
print('Prime number : {}'.format(num_list))

mainloop()
