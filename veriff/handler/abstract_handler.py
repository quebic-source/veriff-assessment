from veriff.dto.context import Context


# Abstract Handler
class AbstractHandler:
    next = None  # Type AbstractHandler

    def set_next(self, handler):
        self.next = handler
        return handler

    def handle(self, context: Context):
        raise Exception("not implemented error")
