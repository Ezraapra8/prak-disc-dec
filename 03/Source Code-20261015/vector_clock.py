class VectorClock:
    def __init__(self, num_processes, process_id):
        self.clocks = [0] * num_processes  
        self.process_id = process_id       

    def increment(self):
        """Increments the local clock for the current process."""
        self.clocks[self.process_id] += 1

    def send_message(self):
        """Prepares the vector clock for sending with a message."""
        self.increment()  # Increment local clock before sending
        return list(self.clocks) 

    def receive_message(self, received_clocks):
        """Updates the vector clock upon receiving a message."""
        for i in range(len(self.clocks)):
            self.clocks[i] = max(self.clocks[i], received_clocks[i])
        self.increment()  

    def __str__(self):
        return f"P{self.process_id}: {self.clocks}"

    def happens_before(self, other_vector_clock):
        """
        Determines if this vector clock happens before another.
        A happens before B if all elements in A are less than or equal to
        the corresponding elements in B, and at least one element in A is
        strictly less than the corresponding element in B.
        """
        if self.clocks == other_vector_clock.clocks:
            return False  

        all_le = True
        any_lt = False 

        for i in range(len(self.clocks)):
            if self.clocks[i] > other_vector_clock.clocks[i]:
                return False 

            if self.clocks[i] < other_vector_clock.clocks[i]:
                any_lt = True

        return all_le and any_lt

    def is_concurrent(self, other_vector_clock):
        """
        Determines if two vector clocks are concurrent.
        Two events are concurrent if neither happens before the other.
        """
        return not (self.happens_before(other_vector_clock) or
                    other_vector_clock.happens_before(self))