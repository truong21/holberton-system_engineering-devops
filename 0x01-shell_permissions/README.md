# Shell and Permissions

1. 0-iam_betty
   - changes userID to betty
2. 1-who_am_I
   - prints the effective userid of the current user
3. 2-groups
   - prints all the groups the current user is part of
4. 3-new_owner
   - changes the owner of the file `hello` to the user `betty`
5. 4-empty
   - creates an empty file called hello
6. 5-excute
   - adds execute permission to the owner of the file `hello`
7. 6-multiple_permissions
   - adds execute permission to the owner and the group owner, and read permission to other users, ot the file `hello`
8. 7-everybody
   - adds execution permission to the owner, the group owner, and the other users, to the file `hello`
9. 8-James_Bond
   - sets the permission to the file `hello` as follows:
     - Owner: no permission at all
     - Group: no permission at all
     - Other users: all the permissions
10. 9-John_Doe
    - sets the mode of the file `hello` to this
11. 10-mirror_permissions
    - sets the mode of the file `hello` the same a `olleh` mode
12. 11-directories_permissions
    - adds execute permission to all subdirectories of the current directory for the owner, the group
      owner, and all other users
13. 12-directory_permissions
    - creates a directory called dir_holberton with permissions 751
14. 13-change group
    - changes group owner to holberton and the file hello
15. 14-change_owner_and_group
    - change owner to betty and group owner to holberton for all files and directories
16. 15-symbolic_link_permissions
    - changes owner and group owner of the file `_hello` to `betty` and `holberton`
17. 16-if_only
    - changes the owner of the file hello to betty only if it is owned by the user guillaume
