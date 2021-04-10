from veriff.dto.context import Context
from veriff.handler.abstract_handler import AbstractHandler


class ResultGenerateHandler(AbstractHandler):
    def handle(self, context: Context):
        print("ResultGenerateHandler start")
        print("!!!! result !!!")
        print(context.result)
        print("ResultGenerateHandler done")