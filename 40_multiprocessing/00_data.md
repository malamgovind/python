Multiprocessing એ એવી Programming Technique છે જેમાં એક જ Program માટે એક કરતાં વધુ Processes બનાવવામાં આવે છે જેથી ઘણા Tasks એકસાથે (Parallel) Execute થઈ શકે.

દરેક Process સંપૂર્ણપણે Independent હોય છે અને તેની પોતાની Memory, Address Space, Resources અને Python Interpreter Instance હોય છે.

Multithreading માં Threads Memory Share કરે છે, જ્યારે Multiprocessing માં દરેક Process ની Memory અલગ હોય છે.

Multiprocessing નો મુખ્ય હેતુ CPU ના Multiple Cores નો સંપૂર્ણ ઉપયોગ કરીને Performance વધારવાનો છે.

Python Program
        │
        ▼
 Main Process
        │
 ┌──────┼───────────┐
 ▼      ▼           ▼
Process1 Process2 Process3
 │        │          │
 ▼        ▼          ▼
Own      Own        Own
Stack    Stack      Stack
 │        │          │
 ▼        ▼          ▼
Own      Own        Own
Heap     Heap       Heap
 │        │          │
 ▼        ▼          ▼
Independent Memory

| Property       | Description                    |
| -------------- | ------------------------------ |
| Execution Unit | Process                        |
| Parent         | Operating System               |
| Memory         | Separate                       |
| Heap           | Separate                       |
| Stack          | Separate                       |
| GIL            | અસર નથી                        |
| Parallelism    | True Parallel                  |
| Communication  | IPC દ્વારા                     |
| Isolation      | High                           |
| Creation Cost  | High                           |
| Performance    | CPU Intensive Tasks માટે ઉત્તમ |

** class **

| Class   | Use                   |
| ------- | --------------------- |
| Process | Create Process        |
| Pool    | Process Pool          |
| Queue   | Share Data            |
| Pipe    | Process Communication |
| Value   | Shared Value          |

** --- methods --- **

| Method  | Use                    |
| ------- | ---------------------- |
| start() | Start Process          |
| join()  | Wait Process           |
| map()   | Execute Multiple Tasks |
| put()   | Insert Queue Data      |
| get()   | Read Queue Data        |
| send()  | Send Pipe Data         |
| recv()  | Receive Pipe Data      |
