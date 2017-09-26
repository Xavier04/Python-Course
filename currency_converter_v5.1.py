"""
程序结构化
"""


# def exchange(value, tmp_rate):
#     """
#         汇率兑换函数
#     """
#     result = value * tmp_rate
#     return result


def main():
    """
        主函数
    """
    cny_vs_usd = 6.77

    currency_str_value = input('input currency with unit:')
    currency_unit = currency_str_value[-3:]
    currency_value = eval(currency_str_value[:-3])

    if currency_unit == 'CNY':
        rate = 1 / cny_vs_usd
        unit = 'USD'
    elif currency_unit == 'USD':
        rate = cny_vs_usd
        unit = 'CNY'
    else:
        rate = -1

    if rate != -1:
        # 使用lambda定义函数
        exchange2 = lambda x, y: x * y
        exchange_result = exchange2(currency_value, rate)
        # exchange_result = exchange(currency_value, rate)
        print('The exchanged currency is:', exchange_result, unit)
    else:
        print('input the wrong type!')


if __name__ == '__main__':
    main()
