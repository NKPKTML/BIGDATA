
========================== folder tree: 
folder tree: (phải làm theo đúng cấu trúc thư mục project của maven thì mới build và chạy dc)


hadoop-web-log-analysis/
│── src/
│   ├── main/java/com/example/weblog/
│   │   						├── mapper/
│   │   						│   ├── MethodCounterMapper.java
│   │   						│   ├── StatusCounterMapper.java
│   │   						│   ├── SizeAvgMapper.java
│   │   						├── reducer/
│   │   						│   ├── MethodCounterReducer.java
│   │   						│   ├── StatusCounterReducer.java
│   │   						│   ├── SizeAvgReducer.java
│   │   						├── driver/
│   │   						│   ├── WebLogDriver.java
│   │   						├── model/
│   │   						│   ├── WebLog.java  (Generated từ Avro schema)
│── resources/
│   ├── weblog.avsc   (Avro Schema)
│── input/
│   ├── access.avro  (Dữ liệu Avro đầu vào)
│── pom.xml (Dùng Maven để quản lý dependencies)
│── README.md (Hướng dẫn chạy project)


==================================================== setup main project
LINK CHATGPT TRAO ĐỔI CÁC LỖI VÀ HƯỚNG DẪN CHI TIẾT: 
https://chatgpt.com/share/67ebf2f3-40b0-800e-92a3-3c434f5b6e48



1.1. Tải Maven
Truy cập trang chủ Apache Maven:
🔗 https://maven.apache.org/download.cgi

Tải phiên bản Maven 3.8.x (khuyến nghị dùng apache-maven-3.8.8-bin.zip).

1.2. Giải nén và thiết lập biến môi trường
Giải nén file apache-maven-3.x.x-bin.zip vào một thư mục: C:\apache-maven-3.8.8

1.3: set biến môi trường:
MAVEN_HOME
C:\apache-maven-3.8.8

path - edit - new: %MAVEN_HOME%\bin

- check maven: mvn -version


------------------------------------------
2. Cài đặt Apache Avro (bước này k cần thiết vì sẽ tải và sử dụng avro trong maven luôn)
2.1. Tải Avro
Tải Avro Tools từ Apache:
🔗 https://www.apache.org/dyn/closer.cgi/avro/stable/java/

https://avro.apache.org/blog/releases/

https://repo1.maven.org/maven2/org/apache/avro/avro-tools/1.11.0/
Tải file avro-tools-1.11.0.jar.
2.2. Chuyển Avro Schema thành Java Class 
Sau khi tải về, mở terminal và chạy lệnh:
java -jar avro-tools-1.11.0.jar compile schema resources/weblog.avsc src/model/
Lệnh này sẽ tạo file WebLog.java trong thư mục src/model/.
------------------------------------------


- Kiểm tra Avro Schema
java -jar avro-tools-1.11.0.jar tojson input/access.avro
Nếu hiển thị dữ liệu JSON, tức là file Avro hợp lệ.

- Tải các thư viện cần thiết cho maven
mvn clean install

- tạo file WebLog.java: 
mvn generate-sources

- build project: 
mvn clean package


------------------------------------------
- các câu lệnh có thể cần: thêm, xóa file trên hdfs

hdfs dfs -rm -r /user/Nightzone0/output/method_count
hdfs dfs -rm -r /user/Nightzone0/input/access.avro

hdfs dfs -mkdir -p /user/Nightzone0/input
hdfs dfs -put input/access.avro /user/Nightzone0/input/

hdfs dfs -ls /user/Nightzone0/input/
------------------------------------------


chạy project bằng hadoop:
hadoop jar target/web-log-analysis-1.0.jar com.example.weblog.driver.WebLogDriver

- nếu gặp lỗi: Exception in thread "main" java.io.IOException: Mkdirs failed to create C:\somepath\META-INF\license
thì chạy: 
jar -xf target\web-log-analysis-1.0.jar
del META-INF\LICENSE
del LICENSE
jar -cf target\web-log-analysis-1.0.jar .

chạy lại và show output:
hdfs dfs -cat /user/Nightzone0/output/method_count/part-r-00000


- setup tương tự và chạy full 3 job:
hadoop jar target/web-log-analysis-1.0.jar com.example.weblog.driver.WebLogDriver hdfs://localhost:9000/user/Nightzone0/input/access.avro hdfs://localhost:9000/user/Nightzone0/output/method_count hdfs://localhost:9000/user/Nightzone0/output/status_count hdfs://localhost:9000/user/Nightzone0/output/size_avg

hdfs dfs -cat /user/Nightzone0/output/method_count/part-r-00000
hdfs dfs -cat /user/Nightzone0/output/status_count/part-r-00000
hdfs dfs -cat /user/Nightzone0/output/size_avg/part-r-00000



============================================================================== word count example:

- SHOW FULL HADOOP CLASSPATH
hadoop classpath


- SET PATH CHO HADOOP_CLASSPATH
set HADOOP_CLASSPATH=C:\hadoop\hadoop-3.3.0\etc\hadoop;C:\hadoop\hadoop-3.3.0\share\hadoop\common\*;C:\hadoop\hadoop-3.3.0\share\hadoop\common\lib\*;C:\hadoop\hadoop-3.3.0\share\hadoop\hdfs\*;C:\hadoop\hadoop-3.3.0\share\hadoop\hdfs\lib\*;C:\hadoop\hadoop-3.3.0\share\hadoop\yarn\*;C:\hadoop\hadoop-3.3.0\share\hadoop\yarn\lib\*;C:\hadoop\hadoop-3.3.0\share\hadoop\mapreduce\*


- BUILD CÁC FILE JAVA THÀNH CLASS
javac -classpath "%HADOOP_CLASSPATH%" -d build src/*.java


- Tạo file JAR
jar -cvf wordcount.jar -C build/ .


- Chạy chương trình trên Hadoop

hadoop fs -mkdir /wordcount
hadoop fs -mkdir /wordcount/input
hadoop fs -put input.txt /wordcount/input/

hadoop jar wordcount.jar WordCount /wordcount/input /wordcount/output


hadoop-web-log-analysis/
│── src/
│   ├── main/java/com/example/weblog/
│   │   						├── mapper/
│   │   						│   ├── MethodCounterMapper.java
│   │   						│   ├── StatusCounterMapper.java
│   │   						│   ├── SizeAvgMapper.java
│   │   						├── reducer/
│   │   						│   ├── MethodCounterReducer.java
│   │   						│   ├── StatusCounterReducer.java
│   │   						│   ├── SizeAvgReducer.java
│   │   						├── driver/
│   │   						│   ├── WebLogDriver.java
│   │   						├── model/
│   │   						│   ├── WebLog.java  (Generated từ Avro schema)
│   │   						├── util/
│   │   						│   ├── AvroUtils.java (Đọc và ghi file Avro)
│── resources/
│   ├── weblog.avsc   (Avro Schema)
│── input/
│   ├── access.avro  (Dữ liệu Avro đầu vào)
│── output/
│   ├── method_count/
│   ├── status_count/
│   ├── size_avg/
│── lib/   (Chứa các thư viện cần thiết như Hadoop, Avro, etc.)
│── pom.xml (Dùng Maven để quản lý dependencies)
│── README.md (Hướng dẫn chạy project)
