from .._stack import Stack

from ._queue import Queue

from ._errors import EmptyQueueException


class StackBasedQueue[T](Queue[T]):
    def __init__(self):
        self._inbound_stack = Stack[T]()
        self._outbound_stack = Stack[T]()

    def enqueue(self, data: T):
        self._inbound_stack.push(data)

    def unqueue(self) -> T:
        self._transfer_inbound_to_outbound()

        if len(self._outbound_stack) == 0:
            raise EmptyQueueException()

        return self._outbound_stack.pop()

    @property
    def size(self) -> int:
        return len(self._inbound_stack) + len(self._outbound_stack)

    def _transfer_inbound_to_outbound(self):
        if not self._outbound_stack:
            while self._inbound_stack:
                self._outbound_stack.push(self._inbound_stack.pop())
