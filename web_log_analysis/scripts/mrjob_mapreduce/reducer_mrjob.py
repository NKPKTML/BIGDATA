from mrjob.job import MRJob
import fastavro
import sys

class LogReducer(MRJob):
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

        with open("data/output.avro", "wb") as out_file:
            fastavro.writer(out_file, schema, records)

if __name__ == '__main__':
    LogReducer.run()
