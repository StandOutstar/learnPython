
print('please input your account name:')
# input() 计算机等待输入，输入并按回车键确认，输入读取到name中
name = input()
if name == '':
    print('please input your name again:')
print('now input your password:')
password = input()
if password == 'zxk':
    print('%s login success!' % name)
elif password == '':
    print('please input your password again:')
else:
    print('your password is not correct.')
