# Qt获取系统信息

### 获取系统用户名

```
QString getUserName()
{
    QString name = qgetenv("USER");

    if (name.isEmpty())
        name = qgetenv("USERNAME");

    return name;
}
```

### 获取平台信息

```
QString getPlatform()
{
    return QString("%1 %2")
           .arg(QSysInfo::kernelType())
           .arg(QSysInfo::currentCpuArchitecture());
}
```

### 获取发行版

```
QString getDistribution()
{
    return QSysInfo::prettyProductName();
}
```

### 获取内核版本

```
QString getKernel()
{
    return QSysInfo::kernelVersion();
}
```

### 获取CPU型号与核数

```
void getCpuInfo(QString &cpuModel, QString &cpuCore)
{
    QFile file("/proc/cpuinfo");
    file.open(QIODevice::ReadOnly);

    QString buffer = file.readAll();
    QStringList model_line = buffer.split("\n").filter(QRegExp("^model name"));
    QStringList core_line = buffer.split("\n");

    cpuModel = model_line.first().split(":").at(1);
    cpuCore = QString::number(core_line.filter(QRegExp("^processor")).count());

    file.close();
}
```

### 获取CPU Time

```
void getCpuTime(unsigned long long &workTime, unsigned long long &totalTime)
{
    QFile file("/proc/stat");
    file.open(QIODevice::ReadOnly);

    QString buffer = file.readAll();
    QStringList list = buffer.split("\n").filter(QRegExp("^cpu "));
    QString line = list.first();
    QStringList lines = line.trimmed().split(QRegExp("\\s+"));

    unsigned long long user = lines.at(1).toLong();
    unsigned long long nice = lines.at(2).toLong();
    unsigned long long system = lines.at(3).toLong();
    unsigned long long idle = lines.at(4).toLong();
    unsigned long long iowait = lines.at(5).toLong();
    unsigned long long irq = lines.at(6).toLong();
    unsigned long long softirq = lines.at(7).toLong();
    unsigned long long steal = lines.at(8).toLong();
    //unsigned long long guest = lines.at(9).toLong();
    //unsigned long long guestnice = lines.at(10).toLong();

    workTime = user + nice + system;
    totalTime = user + nice + system + idle + iowait + irq + softirq + steal;

    file.close();
}
```

### 获取内存信息

```
void getMemoryInfo(QString &memory, float &percent)
{
    QFile file("/proc/meminfo");
    file.open(QIODevice::ReadOnly);

    QString buffer = file.readAll();
    QStringList lines = buffer.split("\n").filter(QRegExp("^MemTotal|^MemAvailable|^SwapTotal|^SwapFree"));
    QRegExp sep("\\s+");

    unsigned long long memTotal = lines.at(0).split(sep).at(1).toLong();
    unsigned long long memAvailable = lines.at(1).split(sep).at(1).toLong();
    unsigned long long swapTotal = lines.at(2).split(sep).at(1).toLong();
    unsigned long long swapFree = lines.at(3).split(sep).at(1).toLong();

    memory = QString("%1 / %2").arg(formatBytes((memTotal - memAvailable) * 1024)).arg(formatBytes(memTotal * 1024));
    percent = (memTotal - memAvailable) * 100.0 / memTotal;

    file.close();
}
```

### 获取磁盘信息

```
void getDiskInfo(QString &disk, float &percent)
{
    QProcess *process = new QProcess;
    process->start("df -Pl");
    process->waitForFinished();

    QString buffer = process->readAllStandardOutput();
    QStringList result = buffer.trimmed().split(QChar('\n'));
    long long size = 0, used = 0, free = 0;
    long long totalSize = 0, totalFree = 0;

    process->kill();
    process->close();

    for (const QString &line : result.filter(QRegExp("^/")))
    {
        QStringList slist = line.split(QRegExp("\\s+"));
        size = slist.at(1).toLong() << 10;
        used = slist.at(2).toLong() << 10;
        free = slist.at(3).toLong() << 10;

        totalSize += size;
        totalFree += free;
    }

    disk = QString("%1 / %2").arg(formatBytes(totalSize - totalFree)).arg(formatBytes(totalSize));
    percent = used * 100.0 / size;
}

```

### 获取当前网络字节数

```
void getNetworkBandWidth(unsigned long long &receiveBytes, unsigned long long &sendBytes)
{
    QFile file("/proc/net/dev");
    file.open(QIODevice::ReadOnly);

    file.readLine();
    file.readLine();

    QString buffer;
    receiveBytes = 0;
    sendBytes = 0;

    while ((buffer = file.readLine()) != nullptr)
    {
        QStringList lines = buffer.trimmed().split(QRegExp("\\s+"));

        if (lines.first() != "lo:") {
            receiveBytes += lines.at(1).toLong();
            sendBytes += lines.at(9).toLong();
        }
    }

    file.close();
}
```
