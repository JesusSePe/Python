def downgrade(num):
    if num == 0:
        print(num)
        return
    else:
        print(num)
        return downgrade(num-1)


downgrade(15)
