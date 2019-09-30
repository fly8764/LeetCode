if __name__ =='__main__':
    line = list(input().split())
    if len(line) > 0:
        if line[-1] == '.':
            line.pop()
            # line.append(bottom[:-1])
            line = line[::-1]
            print(' '.join(line) + '.')
            # line = line[:-1]
        else:
            # print(line)
            bottom = line[-1]
            line.pop()
            line.append(bottom[:-1])
            line = line[::-1]
            print(' '.join(line) + '.')
    else:
        print('')



