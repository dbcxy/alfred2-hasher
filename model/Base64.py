import base64
import re

from model.BaseModel import BaseModel
from workflow.workflow import Item


class Base64(BaseModel):
    def __init__(self):
        self.name = u'base64'
        self.desc = u'Base64 Converter'

    def convert(self, query):
        result = []

        encode_result = base64.encodestring(query).replace('\n', '')
        result += [
            Item(
                    title=u'Base64 Encode' + ': ' + query,
                    key=self.name + u'-encode',
                    subtitle=encode_result,
                    arg=encode_result,
                    valid=True
            )
        ]

        try:
            if re.search("^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$", query):
                decode_result = base64.decodestring(query).encode('utf-8').replace('\n', '')
                if base64.encodestring(decode_result).replace('\n', '') == query:
                    result += [
                        Item(
                                title=u'Base64 Decode' + ': ' + query,
                                key=self.name + u'-decode',
                                subtitle=decode_result,
                                arg=decode_result,
                                valid=True
                        )
                    ]
        except:
            pass

        return result
