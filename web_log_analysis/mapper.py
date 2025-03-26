from mrjob.job import MRJob
import fastavro
import sys

class AvroMapper(MRJob):
    def mapper(self, _, line):
        # Đọc dữ liệu Avro từ file HDFS
        with open(sys.stdin.fileno(), "rb") as f:
            reader = fastavro.reader(f)
            for record in reader:
                yield record["ip"], 1  # Trả về IP và giá trị 1

if __name__ == '__main__':
    AvroMapper.run()
