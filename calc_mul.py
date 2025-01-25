#!/usr/bin/python3

def calc(A, B):
    """
    AとBの積を計算します。ただし、次の条件を満たす場合のみ計算を行います:
    - AとBは数値である
    - 0 < A < B < 1000
    条件を満たさない場合、-1を返します。
    """
    try:
        # AとBを数値に変換
        a = float(A)
        b = float(B)
    except ValueError:
        # 数値変換に失敗した場合は-1を返す
        return -1

    # 条件をチェック
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
