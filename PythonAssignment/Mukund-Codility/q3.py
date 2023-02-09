# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.


def si():  return input()

if __name__ == "__main__":
    S = "Sat"
    K = 23
    dic = {"Mon":0, "Tue":1, "Wed":2, "Thu":3, "Fri":4, "Sat":5, "Sun":6}
    ans = (dic[S]+K)%7
    # print(dic.keys()[dic.values().index(ans)])
    for day, num in dic.items():
        if ans == num:
            print(day)

    # freq = 26*[0]
    # for _ in s:
    #     freq[ord(_)-65] += 1
    
    # #1 -> B, 2 -> N, 3 -> A
    # print(min(freq[1], freq[13]//2, freq[0]//3))
    
    