from setup import topic

consumer = topic.get_simple_consumer()
for m in consumer:
    if m is not None:
        print(str(m.value))
