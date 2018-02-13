import os, re

#-*-coding=utf-8 -*-

class Test:
    def __init__(self):
        self.test_base = os.path.dirname(os.path.dirname(__file__))
        self.test_dir = os.path.join(self.test_base, 'test')
        self.test_list = os.listdir(self.test_dir)
        print(self.test_list)
        self.pattern = re.compile(r'(__init__.py|.*.pyc)')

        if not os.path.exists(os.path.join(self.test_base,"log.txt")):
            f = open(os.path.join(self.test_base,"log.txt"),'a')
        else:
            f = open(os.path.join(self.test_base,"log.txt"),'w')
            f.flush()
        f.close()

    def run_test(self):
        for py_file in self.test_list:
            match = self.pattern.match(py_file)
            if not match:
                os.system('python %s 1>>%s 2>&1' %(os.path.join(self.test_dir,py_file),os.path.join(self.test_base,"log.txt")))

if __name__ == "__main__":
    test = Test()
    test.run_test()