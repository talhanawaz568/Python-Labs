import multiprocessing

def sum_large_list(num_list):
    total = sum(num_list)
    print(f"Sum of the list is: {total}")

numbers = list(range(1000000))

if __name__ == '__main__':
    process1 = multiprocessing.Process(target=sum_large_list, args=(numbers,))
    process2 = multiprocessing.Process(target=sum_large_list, args=(numbers,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()
