'''
操作系统
1. 内存管理
2. 驱动管理
3. 进程线程协程
4. 文件系统

1. 内存
32位电脑 4G
DOS 内存是程序自己控制
Windows 统一的内存空间 4G
虚拟存储器
1. CPU n核心  ALU cpu寄存器
2. 每个核心 L1 L2
3. 整个CPu L3 3M
4. 内存 很大很大8G
5. 硬盘
6. 网络传输

虚拟存储器，统一的内存模型
一个程序 4G 内存+硬盘
电脑4G
a 1G -> 内存中  页表
b 1G -> 内存中  页表

c 3G -> 把a存储，把c load进来

a => page fault
''''''
操作系统
1. 内存管理
2. 驱动管理
3. 进程线程协程
4. 文件系统

1. 内存
32位电脑 4G
DOS 内存是程序自己控制
Windows 统一的内存空间 4G
虚拟存储器
1. CPU n核心  ALU cpu寄存器
2. 每个核心 L1 L2 cache miss
3. 整个CPu L3 3M
4. 内存 很大很大8G
5. 硬盘
6. 网络传输

虚拟存储器，统一的内存模型
一个程序 4G 内存+硬盘
电脑4G
a 1G -> 内存中  页表
b 1G -> 内存中  页表

c 3G -> 把a存储，把c load进来

a => page fault => page load => 正常运行

2. 驱动
    ps/2 usb bluetooth
    flopy disk
    linux: 统一成文件 read write seek
3. 文件系统
    数组
    [meta元信息 对应的文件位置（偏移量） 对应的文件大小]
    格式化： 会把所有信息抹掉
    快速格式化：meta清空

    所有的问价你，存在同一个file
    /main/main.py -> file load -> execute
'''

'''
1. 进程 pid 时间片
2. 多线程
3. 线程和进程
    进程间通信 pipe file socket
    线程通信 n线程来说 我都可以看到进程中的全局数据

    对于一个进程来说，你持有了一个页表
    对于同一个进程内的线程，你共享同一张页表
4. 多线程同步问题

    数组 支持add
    1. 把数组size + 1
    2. 把add的这个数字放在 data[size]

    两个线程 同时add
    1. A线程 走了1
    2. B线程 也走了1
    3. A存了数据 data[size] = xxx
    4. B也存了数据 data[size] = xxx

    核心在于
    你的操作被拆分
    解决方案呢？
    1. atomic swap_and_cmp
    2. 加锁，mutex，信号量，读写锁，自旋锁。

    加锁以后，我对这个资源有所有权，
    在我所有操作没有结束前，
    其他操作这个数据的人，就要等待

    数组 支持add
    1. 加锁
    2. 把数组size + 1
    3. 把add的这个数字放在 data[size]
    4. 解锁

    两个线程 同时add
    1. A线程 走了1
    2. B线程 也走了1
    3. A 2
    4. A 3
    5. A 解锁
    4. b走2，3，4

    同步会有问题？产生了死锁
    哲学家进餐

    1. 为什么死锁？获取资源的顺序不一样
    对于底下哲学家 先1后2
    对于上面哲学家 先2后1

    所有的哲学家都是先1后2
    1. 调整最后一个人的顺序
    2. 如果我那不到右手，那我左手的也不要

    线程安全的交换数据的函数
    swap(a,b)
    id(a) id(b)
    a.lock()
    b.lock()
    exchange(a.data, b.data)
    a.unlock()
    b.unlock()

    swap(a,b) ------ swap(b,a)

    Python? GIL global interpreter lock

    并发 并行
    不管你多少个线程，只要你系统能处理多个事情，就是并发的
    并行 这些事情都是在同一时间执行的 多线程 多进程

    同步异步 事件发生与否，需要你自己去检查
             事件的发生与否，这个是别人通知给你的
    阻塞非阻塞
            阻塞 等
            不等，就是非阻塞
'''

'''
编译 解释 JIT
编译？ 一个代码编译成另外一种代码，编译到机器码，目标代码就是机器码
解释？ c语言是统一的，那我用c语言写出一个虚拟机，这个机器是可以部署到任何机器的
     python语言，语言逐条转换成对应的虚拟机指令
JIT just in time compiler 把最热的代码替换成编译到机器码

动态VS静态
a = ''
a = 1
a = True

a = ''
a = 'hello'
a = 'test'

强类型弱类型
1 + '1'
1 + 1

有GC 无GC garbage collection
new delete // malloc free c, c++
有gc: java golang python ruby scala js
new
1. mark & sweep concurrent mark sweep
2. ref counting

python
1. ref counting
2. mark & sweep

a b
a.parent = b
b.child = a

weakref
'''

'''
1. generator
2. iterator
3. class method, instance method, static method
4. lambda closure
5. *args **kwargs
6. magic method
7. list comprehension
8. dict comprehension
9. decorator
10.默认参数
'''

'''
1. generator
for i in range(1000000000)
for i in xrange(100000000)

l = [1...1000000000]
for i in l:
    print(i)

希望1就够了
'''


def my_range(n):
    i = 0
    while i != n:
        i += 1
        yield i


r = my_range(10)
for i in r:
    print(i)


