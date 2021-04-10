from veriff.dto.context import Context


class AbstractHandler:
    """
        AbstractHandler provide abstract methods for  handler implementation
    """
    next = None  # Type AbstractHandler

    def set_next(self, handler):
        """
        Set next handler of the chain
        :param handler: AbstractHandler
        :return: AbstractHandler
        """
        self.next = handler
        return handler

    def handle(self, context: Context):
        """
        This method must be implemented by child
        :param context:
        :return:
        """
        raise Exception("not implemented error")
