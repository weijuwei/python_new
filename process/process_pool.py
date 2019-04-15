from multiprocessing import Pool
import os,time,random


def long_time_task(name):
	print("子进程 %s pid: %s ..." %(name,os.getpid()))
	start = time.time()
	time.sleep(random.random()*3)
	end = time.time()
	print("子进程 %s 运行 %0.2f seconds" %(name,end-start))


if __name__ == '__main__':
	print("父进程id：",os.getpid())

	p = Pool(4)  # 创建进程池

	for i in range(1,5):
		p.apply_async(long_time_task,args=(i,))  # 创建子进程任务
	print("等待所有子进程完成。。。。")

	p.close()
	p.join()
	print("所有子进程完成。。。。")
# 对Pool对象调用join()方法会等待所有子进程执行完毕，
# 调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了