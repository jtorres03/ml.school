import random
from metaflow import FlowSpec, step, retry
# This code demonstrates how to use the retry decorator in Metaflow
# to handle flaky external services in a flow.
# The retry decorator allows you to specify how many times a step should be retried
# in case of failure, which is useful for dealing with unreliable external systems

class RetryFlow(FlowSpec):
    """A flow with a retry decorator to handle a flaky external service."""

    @step
    def start(self):
        """Initialize the flow."""
        self.value = 0
        self.next(self.flaky_step)

    @retry(times=3)  # Retry up to 3 times if it fails
    @step
    def flaky_step(self):
        """Simulate a flaky external service with 50% failure chance."""
        if random.random() < 0.5:  # 50% chance of failure
            print("Flaky service failed!")
            raise Exception("Simulated failure")
        self.value += 1
        print(f"Flaky step succeeded, value is now {self.value}")
        self.next(self.end)

    @step
    def end(self):
        """Print the final value."""
        print(f"Final value: {self.value}")

if __name__ == "__main__":
    RetryFlow()
