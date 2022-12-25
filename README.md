# todocli
A simple todo list manager in command line, coming from this excellent [tutorial](https://realpython.com/python-typer-cli/) on [RealPython](https://realpython.com/).

## Usage

### Getting help

All the commands are explained with the help command:

```
$ python -m todocli --help

Usage: todocli [OPTIONS] COMMAND [ARGS]...                                     
                                                                                
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --version             -v        Show the application's version and exit.     │
│ --install-completion            Install completion for the current shell.    │
│ --show-completion               Show completion for the current shell, to    │
│                                 copy it or customize the installation.       │
│ --help                          Show this message and exit.                  │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────╮
│ add         Add a new to-do with a DESCRIPTION.                              │
│ clear       Remove all to-dos.                                               │
│ complete    Complete a to-do by setting it as done using its TODO_ID         │
│ init        Initialize the to-do database.                                   │
│ list        List all to-dos.                                                 │
│ remove      Remove a to-do using its TODO_ID                                 │
╰──────────────────────────────────────────────────────────────────────────────│
```

If you want explanation of a single command, simply type `python -m todocli COMMAND --help`. Example with the `add` command:

```
$ python -m todocli add --help
                                                                                                
 Usage: todocli add [OPTIONS] DESCRIPTION...                                                    
                                                                                                
 Add a new to-do with a DESCRIPTION.                                                            
                                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────╮
│ *    description      DESCRIPTION...  [default: None] [required]                             │
╰──────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────────────╮
│ --priority  -p      INTEGER RANGE  [default: 2]                                              │
│ --help                             Show this message and exit.                               │
╰──────────────────────────────────────────────────────────────────────────────────────────────╯
```



### Quick example

Start with initializing a to-do database :

```
$ python -m todocli init  
```

You will be asked to precise the location of this database (or you can just accept the proposed default location):

```
to-do database location? [/Users/yourname/.yourname_todo.json]: 
The to-do database is /Users/yourname/.yourname_todo.json
```

You can then add to-dos with the command `add`:
```
$ python -m todocli add First todo
to-do: "First todo." was added with priority: 2
```

Default priority is 2, but you can chose another level from 1 to 3 with the option `--priority` or `-p`:
```
$ python -m todocli add Second todo -p 1
to-do: "Second todo." was added with priority: 1
```

Listing all those to-dos is done with the `list` command:
```
$ python -m todocli list                

to-do list:

ID.  | Priority  | Done  | Description  
----------------------------------------
1    | (2)       | False | First todo.
2    | (1)       | False | Second todo.
----------------------------------------
```

To mark a to-do as done, use the command `complete`:

```
$ python -m todocli complete 1     
To-do #1, "First todo." completed!
```

The to-do is still shown in the list, but now marked as done:
```
python -m todocli list      

to-do list:

ID.  | Priority  | Done  | Description  
----------------------------------------
1    | (2)       | True  | First todo.
2    | (1)       | False | Second todo.
----------------------------------------
```

To delete it, use the command `remove` (use the option `--force ` or `-f` to force confirmation):
```
$ python -m todocli remove -f 1  
To-do #1: "First todo." was removed.
$ python -m todocli list       

to-do list:

ID.  | Priority  | Done  | Description  
----------------------------------------
1    | (1)       | False | Second todo.
----------------------------------------
```

The command `clear` remove all to-dos (option `--force` to force confirmation):
```
$ python -m todocli clear --force
All to-dos were removed
$ python -m todocli list         
There are no tasks in the to-do list yet
```
