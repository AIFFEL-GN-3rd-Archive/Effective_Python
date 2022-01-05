class queue():
    
    def __init__(self):
        self.queue_list = []

    def push(self,x):
        self.queue_list.append(x)
        return self.queue_list
    
    def pop(self):
        if len(self.queue_list) == 1: 
            # 일단 예외처리 하긴 했는데, 
            # 어케해야 깔끔할까요
            # 이거 안하면 리스트 길이 1일때 
            # dequeue하고 빈 리스트가 출력되버림..
            return -1

        elif self.empty() == 0:
            self.queue_list.pop(0)
            return self.queue_list
        else:
            return -1
            

    def size(self):
        return len(self.queue_list)

    def empty(self):
        if len(self.queue_list) > 0:
            return 0
        else:
            return 1
    
    def front(self):
        return(self.queue_list[0])

    def back(self):
        return(self.queue_list[-1])
    
#확인구문
list_1 = queue()

print("queue empty? (1 means empty) : ",list_1.empty())
print("push 1 : ", list_1.push(1))
print("push 2 : ", list_1.push(2))
print("push 3 : ", list_1.push(3))
print("push 4 : ", list_1.push(4))
print("queue empty? (1 means empty) : ",list_1.empty())
print("size? : ",list_1.size())
print("front element? : ",list_1.front())
print("back element? : ",list_1.back())
print("dequeue : ",list_1.pop())
print("dequeue : ",list_1.pop())
print("dequeue : ",list_1.pop())
print("dequeue : ",list_1.pop())
print("dequeue : ",list_1.pop())



 



        
