import shutil

class DocsPublisher:

    def __init__(self):
        pass

    def publish(self, dir, output_dir):
        shutil.move(dir, output_dir)