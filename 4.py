import time

#1 задание

def f1(*args):
    try:
        sum = 0
        for i in args:
            sum += int(i)
        return sum/len(args)
    except Exception:
        print("Error!" + str(Exception))

#тест 1
print("test 1", f1(1,2,3,4,5))
#тест 2
print('test 2', f1())
#тест 3
print('test 3', f1(1,1.0,2,3,4))
#тест 4
print('test 4', f1(1,'2',3,'4',5))
#тест 5
print('test 5', f1(1,'a',3,'b',5))
#тест 6
print('test 6', f1(1,2,3,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5))

#2 задание

def f2(**kwargs):
    for key, value in kwargs.items():
        print("key =", key, "value =", value)

f2(k1= 1, k2=2, k3= 3)

#3 задание
def f3(x):
    try:
        a = 10/x
    except Exception:
        print("Error!" + str(Exception))
    else:
        print('a=', a)
    finally:
        print('x=', x)

f3(5)
f3(0)
#блок else срабатывает если в try нет исключения, блок finally срабатывает всегда

#4 задание

def f4(nums, k):
    if len(nums)!= 0:
        k = k % len(nums)
        for i in range(k):
            nums.insert(0, nums.pop())
    return nums

def test():
    #тест 1
    nums = [1,2,3,4,5,6,7]
    k = 3
    print('test 1')
    print('nums=', nums)
    print('k=',k)
    print('result=', f4(nums, k))

    #тест 2
    nums = [1,2,3,4,5,6,7]
    k = 126
    print('test 2')
    print('nums=', nums)
    print('k=',k)
    print('result=', f4(nums, k))

    #тест 3
    nums = []
    k = 7
    print('test 3')
    print('nums=', nums)
    print('k=',k)
    print('result=', f4(nums, k))

    #тест 4
    nums = []
    for i in range(10000):
        nums.append(i)
    k = 121
    print('test 4')
    print('nums=', nums)
    print('k=',k)
    print('result=', f4(nums, k))

    #тест 5
    nums = nums = [1,2,3,4,5,6,7]
    k = 52
    print('test 5')
    print('nums=', nums)
    print('k=',k)
    print('result=', f4(nums, k))

test()

#5 задание

def f5(nums):
    countzero = 0
    i = 0
    while i < len(nums):
        if i + countzero < len(nums):
            if(nums[i + countzero] == 0):
                countzero += 1
                continue
            else:
                nums[i] = nums[i + countzero]
        else: break
        i += 1
    while i < len(nums):
        nums[i] = 0
        i += 1
    return nums

def test2():
    #тест 1
    nums = [0,1,0,3,12]
    print('test 1')
    print('nums=', nums)
    print('result=', f5(nums))

    #тест 2
    nums = []
    for i in range(1000):
        if i % 2 == 0: nums.append(0)
        else: nums.append(i)
    print('test 2')
    print('nums=', nums)
    print('result=', f5(nums))

    #тест 3
    nums = [0,0,0,0,1,3,12]
    print('test 3')
    print('nums=', nums)
    print('result=', f5(nums))

    #тест 4
    nums = [0,0,0,0,1,3,0,0,12]
    print('test 4')
    print('nums=', nums)
    print('result=', f5(nums))

    #тест 5
    nums = [-100,150,0,0,1,3,12,0,0]
    print('test 5')
    print('nums=', nums)
    print('result=', f5(nums))

    #тест 6
    nums = [0,0,0,0]
    print('test 6')
    print('nums=', nums)
    print('result=', f5(nums))

    #тест 7
    nums = [1,3,12,0,0,0,0]
    print('test 7')
    print('nums=', nums)
    print('result=', f5(nums))

    #тест 8
    nums = [0,0,0,0,0,0,0,0,1,0,0,0,0]
    print('test 8')
    print('nums=', nums)
    print('result=', f5(nums))

test2()