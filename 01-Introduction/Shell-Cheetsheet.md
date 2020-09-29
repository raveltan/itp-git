# Shell Scripting Cheet Sheet

Below list most-used command that is applicable in Unix-like system.

## Filesystem Navigation

Navigate in the filesystem

### cd (Change Directory)

cd is used to change inside or outside of the current directory.

example:

- "cd ~" = Change to the home directory 
- "cd .." = Move one directory up.
- "cd file" = Move to the file directory

> Home directory in Unix-like system is a special directory that stores user and user app data, it acts like C:\User\{username} on Windows system.

### pwd

pwd is used to get the current directory path.

will print out a string of the current directory,
for example: "/home/ravel/Documents/"

### cat

Get the content of a file an prints it out to the console.
```bash
cat [filename]
```

## Filesystem Manipulation

Create update or delete file or directory in a filesystem.

### touch

Create an empty file in the current path.

```bash
touch [filename]
```

### mkdir 

Create an empty directory file the specified name.

```bash
mkdir [dirname]
```

### rm
Delete certain file or directory

Delete a file 
```bash
rm [filename]
```

Delete a directory

```bash
rm -r [dirname]
```

> -r here is a flag that tell rm to delete recursively

Force delete a file
```bash
rm -f [filename]
```

The flag here such as -r and -f can be chained,
for example to force delete a directory, you can run:

```bash
rm -rf [dirname]
```

### vim and nano

Vim and Nano are 2 of the most popular CLI-based text editor.

> !!! IMPORTANT: For beginner please use Nano as it's easier

To open a file, run:
```bash
nano [filename]
```
To exit and save from nano, press CTRL+X

> IF YOU EVER GOT STUCK IN A VIM EDITOR,DON'T PANIC TYPE :q! TO EXIT WITHOUT SAVING.


