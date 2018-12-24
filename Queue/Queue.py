#!/usr/bin/env python3

"""
1.Queue使用方法：
Queue.qsize()：返回当前队列包含的消息数量；
Queue.empty()：如果队列为空，返回True，反之False ；
Queue.full()：如果队列满了，返回True,反之False；
Queue.get():获取队列中的一条消息，然后将其从列队中移除，可传参超时时长。
Queue.get_nowait()：相当Queue.get(False),取不到值时触发异常：Empty；
Queue.put():将一个值添加进数列，可传参超时时长。
Queue.put_nowait():相当于Queue.get(False),当队列满了时报错：Full。
"""

import time
from multiprocessing import Process,Queue

#创建队列
q = Queue()
for i in range(11):
	q.put(i)

def FuncA():
	while 1:
		try:
			num = q.get_nowait()
			print("我是进程A，取出数字:%d"%(num))
			#q.put(num + 1)
			time.sleep(1)
		except:
			print('except A')
			break

def FuncB():
	while 1:
		try:
			num = q.get_nowait()
			print("我是进程B，取出数字:%d"%(num))
			time.sleep(1)
			#q.put(num + 1)
		except:
			print('except B')
			break

def main():
	p1 = Process(target = FuncA)
	p2 = Process(target = FuncB)
	p1.start()
	p2.start()

if __name__ == '__main__':
	main()