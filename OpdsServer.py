from xml.dom.minidom import Document
from flask import Flask
from OpdsCore import FeedDoc, Link, OpdsProtocol
from Protocols import LocalOpdsProtocol


__author__ = 'lei'

app = Flask(__name__)


@app.route("/")
def helo():
    f = FeedDoc(Document())

    f.createEntry("halo,OPds", "2014-12-11T07:10:23Z", "1234567890", "This is halo Opds Describe...",
                  {Link("http://www.baidu.com", "xxx", "aaa",
                        "application/atom+xml;profile=opds-catalog;kind=acquisition"),
                   Link("http://163.com", "mm", "mm", "application/atom+xml;profile=opds-catalog;kind=acquisition")})

    return f.toString() + "\n"


@app.route('/list/<path:path>')
def listbooks(path):
    feed = FeedDoc(Document())

    return getOpdsProtocol().listBooks(feed, path)

@app.route('/download/<path:path>')
def download(path):
    """
    download book
    """
    return "fileContent: " + path


@app.route('/show/<path:path>')
def showhtml(path):
    return "show file:" + path


def getOpdsProtocol():
    return LocalOpdsProtocol()


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
