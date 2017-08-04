
# tstream : 标准C++流的TCP实现

## 客户端

```cpp
#include <tstream.h>

tstream ts("127.0.0.1", 2048);

if (ts) {
    string line;
    ts >> line;           // 接收数据
    ts << line << endl;   // 发送数据
} else {
    // 连接失败，处理错误
}
```

## 服务端

```cpp
#include <tstream.h>

tstream::server server("127.0.0.1", 2048);

auto ts = server.accept();
if (ts) {
    string line;
    ts << "Hello" << endl;
    ts >> line;
    // ...
}
```

## Features

* 跨平台: Windows/Linux/Mac
* 小巧: 只有一个头文件
* 简洁: 采用了部分C++11特性，支持移动语义
