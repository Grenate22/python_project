speed=int(input('Speed of a driver' ))
speed_limit=70
points=12
point_count=0
while point_count<=12:
    if speed>speed_limit:
        point_count+=(speed-speed_limit)//5
        print(f'points:{point_count}')
        speed = int(input('Speed of a driver'))
        if point_count>=12:
            print('Licence Suspended')
            break

    else:
        print('ok')
        break





