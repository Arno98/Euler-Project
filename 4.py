def pal():
    pal_num = []
    pal_num_2 = []
    pal_num_3 = []
    for x in range(1000, 9999):
        x = str(x)
        if x == x[::-1]:
            pal_num.append(x)
            
    for y in pal_num:
        y = int(y)
        pal_num_2.append(y)
        for d in range(10, 99):
            if y % d == 0:
                result = y / d
                if result in range(10, 100):
                    m = int(result * d)
                    pal_num_3.append(m)
    if max(pal_num_3) in pal_num_2:
      for y in range(10, 99):
        if max(pal_num_3) % y == 0:
          res = int(max(pal_num_3) / y)
          if res in range(10, 100):
            print(max(pal_num_3), y, res)
pal()
