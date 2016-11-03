#!/usr/bin/env python
# -*-conding:utf-8-**
# __Author__:'liudong'
#!/usr/bin/env python
# -*-coding:utf-8-*-
# __author__="Life"
login_user = 'life'
login_passwd = '7777'
print('You have three times to login,otherwise your account will be locked!')
for i in range(3):
    username = input('Please input your username:')
    password = input('Please input your password:')
    lock_file = open('account_lock.txt', 'r')
    lock_list = lock_file.readlines()  # 已经被锁定用户清单文件
    for lock_line in lock_list:     #判断用户输入的名字是否已经锁定（在锁定的文件列表中）
        lock_line = lock_line.strip('\n')
        if username == lock_line:
            print('Your account is locked!')
            lock_file.close()
            exit()
    if username == login_user and password == login_passwd:
        print('login successed!')
        break
    else:
        print('Invalid username or password...')
        print('this is the %d time(s)' % (i + 1))
        continue
if i >= 2:
    print('Your account is locked! Please,contact adminstrator to unlock your account!')
    lock_file = open('account_lock.txt', 'w')
    lock_file.write(username + '\n')    #锁定用记名写入锁定文件
lock_file.close()