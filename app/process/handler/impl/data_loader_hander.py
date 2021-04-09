from app.process.context import Context
from app.process.handler.abstract_handler import AbstractHandler


class DataLoaderHandler(AbstractHandler):
    def handle(self, context: Context):
        print("DataLoaderHandler start")
        context.data_set = [1,2,3,4,5]
        print("DataLoaderHandler done")
        self.next.handle(context)
