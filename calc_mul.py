#!/usr/bin/python3

def calc(A, B):
    try:
        a = float(A)
        b = float(B)
    except (ValueError, TypeError):
        return -1

    if 0 < a < b < 1000:
        return a * b
    else:
        return -1



def main():
    """
    ユーザーからの入力を受け取り、calc関数を使用して計算結果を出力します。
    """
    while True:
        A = input("Input A (or type 'end' to exit): ")
        if A.lower() == 'end':
            break
        B = input("Input B: ")
        print("Result:", calc(A, B))

if __name__ == '__main__':
    main()
