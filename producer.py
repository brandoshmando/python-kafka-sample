from setup import topic

with topic.get_sync_producer() as p:
    while True:
        message = input("Type any message:")
        p.produce(bytes(message, 'utf8'))
