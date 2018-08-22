from multiprocessing import Process
from .. import server
import pytest


@pytest.fixture(scope="session", autouse=True)
def server_setup():
    """
    create an instance of a server, run the process forever
    """
    instance = server.create_server()

    process = Process(target=instance.serve_forever)
    process.daemon = True
    process.start()
