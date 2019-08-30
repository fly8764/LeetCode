import  sys


def find(mig,row,col):
    if row == 1 and col == 1:return False

    for i in range(row):
        #单行
        #单列
        for j in range(col):
            if mig[i][j] == 'S':
                if i == 0:
                    #单行
                    if j == 0:
                        if mig[i][j+1] == '#' and mig[i+1][j] == '#' and mig[-1][j] =='#' and mig[i][-1] == '#':
                            return False



if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        line = sys.stdin.readline().strip()
        shape = list(map(int,line.split()))
        row,col = shape[0],shape[1]
        mig = []
        for _ in range(row):
            line = sys.stdin.readline().strip()
            nums = list(map(str,line))
            mig.append(nums)
        # print(mig)
