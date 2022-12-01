




def verifyInput(inp, typ):
    # use typ to determine object type
    # to determine function to apply in the try statement

    while True:
        try: out = type(typ)
        except: continue
        break


def receiveInputs():

    print('How many walls are there?')
    
    while True:
        try: nWalls = int(input())
        except: continue
        break

    wallWidths = list()
    for n in range(nWalls):
        print('Enter width of wall #' + str(n) + ':') #verify this input too
        wallWidths.append()

    while True:
        print('Enter Valid Height:')
        try: h = float(input())
        except: continue
        else: break

    while True:
        print('Enter Valid Width:')
        try: w = float(input())
        except: continue
        else: break
    
    while True:
        print('Enter Valid Depth:')
        try: d = float(input())
        except: continue
        else: break

    return h,w,d


def getVolume(h,w,d):
    return h*w*d

def getWallArea(h,w,d):
    return 2*h*w + 2*h*d

def getFloorArea(h,w):
    return h*w

if __name__ == "__main__":
    h,w,d = receiveInputs()
    print(getVolume(h,w,d))
    print(getWallArea(h,w,d))
    print(floorArea(h,w))