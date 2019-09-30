#要考虑相同长度的情况
def find_longest_num_str(s):
    maxx,longest_str,temp,cnt = 0,[],0,''
    for key,value in enumerate(s):
        if '0'<= value <='9':
            cnt += 1
            temp += value

            if cnt > maxx:
                maxx = cnt
                longest_str = [temp]
            elif cnt == maxx:
                longest_str.append(temp)
        else:
            cnt = 0
            temp = ''

    if not maxx:
        return '0/'
    else:
        return str(maxx)+'/'+''.join(longest_str)

# def find_longest_num_str(s):
#     size = len(s)
#
#     table = list(map(str, range(10)))
#     temp = ''
#     cnt = 0
#
#     longest_str = ''
#     maxx = 0
#     for i in range(size):
#         while '0'<= s[i]<= '9':
#             temp += s[i]
#             cnt += 1
#             i += 1
#         if maxx < cnt:
#             maxx = cnt
#             longest_str = temp
#         cnt = 0
#         temp = ''
#
#         # if s[i] in table:
#         #     temp += s[i]
#         #     cnt += 1
#         # else:
#         #     if maxx < cnt:
#         #         maxx = cnt
#         #         longest_str = temp
#         #         cnt = 0
#         #         temp = ''
#
#     if not maxx:
#         return '0/'
#     else:
#         return str(maxx)+'/'+longest_str


if __name__ == '__main__':
    line = input()
    res = find_longest_num_str(line)
    print(res)