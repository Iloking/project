# Sum of natural numbers
def func1(n):
    iteration = 0
    iteration += 1
    print(f"For {n}, iteration is {iteration}")
    return n * (n + 1) / 2

func1(4)
func1(100)
# Time complexity = O(1)
# Space complexity = O(1)

def func2(n):
    iteration = 0
    sum = 0
    for i in range(1, n+1):
        sum += i
        iteration += 1
    print(f"For {n}, iteration is {iteration}")

func2(4)
func2(100)
