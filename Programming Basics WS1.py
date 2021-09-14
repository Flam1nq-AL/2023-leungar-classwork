def check_paint():
    l = int(input('Please input length'))
    w = int(input('Please input width'))
    h = int(input('Please input height'))

    total = (l*w) + (w*h*2) + (l*h*2)
    paint = (total // 11) + 1
    print(f"{paint} buckets of 1 litre paint are needed to paint  {total}  sq.m of wall.")


check_paint()
