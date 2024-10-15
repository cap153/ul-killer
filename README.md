# ul-killer
一个基于DrissionPage的网购秒杀python脚本，无需添加购物车

# 安装环境

1. 自行安装谷歌浏览器，如果已安装谷歌浏览器还是运行不了，又或者想使用edge等其他谷歌内核浏览器，可以手动设置浏览器路径，详见[https://www.drissionpage.cn/get_start/before_start](https://www.drissionpage.cn/get_start/before_start)
2. 自行安装最新版python
3. 使用 pip 安装 DrissionPage：cmd运行`pip install DrissionPage`，如果安装失败，可以尝试换国内的源试试，对应命令如下`pip install -i  http://mirrors.aliyun.com/pypi/simple/ DrissionPage --trusted-host mirrors.aliyun.com --user`

# 使用

1. 修改变量`killer_time`为你的秒杀时间
2. 根据实际情况修改变量`buy`为商品购买按钮的文字信息，可以是立即购买、领券购买等等
3. 直接用python运行即可(需要提前设置好默认的发货地址信息)
4. **打开购物车页面后如果没有登陆需要手动登陆**
5. 在秒杀时间到达之前选择好商品型号

```python
python gd_killer.py
```

【【python抢购脚本】基于DrissionPage且无需添加购物车】 https://www.bilibili.com/video/BV1SWmFYVEmK/?share_source=copy_web&vd_source=d34abe3786a6b85ecc07875a85795885
