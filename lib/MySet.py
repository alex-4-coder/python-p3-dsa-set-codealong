class MySet:
    def __init__(self, enumerable=[]):
        """Initialize the set with unique values from the iterable."""
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True

    def has(self, value):
        """Check if the value exists in the set."""
        return value in self.dictionary

    def add(self, value):
        """Add a value to the set (if not already present)."""
        self.dictionary[value] = True
        return self

    def delete(self, value):
        """Remove a value from the set (if it exists)."""
        self.dictionary.pop(value, None)
        return self

    def size(self):
        """Return the number of elements in the set."""
        return len(self.dictionary)

    def clear(self):
        """Remove all elements from the set."""
        self.dictionary.clear()
        return self

    def __str__(self):
        """Return a readable string representation of the set."""
        return f"MySet: {{{', '.join(str(k) for k in self.dictionary)}}}"

    # ------------------ Bonus Methods ------------------
    def union(self, other_set):
        """Return a new MySet that is the union of this set and another set."""
        new_set = MySet(self.dictionary.keys())
        for value in other_set.dictionary:
            new_set.add(value)
        return new_set

    def intersection(self, other_set):
        """Return a new MySet that is the intersection of this set and another set."""
        new_set = MySet()
        for value in self.dictionary:
            if other_set.has(value):
                new_set.add(value)
        return new_set

    def difference(self, other_set):
        """Return a new MySet with elements in this set but not in the other set."""
        new_set = MySet()
        for value in self.dictionary:
            if not other_set.has(value):
                new_set.add(value)
        return new_set
