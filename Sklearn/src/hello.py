
#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
# ithomer.net  
  
a = 1  
  
def display():  
    print("hello ithomer")  
      
    global a  
    print("a = %d" % a)  
    a = 2  
    print("a = %d" % a)  
  
if __name__ == '__main__':  
    display()  