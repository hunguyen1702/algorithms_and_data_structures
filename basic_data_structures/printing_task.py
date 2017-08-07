from queue import Queue
import random


class Printer(object):

    def __init__(self, ppm):
        self.pagerate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task != None:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.pagerate


class Task(object):

    def __init__(self, current_time):
        self.timestamp = current_time
        self.pages = random.randrange(1, 21)

    def get_timestamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp


def is_newtask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    return False


def simulation(time_range, page_per_min):
    lab_printer = Printer(page_per_min)
    print_queue = Queue()
    waiting_times = []

    for timestamp in range(time_range):

        if is_newtask():
            task = Task(timestamp)
            print_queue.enqueue(task)

        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(timestamp))
            lab_printer.start_next(next_task)

        lab_printer.tick()
    # print waiting_times
    average_time = float(sum(waiting_times)) / float(len(waiting_times))
    print "Average wait %6.2f secs %d tasks remaining." % (average_time, print_queue.size())


for i in range(10):
    simulation(3600, 5)

