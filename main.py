# 学生需要在此文件中实现 PrimeList 函数

def PrimeList(N):
    """
    返回小于 N 的所有质数，以空格分隔
    
    参数:
    N - 正整数
    
    返回:
    str - 包含所有小于 N 的质数的字符串，空格分隔
    """
    # 边界情况处理
    if N <= 2:
        return ""
    
    # 初始化质数列表
    primes = []
    
    # 使用筛选法查找质数
    is_prime = [True] * N
    is_prime = is_prime = False  # 0 和 1 不是质数
    
    for num in range(2, N):
        if is_prime[num]:
            primes.append(str(num))  # 添加质数
            # 标记质数的倍数
            for multiple in range(num * num, N, num):
                is_prime[multiple] = False
    
    # 返回空格分隔的字符串
    return " ".join(primes)
