# Queue => first we append elements in list and then remove it in FIFO form.

queue = []
queue.append('a')
queue.append('b')
queue.append('c')
print("Initial queue")
print(queue)
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print("\nQueue after removing elements")
print(queue)


# Output:=>

# Initial queue
# ['a', 'b', 'c']

# Elements dequeued from queue
# a
# b
# c

# Queue after removing elements
# []