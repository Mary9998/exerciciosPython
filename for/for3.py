import time

print("Os fogos de artifício serão lançados em...")

for i in range(10, 0, -1):
    print(f'{i}...')

    if i > 0:
        time.sleep(1)
print('UHUUUUUUL!')