import avro.datafile
import avro.io

# Đọc dữ liệu từ file Avro
avro_file_path = "C:\\hadoop\\hadoop-2.6.0\\avro_example\\users.avro"

with open(avro_file_path, "rb") as f:
    reader = avro.datafile.DataFileReader(f, avro.io.DatumReader())
    for record in reader:
        print(record)
    reader.close()
