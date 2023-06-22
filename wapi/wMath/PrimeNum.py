# 质数判断器 by wyf9, Dobastickrn 2023.4.1

# Input: int(num) / str(num) -> be a num
# Back: True / False
def wMain(num0):
    num = int(num0)
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False