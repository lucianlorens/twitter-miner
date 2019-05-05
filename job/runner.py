import subprocess
import os

class SingleRunner():

    instance = None

    def __init__(self):
        if not SingleRunner.instance:
            SingleRunner.instance = SingleRunner.__SingleRunner()

    def __getattr__(self, name):
        return getattr(self.instance, name)

    class __SingleRunner:

        process = None

        abs_path = os.path.dirname(os.path.realpath(__file__))

        def __init__(self):
            pass

        def run_job(self):
            if (self.check_process_running() is False):
                self.process = subprocess.Popen(['python', self.abs_path + '/job.py'])
                return {"status": "New job created", "pid": self.process.pid}
            else:
                return {"status": "Job already running", "pid": self.process.pid}

        def status(self):
            if (self.check_process_running() is True):
                return {"status": "Job running", "pid": self.process.pid}
            else:
                return {"status": "No job running", "pid": None}

        def stop_job(self):
            if (self.check_process_running() is False):
                return {"status": "No job running", "pid": None}
            else:
                self.process.terminate()
                return {"status": "Job terminated", "pid": self.process.pid}

        def check_process_running(self):
            if self.process is None:
                return False
            elif self.process.poll() is not None:
                return False
            else:
                return True