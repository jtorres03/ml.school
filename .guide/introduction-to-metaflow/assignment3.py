from metaflow import FlowSpec, step, retry
import random

class Assignment3(FlowSpec):
    """A Metaflow flow that squares a list of numbers and sums the results."""

    @step
    def start(self):
        """Create a list of numbers."""
        self.numbers = [1, 2, 3, 4, 5]
        self.next(self.flaky_service)

    @step
    @retry(times=3)
    def flaky_service(self):
        """Simulate a flaky external service that fails 50% of the time."""
        print("Calling flaky external service...")
        if random.random() < 0.5:
            print("Flaky service failed! Retrying...")
            raise Exception("Random failure!")
        print("Flaky service succeeded.")
        self.next(self.square, foreach="numbers")

    @step
    def square(self):
        """Square the input number."""
        self.numbers = self.input or ""
        self.squared_number = self.numbers ** 2
        print(f'Squared {self.numbers} to get {self.squared_number}')  # noqa: Q000
        self.next(self.join)

    @step
    def join(self, inputs):
        """Join the results from the square step. Sum the squared numbers."""
        self.squared_numbers = [i.squared_number for i in inputs]
        self.sum_of_squares = sum(self.squared_numbers)
        self.next(self.end)

    @step
    def end(self):
        """Print the list of squared numbers."""
        print("List of squared numbers:", self.squared_numbers)
        print("Sum of squared numbers:", self.sum_of_squares)

if __name__ == "__main__":
    Assignment3()