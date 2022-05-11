# CTA200 2022

Somewhere in Norm's (username murray) home directory, there are two files named Hello_world.c and Hello_world.py (note that the H is capitalized). Find them and copy them to the assignment_1 folder you created in step 1. You can use find to help you search for them.

### Command used is 
```
find . -name "Hello_world.c" | grep "Hello_world.c"
find . -name "Hello_world.py" | grep "Hello_world.py"
```

The files are in 
```/home/murray/Papers/tmp```

Rename your version of the files Hello_world_your-last-name.c/py.

### Command used is 
```
mv Hello_world.py Hello_world_ang.py
mv Hello_world.c Hello_world_ang.c
```

Compile the C code using gcc (you will need to load a module for this). Name the executable Hello_world.x.

### Command used is 
```
gcc Hello_world_ang.c -o Hello_world.x
```

Run the C program and the Python program to see what they do.

### Command used is 
```
./Hello_world.x
```

Using vi, edit both programs so that they now print Hello, <Your Full Name> from <Language (C/Python)>.

Run the updated C and Python programs. Pipe the output of the C program to a file called output_c.txt and the output from the Python program to a file called output_python.txt.
  
### Command used is 
```
./Hello_world.x > output_c.txt
python Hello_world_ang.py > output_python.txt
```

Pipe the commands you used to do steps 1-7 to a text file by using the history command. Call the file history.txt and place it in the assignment_1 folder.
