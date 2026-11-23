
import gc
import sys

# Function to create some objects
def create_objects():
    objects = []
    for i in range(1000):
        objects.append([i] * 100)
    return objects

# Function to display memory usage
def display_memory():
    print("Memory used by objects:", sys.getsizeof(objects), "bytes")

# Display initial memory usage
objects = []
print("Initial Memory Usage:")
display_memory()

# Create objects and display memory usage
print("\nAfter Creating Objects:")
objects = create_objects()
display_memory()

# Enable garbage collection debugging
gc.set_debug(gc.DEBUG_LEAK)

# Delete objects
del objects

# Collect garbage and display memory usage
print("\nGarbage Collection:")
collected = gc.collect()
print("Garbage collected:", collected)
print("Memory after garbage collection:", gc.get_count())

# Disable garbage collection debugging
gc.set_debug(0)

print("\nGarbage Collection Completed.")