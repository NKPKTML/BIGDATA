from mrjob.job import MRJob
import fastavro
import sys

class AvroReducer(MRJob):
    def reducer(self, key, values):
        schema = {
            "type": "record",
            "name": "Result",
            "fields": [
                {"name": "ip", "type": "string"},
                {"name": "count", "type": "int"}
            ]
        }
        records = [{"ip": key, "count": sum(values)}]

        # Xuất kết quả dưới dạng Avro
        with open("output.avro", "wb") as f:
            fastavro.writer(f, schema, records)

if __name__ == '__main__':
    AvroReducer.run()
