
def long_collatz_seq(end_num):
    def find_next_num(num):
        if num % 2 == 0:
            return num/2
        else:
            return 3 * num + 1


    steps_dic = {1: 0,}
    max_steps = 0
    max_num = 0
    
    def save_num(num_par, steps_par):
        num = int(num_par)
        steps = int(steps_par)
        steps_dic[num] = steps
##        print("SAVED", num, steps)
        return 0

    def find_collatz_seq(num):
        if num in steps_dic:
##            print("FOUND", steps_dic)
            return steps_dic[num]
        else:
            next_num = find_next_num(num)
            search_steps = find_collatz_seq(next_num)
##            print(search_steps+1)
            save_num(num, search_steps+1)
##            print("SAVE", num, search_steps+1)
##            print(steps_dic)
            return search_steps+1

    for i in range(2, end_num + 1):
        num_steps = find_collatz_seq(i)
        steps_dic[i] = num_steps
        if num_steps > max_steps:
            max_steps = num_steps
            max_num = i

##    print(steps_dic)
    return max_num

print(long_collatz_seq(999999))
