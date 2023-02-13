def hanoi(disks,source,helper,destination):
    if(disks==1):
        print('Disks{} moves from tower {} to tower {} .'.format(disks,source,destination))
        return

    hanoi(disks-1,source,destination,helper)
    print('Disks{} moves from tower {} to tower {} .'.format(disks,source,destination))
    hanoi(disks-1,helper,source,destination)


disks=int(input('number of disks to be desplased'))   
'''
Tower names passed as arguments:
Source: A
Helper: B
Destination: C
'''
hanoi(disks, 'A', 'B', 'C')    
