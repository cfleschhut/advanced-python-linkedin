nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

new_nums = list(
    map(lambda num: num ** 2,
        filter(lambda num: num > 4 and num < 16, nums)
        )
)

new_nums = [n ** 2 for n in nums if n > 4 and n < 16]

print(new_nums)
