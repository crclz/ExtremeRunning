# ExtremeRunning

## 视频教程
TODO
链接
时长：

## 前提条件

1. 安装[夜神模拟器](https://www.yeshen.com/)，因为需要夜神模拟器提供的设置经纬度的功能
2. git clone 本仓库，或下载本仓库
3. 安装python。推荐 python3.8，最低要求 python3.6
4. 安装依赖: `pip install -r requirements.txt`. 速度慢的解决方案：[pip更换镜像加速](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)


## 准备

1. 启动模拟器，安装跑步软件。（“悦动圈”我已经测试过了）
2. 找到模拟器安装目录`xxx/Nox`，修改**nox-path.txt**的内容，例如`C:\yeshen\Nox`
3. 通过[坐标拾取系统](https://api.map.baidu.com/lbsapi/getpoint/index.html)，创建路线文件（参考route-playground.txt）。
   - 路径会循环。跑到最后一个点，然后就会往第一个点跑。
   - 注意，由于本程序计算路线是使用三次样条曲线，会平滑处理路径，所以如果想要跑直角，请在转角处多拾取几个点。
   
4. 计算你想跑的速度(m/s)。例如你想跑 5min/km ，那么速度`v = 1000 / (5*60) = 3.333`

## 运行

1. 打开模拟器，打开跑步软件
2. 运行 `python main.py [跑步路径文件] [速度m/s]` 例如：`python main.py route-playground.txt 3.333`
3. 打开跑步软件，开始跑步
4. 到距离了，手动ctrl-c关闭本程序，并到模拟器手动停止跑步


## 注意事项
不使用的时候，请及时关闭悦跑圈和安卓模拟器。不然电脑可能<span class="hot">发烫</span>。

<style>
.hot {
    color: red;
    background-color: wheat;
}
</style>