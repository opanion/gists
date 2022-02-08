class Job:
    def __init__(self, pages):
        self.pages = pages
    
    def print_page(self):
        if self.pages > 0:
            self.pages -= 1
        
    def check_complete(self):
        if self.pages == 0: 
            return True
        return False

class PrintQueue:
    def __init__(self):
        self.jobs = []

    def enqueue(self, job):
        self.jobs.insert(0, job)

    def dequeue(self):
        if self.jobs:
            return self.jobs.pop()
        else: return None

    def peek(self):
        if self.jobs:
            return self.jobs[-1]
        else: return None

    def size(self):
        return len(self.jobs)

    def is_empty(self):
        return self.items == []

class Printer:
    def __init__(self):
        self.current_job = None

    def get_job(self, print_queue):
        try:
            self.current_job = print_queue.dequeue()
        except IndexError:
            return 'No more jobs to print'

    def print_job(self, job):
        while job.pages > 0:
            job.print_page()

        if job.check_complete():
            return 'Printing Complete! ...'
        else: 
            return 'An error ocurred.'

job1 = Job(10)
job2 = Job(7)
job3 = Job(5)
queue = PrintQueue()
printer = Printer()

queue.enqueue(job1)
queue.enqueue(job2)
queue.enqueue(job3)

printer.get_job(queue)
print(printer.print_job(printer.current_job))
