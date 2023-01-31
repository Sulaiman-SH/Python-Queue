def create_que():
    que_init = []
    return que_init

def check_ifEmpty(QueCheckE):
    return QueCheckE == 0

def Push(PushQue, item):
    PushQue.append(item)
    return PushQue

def pop(PopQue):
    if check_ifEmpty(len(PopQue)):
        return "Empty Que"
    return PopQue.pop(0)

queue = []
queue = create_que()
print('push', Push(queue, 5))
print('push', Push(queue, 3))
print('pop', pop(queue))
print('pop', pop(queue))
print('pop', pop(queue))
