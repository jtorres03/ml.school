from metaflow import FlowSpec, step


class Assignment1(FlowSpec):
    """A flow that demonstrates the use of Metaflow for a simple assignment."""

    @step
    def start(self):
        """Initialize the variable."""
        self.values = []
        self.variable = 1
        self.values.append(self.variable)
        self.next(self.increment)

    @step
    def increment(self):
        """Increment the value of the variable and append each new value to the list."""
        print("Incrementing the variable by 2")
        self.variable += 2
        self.values.append(self.variable)
        self.next(self.multiply)

    @step
    def multiply(self):
        """Multiply the variable by 3 and append the new value to the list."""
        print("Multiplying the variable by 3")
        self.variable *= 3
        self.values.append(self.variable)
        self.next(self.divide)

    @step
    def divide(self):
        """Divide the variable by 2 and append the new value to the list."""
        print("Dividing the variable by 2")
        self.variable /= 2
        self.values.append(self.variable)
        self.next(self.end)

    @step
    def end(self):
        """Print the final values list."""
        print("Sum value of the variable:", sum(self.values))
        print("Average value of the variable:", sum(self.values) / len(self.values))
        print("All values:", self.values)

if __name__ == "__main__":
    Assignment1()
