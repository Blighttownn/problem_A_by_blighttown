import time
if __name__=="__main__":
    K = int(input("введите расстояние между автобусными останвками: "))
    M = int(input("введите расстояние которое прошла Света: "))
    start_time = time.time()
    distance_to_next_stop = M % K
    print(min(distance_to_next_stop, K - distance_to_next_stop))
    print("время выполнения: ")
    print(time.time()-start_time)