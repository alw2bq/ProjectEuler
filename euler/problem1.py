def solution():
    answer = 0

    for n in range(1000):
        if n % 3 == 0 or n % 5 == 0:
            answer = answer + n

    return answer


if __name__ == "__main__":
    print(solution())
