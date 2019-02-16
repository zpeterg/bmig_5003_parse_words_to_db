from getFile import getFile

class dealArgs:
    def __init__(self, args):
        self.start = ''
        self.stop = ''
        self.finish = ''
        self.format = False
        self.output = ''
        self.stats = False
        self.csv = False

        for a in args:
            a = a.split('=')
            if a[0] == '--input':
                # If one input go ahead with that
                self.files = [a[1]]
            elif a[0] == '--inputs':
                # If multiple inputs, go ahead and get them
                self.files = getFile(a[1], lambda x: x.strip())
            elif a[0] == '--start':
                self.start = a[1]
            elif a[0] == '--stop':
                self.stop = a[1]
            elif a[0] == '--finish':
                self.finish = a[1]
            elif a[0] == '--output':
                self.output = a[1]

        # throw error if no input files supplied
        if not hasattr(self, 'files') or len(self.files) <= 0:
            raise ValueError('You must supply a file with --input or a list of space-separated files with --inputs')

        if '-s' in args:
            self.stats = True
        elif '-f' in args:
            self.format = True

        if '-c' in args:
            self.csv = True

    # FILE
    @property
    def files(self):
        return self.__files

    @files.setter
    def files(self, files):
        if files == '':
            raise ValueError('You must supply files')

        self.__files = files

    # OUTPUT
    @property
    def output(self):
        # append correct ending if its not there already
        if self.csv and self.__output and self.__output[-4:] != '.csv':
            return self.__output + '.csv'
        if not self.csv and self.__output and self.__output[-5:] != '.json':
            return self.__output + '.json'
        return self.__output

    @output.setter
    def output(self, output):
        self.__output = output

    # STATS
    @property
    def stats(self):
        return self.__stats

    @stats.setter
    def stats(self, stats):
        if not isinstance(stats, bool):
            stats = False

        # if printing stats, do not format
        if stats:
            self.__format = False

        self.__stats = stats

    # FORMAT
    @property
    def format(self):
        return self.__format

    @format.setter
    def format(self, this_format):
        if not isinstance(this_format, bool):
            this_format = False

        self.__format = this_format

    # CSV
    @property
    def csv(self):
        return self.__csv

    @csv.setter
    def csv(self, csv):
        if not isinstance(csv, bool):
            csv = False
        if csv:
            self.__format = False
        self.__csv = csv

    def to_object(self):
        return {
            "files": self.files,
            "start": self.start,
            "stop": self.stop,
            "finish": self.finish,
            "format": self.format,
            "output": self.output,
            "stats": self.stats,
            "csv": self.csv,
        }


def cleanWord(word):
    word = word.lower()
    word = word.replace('\n', '')
    return word.strip("~`!@#$%^&*()_-+={[}]|\\:;\"' <,>.?/")
