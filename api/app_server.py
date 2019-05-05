import bjoern
import os
from app import app

host = os.environ['HOST']
port = int(os.environ['PORT'])

print("Starting Bjoern server on %s:%s" % (host, port))

bjoern.run(app, host, port)