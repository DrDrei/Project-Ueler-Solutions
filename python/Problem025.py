import time

def main():
    fibList = list()
    fibList.append(1)
    fibList.append(1)
    strLength = len(str(fibList[-1]))
    startTime = time.time()
    while strLength != 1000:
        fibList.append(fib(fibList[-1], fibList[-2]))
        strLength = len(str(fibList[-1]))
    endTime = time.time()
    print('Calculation took: ' + str(endTime-startTime) + 'sec')
    print('Index: ' + str(len(fibList)))
    
def fib(one, two):
    return one+two   

if __name__ == "__main__":
    main()