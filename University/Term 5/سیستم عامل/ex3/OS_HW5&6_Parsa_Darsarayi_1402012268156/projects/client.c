#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>   
void encrypt_msg(char *s) {
    for (int i = 0; s[i]; i++) {
        if (s[i] >= 'a' && s[i] <= 'z')
            s[i] = 'a' + ((s[i] - 'a' + 2) % 26);
        else if (s[i] >= 'A' && s[i] <= 'Z')
            s[i] = 'A' + ((s[i] - 'A' + 2) % 26);
    }
}

void decrypt_msg(char *s) {
    for (int i = 0; s[i]; i++) {
        if (s[i] >= 'a' && s[i] <= 'z')
            s[i] = 'a' + ((s[i] - 'a' - 2 + 26) % 26);
        else if (s[i] >= 'A' && s[i] <= 'Z')
            s[i] = 'A' + ((s[i] - 'A' - 2 + 26) % 26);
    }
}
int main() {
    int client_fd;
    struct sockaddr_in server_addr;
    char buffer[1024];

    client_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (client_fd < 0) {
        perror("socket");
        return 1;
    }

    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(5050);
    server_addr.sin_addr.s_addr = inet_addr("127.0.0.1");

    if (connect(client_fd, (struct sockaddr*)&server_addr, sizeof(server_addr)) < 0) {
        perror("connect");
        close(client_fd);
        return 1;
    }

    printf("Enter a message: ");
    if (!fgets(buffer, sizeof(buffer), stdin)) {
        fprintf(stderr, "fgets failed\n");
        close(client_fd);
        return 1;
    }
    size_t len = strlen(buffer);
    if (len > 0 && buffer[len-1] == '\n') buffer[len-1] = '\0';
    encrypt_msg(buffer);
    write(client_fd, buffer, strlen(buffer) + 1); 


    ssize_t n = read(client_fd, buffer, sizeof(buffer) - 1);
    decrypt_msg(buffer);
    if (n < 0) {
        perror("read");
        close(client_fd);
        return 1;
    }
    buffer[n] = '\0';
    printf("Server reply: %s\n", buffer);

    close(client_fd);
    return 0;
}