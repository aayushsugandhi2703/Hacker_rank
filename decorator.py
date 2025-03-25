def wrapper(f):
    def fun(l):
        arr =[]
        for i in l:
            num = i[-10:]  # Extract last 10 digits
            formatted_num = f"+91 {num[:5]} {num[5:]}"
            arr.append(formatted_num)
        return f(arr)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 