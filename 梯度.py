def decimal_to_binary(decimal_num, precision=10):

    if decimal_num < 0:
        return "-" + decimal_to_binary(-decimal_num, precision)

    integer_part = int(decimal_num)
    fractional_part = decimal_num - integer_part

    if integer_part == 0:
        binary_integer = "0"
    else:
        binary_integer = ""
        temp_int = integer_part
        while temp_int > 0:
            binary_integer = str(temp_int % 2) + binary_integer
            temp_int = temp_int // 2

    binary_fraction = ""
    temp_frac = fractional_part
    count = 0

    while temp_frac > 0 and count < precision:
        temp_frac *= 2
        bit = int(temp_frac)
        binary_fraction += str(bit)
        temp_frac -= bit
        count += 1

    if not binary_fraction:
        return binary_integer
    else:
        return f"{binary_integer}.{binary_fraction}"

if __name__ == "__main__":
    # 测试用例
    test_numbers = [0.25, 0.8125, 10.625, 0.3, 0.1]

    print("十进制小数转二进制小数测试：")
    print("-" * 40)

    for num in test_numbers:
        binary_result = decimal_to_binary(num)
        print(f"十进制 {num} → 二进制 {binary_result}")

    try:
        user_input = float(input("\n请输入一个十进制小数: "))
        user_precision = int(input("请输入精度位数(默认10): ") or "10")
        result = decimal_to_binary(user_input, user_precision)
        print(f"转换结果: {result}")
    except ValueError:
        print("输入无效，请输入有效的数字")