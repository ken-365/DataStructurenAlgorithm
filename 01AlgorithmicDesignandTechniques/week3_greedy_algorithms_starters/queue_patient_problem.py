# Naive
import sys
import time
def queue_patient_Naive(list_of_wait_time,n):
    sorted_list_of_wait_time = sorted(list_of_wait_time)
    print(sorted_list_of_wait_time)
    accumulate_wait_time = [0]
    wait_time = 0
    total_waittime = [0]
    for i in range(n-1):
        wait_time += sorted_list_of_wait_time[i]
        accumulate_wait_time.append(wait_time)
        total_waittime.append(sum(accumulate_wait_time))

    print(accumulate_wait_time)
    print(total_waittime)
    return sum(total_waittime)

# print(queue_patient_Naive([15,20,10],3))

# Greedy
def queue_patient_greedy(t,n):
    waitingTime = 0
    treated = [0] * (n)
    # find the minimum time treatment of all patient
    for _ in range (n):
        t_min = float("inf")
        #init index of min wait time
        minIndex = 0
        #loop through patients and treat the patient that are not treated yet
        for j in range (n):
            # if treated[j] = 0 mean not treated yet and if it is minimum
            if treated[j] ==0 and t[j] < t_min:
                t_min = t[j]
                minIndex = j
        # number of people in the queue (left) will need to wait t_min time
        waitingTime = waitingTime + (n-1) * t_min
        # change to 1 signal that this patient already treated
        treated[minIndex] =1
    # the run time is O(n2)
    return waitingTime


# start_time = time.time()
# print('answer is',queue_patient_Naive([5,46,854,5,3,22,2],7), 'took time ' ,"--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print('answer is',queue_patient_greedy([5,46,854,5,3,22,2],7), 'took time ' ,"--- %s seconds ---" % (time.time() - start_time))

# start_time = time.time()
# print('answer is',fibonacci_fast(888888), 'took time ' ,"--- %s seconds ---" % (time.time() - start_time))

