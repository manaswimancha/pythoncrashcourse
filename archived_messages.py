def show_messages(messages,sent_messages):
    while(True):
        if len(messages) != 0:
            print(messages[0])
            sent_messages.append(messages[0])
            messages.remove(messages[0])
        else:
            break
messages = ["hello","hi","how are you?","good afternoon"]
sent_messages = []
show_messages(messages[:],sent_messages)
print(sent_messages)
print(messages)