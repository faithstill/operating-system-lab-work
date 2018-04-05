from operator import itemgetter
process_Readylist = []
process_Runninglist = []
process_Blocked = []

def create_process():
    process_name = raw_input("please input the process name")
    process_priority = raw_input("please input the process priority")
    PCB = (process_name, process_priority)
    process_Readylist.append(PCB)

def show():
    print "Status_Ready:\n"
    Ready_num = len(process_Readylist)
    for i in range(0,Ready_num):
        print("\tProcess's name:"+process_Readylist[i][0]+"\t priority = "+process_Readylist[i][1])
    print "\nStatus_Running:\n"
    Running_num = len(process_Runninglist)
    for i in range(0,Running_num):
        print("\tProcess's name:"+ process_Runninglist[i][0]+"\t priority = "+process_Runninglist[i][1])
    print "\nStatus_Blocked:\n"
    Blocked_num = len(process_Blocked)
    for i in range(0,Blocked_num):
        print("\tProcess's name:"+ process_Blocked[i][0]+"\t priority = "+process_Blocked[i][1])

def dispatch():
    if len(process_Readylist) == 0:
        print "sorry ,we don't have process in ready"
        show()
    elif ( len(process_Runninglist) < 1) :
        process = process_Readylist.pop()
        process_Runninglist.append(process)
        show()
    elif (len(process_Runninglist) == 1):
        print "can't dispatch because there have a process in running "
        show()

def wait():
    if len(process_Runninglist) == 0:
        print "sorry, we don't have process in Running"
        show()
    if len(process_Runninglist) != 0:
        process = process_Runninglist.pop()
        process_Blocked.append(process)
        dispatch()

def timeout():
    if len(process_Runninglist) == 0:
        print "sorry ,we don't have process in Running"
        show()
    else:
        process = process_Runninglist.pop()
        process_Readylist.append(process)
        dispatch()

def occurs():
    if len(process_Blocked) == 0:
        print "sorry ,we don't have process in Blocked"
        show()
    else:
        process = process_Blocked.pop()
        process_Readylist.append(process)
        dispatch()

process_num = input("please input the num of process you want to create")
while process_num > 0:
    create_process()
    process_num = process_num - 1

process_Readylist= sorted(process_Readylist, key=itemgetter(1), reverse=True)
show()

while 1:
    select = raw_input("1.dispatch 2.wait 3.timeout 4.occurs 5.new 6.exit")

    if select == '1':
        dispatch()
    if select == '2':
        wait()
    if select == '3':
        timeout()
    if select == '4':
        occurs()
    if select == '5':
        create_process()
        process_Readylist = sorted(process_Readylist, key=itemgetter(1), reverse=True)
        show()
    if select == '6':
        exit(0)

