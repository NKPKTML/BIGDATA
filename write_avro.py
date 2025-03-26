# import avro.schema
# import avro.datafile
# import avro.io
# import json
#
# # Đọc schema từ file user.avsc
# schema_path = "C:\\hadoop\\hadoop-2.6.0\\avro_example\\user.avsc"
# with open(schema_path, "r") as f:
#     schema = avro.schema.parse(f.read())
#
# # Dữ liệu cần ghi vào file Avro
# users = [
#     {"name": "Alice", "age": 25},
#     {"name": "Bob", "age": 30}
# ]
#
# # Ghi dữ liệu vào file Avro
# avro_file_path = "C:\\hadoop\\hadoop-2.6.0\\avro_example\\users.avro"
# with open(avro_file_path, "wb") as f:
#     writer = avro.datafile.DataFileWriter(f, avro.io.DatumWriter(), schema)
#     for user in users:
#         writer.append(user)
#     writer.close()
#
# print(f"Đã ghi dữ liệu vào {avro_file_path}")
