from metaflow import FlowSpec, step


class Assignment2(FlowSpec):
    """A flow that implements a simple branch loging system."""

    @step
    def start(self):
        """Initialize artifact with numerical variable."""
        self.variable = 3
        print("Initial value:", self.variable)
        self.next(self.branch1, self.branch2)

    @step
    def branch1(self):
        """Branch adding a constant value to the artifact."""
        self.variable += 2
        self.next(self.join)


    @step
    def branch2(self):
        """Multiply artifact by a constant value."""
        self.variable *= 3
        self.next(self.join)

    @step
    def join(self, inputs):
        """Join the two branches."""
        self.merge_artifacts(inputs, exclude=["variable"])

        print("Branch 1 value:", inputs.branch1.variable)
        print("Branch 2 value:", inputs.branch2.variable)

        self.final_value = sum(i.variable for i in inputs)
        self.next(self.end)

    @step
    def end(self):
        """This step sums the values from both branches."""  # noqa: D401, D404
        print("Final value:", self.final_value)

if __name__ == "__main__":
    Assignment2()
