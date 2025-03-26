from mrjob.job import MRJob
import fastavro
import sys
import re

class LogMapper(MRJob):
    def mapper(self, _, line):
        log_pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "(.*?) (.*?)" (\d+) (\d+)')
        match = log_pattern.match(line)
        if match:
            ip = match.group(1)
            yield ip, 1

if __name__ == '__main__':
    LogMapper.run()
