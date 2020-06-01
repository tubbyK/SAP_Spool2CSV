import re

class Spool_Content_Util():
    def __init__(self, file):
        self.file = file
        self.content = None

    def process_content(self):
        self.content = self.read_content()
        self.content = self.remove_separator_lines()
        self.content = self.remove_non_content()
        self.content = self.remove_duplicates()
        result = []
        result = [self.extract_values(line) for line in self.content]
        self.file, self.content = None, None
        return result

    def read_content(self, lines_to_read=None):
        try:
            with open(self.file, 'r', encoding='utf-8') as f:
                content = f.readlines()
        except:
            with open(self.file, 'r', encoding='latin-1') as f:
                content = f.readlines()
        if lines_to_read is None: lines_to_read = len(content)
        return content[:lines_to_read]

    def remove_separator_lines(self):
        result = []
        result = [line for line in self.content if self.is_not_separator_line(line)]
        return result

    def is_not_separator_line(self, line):
        keep = True if len(set(line.strip())) > 2 else False
        return keep

    def remove_non_content(self):
        result = []
        result = [line[:-1] for line in self.content if self.is_content_line(line)]
        return result

    def is_content_line(self, line, delimiter=None):
        if delimiter is None: delimiter = '|'
        keep = True if line[0] == delimiter else False
        return keep

    def remove_duplicates(self):
        new_set = self.content.copy()
        new_set = sorted(set(new_set), key=lambda x: new_set.index(x))
        new_set = list(new_set)
        return new_set

    def extract_values(self, line, delimiter=None):
        if delimiter is None: delimiter = '|'
        tokens = [',', '"']
        for token in tokens: line = re.sub(token, '', line)
        split_line = line[1:-1].split(delimiter)
        split_line = [splitted_line.strip() for splitted_line in split_line]
        return ','.join(split_line) + '\n'