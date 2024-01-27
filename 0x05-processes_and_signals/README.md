# Processes and signals (Unix)

*Processes are identification numbers* that are automatically assigned to a process/each process when its created in unix like operating system.

A process is an executing instance of a program and each processes created has a *unique PID thats a non-negative integer.*

No two processes has the same PID number on any session when created but the init process has the same process on any session and its value is always 1.

This is possible as its the first process on the system and its the predecessor to every created processes.

When a process ends, the PID number is not immediately assigned to another process so as to prevent possible errors and thats why PID numbers are sometimes large when created.

The default maximum number of PIDs is 32,767 and its the number of processes that can exist simultaneously on a system, although, it can be increased to about 4 million and its also dependent on your RAM.

This can be checked by running:
`cat /proc/sys/kernel/pid_max`

## Commands to check processes

The following commands can be used to check the processes associated with running application or programs on your linux system;

1. *ps* (shows all process currently running)
2. *pstree* (shows the Parent & child process names and PIDs in a tree diagram)
3. *top* (used to show PIDs of running process and some information about them)
4. *kill* (used to terminate misbehaving programs)

Information about all current processes is stored in the /proc directory filesystem and the filesystem consists of kerenel data that changes in real time.

`ls /proc | less` (can be used to extract information related to processes).

The /proc directory contains a lot of vital information which would be necessary to use the root `su` because of the security of the directory.

Information about the 1 (init process) status file in the `/proc` can be know by running the command:

`cat /proc/1/status`

## How To Stop/Kill/Terminate a proess

The kill command is used on Linux and other Unix-like operating systems to terminate processes without having to log out or reboot (i.e., restart) the computer.

The syntax for kill is

`kill [signal or option] PID(s)`

The only argument (i.e., input) that is required is a PID, and as many PIDs as desired can be used in a single command.

example:
kill 485

*kill command* has a misleading name because it does not actually kill processes. Rather, it sends signals to them. The signals are what the kill command actually terminates and the most common/used kill signal is the the signal 9.

The *signal 9 is called SIGKILL* and its wideley used if the *SIGTERM (signal 15)* fails to actually to dectect any signal.

> example
`kill -9 485`

*SIGTERM would only fail* when the process is at the point of making a system call which is a request to the kernel and the process would die only if it has returned from the system call.

There are more than 60 Signal calls but the most widely used kill signal by users is 9 and its full list is found in the /usr/include/linux/signal.h and viewed by doing `kill -l`.

### Other ways of terminating a program

To terminate a process you can use the `pkill -f NAME_OF_FILE` where -f is the the flag to specify the file name.
To find all processes in another terminal use the `ps -ax` or the `pgrep -f NAME_OF_FILE` to find the specific file process that you want to terminate while in another terminal.

You can also use the trap keyword in bash to prevent a script from terminating while being executed. The syntax is as follows;
`trap "COMMAND/ACTION" SIGNAL`
where *signal* is the type of SIG you want to prevent/block eg *SIGTERM*

## How to check failing processes

Things to note that a program is failing are:

1. The app appears to freeze while running
2. Application can't shutdown/ terminate normally.

The best thing to do in this situation when an application or a process fails is to;
1. run `ps -aux | less` to know all the available process and information on them
2. run `pstree | less` as to know the parent process and childprocesses of the respected program you wish to terminate.
3. run the `kill -9` on the desired process to terminate the frozen program

*Note:*
some times even the strongest signal wouldnt be able to terminate a program and its best to just reboot the system when it gets to that point.