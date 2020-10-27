# from datetime import datetime

# week = ('Mon', 'Tue', 'Wen')

# # easier way to write the date
# now = datetime.now()
# dt_string = now.strftime("%b %d %H:%M:%S %Y")
# dt_string = week[now.weekday()] + " " + dt_string
# print(dt_string)	

# # easier way to calculate statistics

# # example of main results list
# l = [
#     ('a', 'a', 1),
#     ('b', 'b', 2),
#     ('c', 'd', 3),
# ]

# #initialization of variables
# right = 0
# wrong = 0
# r_time = 0
# w_time = 0

# # iteration trough list to calculate variables
# for t in l:
#     if t[0] == t[1]:
#         right += 1
#         r_time += t[2]
#     else:
#         wrong += 1
#         w_time += t[2]
    
# # print results
# print("number of hits: " + str(right))
# print("total time of hits: " + str(r_time))
# print("number of misses: " + str(wrong))
# print("total time of misses: " + str(w_time))
# print("total time: " + str(r_time + w_time))
# print("total time 2: " + str())

import readchar
import time
import signal    
    
def funcao_para_interroper():
    while True:
        try:
            print('press a key')
            c = readchar.readchar()
            print('you pressed ' + c)
        except:
            print("O tempo acabou")
            break


def main():
    signal.signal(signal.SIGALRM, funcao_para_interroper)
    signal.alarm(3)
    funcao_para_interroper()
    
if __name__ == "__main__":
    main()
    