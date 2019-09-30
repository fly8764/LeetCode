class Solution:
    # def scheduleCourse(self, courses):
    #     #按照课程的长短来升序排序，课程短的先学习，这种方法通过率更低
    #     n = len(courses)
    #     #先按照结束时间的早晚排序，早的排在前面，越早结束的，越能学习更多的知识
    #     a = sorted(courses,key = lambda x:x[0])
    #     cnt = 0
    #     start = 0
    #     for i in range(n):
    #         item = a[i]
    #         if start + item[0] <= item[1]:
    #             start += item[0]
    #             cnt += 1
    #         else:
    #             continue
    #     return cnt

    # def scheduleCourse(self, courses):
         #先按照结束时间的早晚排序，早的排在前面，越早结束的，越能学习更多的知识，不能全部通过
    #     n = len(courses)
    #
    #     a = sorted(courses,key = lambda x:x[1])
    #     cnt = 0
    #     start = 0
    #     for i in range(n):
    #         item = a[i]
    #         if start + item[0] <= item[1]:
    #             start += item[0]
    #             cnt += 1
    #         else:
    #             continue
    #     return cnt

    def scheduleCourse(self, courses):
        #先根据 课程的结束时间排序，先结束的排在前面，这样才能尽可能多的上课
        #如果 上了当前课后，超时，则比较这节课和已选择的课程中的最长时长比较，
        #如果当前课的时长较短，则剔除已选课程中最大时长课，选择当前课，毕竟选择时长短的课，最终的课程数才多
        #这里就需要用到 优先队列，但python中没有优先队列，只好用 堆排序，默认时最小堆，加个负号，变成“最大堆”
        #时刻修改起始时间
        n = len(courses)
        courses.sort(key=lambda x: x[1])
        q = []
        start = 0
        for item in courses:
            if start + item[0] <= item[1]:
                q.append(item[0])
                start += item[0]
            elif q and item[0] < q[-1]:
                #这里别忘了队列不能为空
                start += item[0] - q[-1]
                q.pop()
                q.append(item[0])
        return len(q)


if __name__ == '__main__':
    so = Solution()
    courses =  [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
    res = so.scheduleCourse(courses)
    print(res)

