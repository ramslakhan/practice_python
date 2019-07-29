import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

patterns = '*'
ignore_patterns = ''
ignore_directories = False
case_sensitive = True
my_event_handler = PatternMatchingEventHandler(patterns,ignore_patterns,ignore_directories,case_sensitive)


# def on_created(event):
#     print(event,'has been created')

# def on_modified(event):
#      print(event.src_path ,'has been modified')
#      #print(type(event.src_path))
#      Open_file=open(event.src_path ,'r')
#      print(Open_file.read())



#
# def on_deleted(event):
#     print(event,'has been deleted')
#
# def on_moved(event):
#     print(event,'has been moved')


#my_event_handler.on_created = on_created()
my_event_handler.on_modified = Practice.FilePoller.FilePoller.on_modified

#my_event_handler.on_deleted = on_deleted
#my_event_handler.on_moved = on_moved


path = 'F:/Python/TextFiles/'
go_recursively=True
Obj_Observer = Observer()

Obj_Observer.schedule(my_event_handler,path,recursive=go_recursively)

Obj_Observer.start()

try:
    while True:
        #print('Sleep starts')
        time.sleep(10)
        #print('Sleep ends')
except KeyboardInterrupt:
    Obj_Observer.stop()
    Obj_Observer.join()
