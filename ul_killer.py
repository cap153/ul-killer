from DrissionPage import ChromiumPage
import datetime

# 创建对象并指定端口
page = ChromiumPage(9226)

# 指定秒杀时间
kill_time = "2024-10-15 22:03:00.00000000"

# 这里填写商品链接
page.get("https://item.taobao.com/item.htm?id=535571681850&pisk=gRWjpPVoNHYPZJhV9REyOpNttHp_YNwEhctOxGHqXKpxWVIpzArD35v15U_MuIJAC_D1xGX4mdrDnivMByzULNscmdYc8xMRhQpJYgH9XAeEhlWzxyzULRNx2dab8ZS60ccJAHp9DCdveutwcAKOWCHR2UxMXqKtHusJrUHvWELve8KeXjKOWnL-eH-HDfH9M0HJjUKvBCHxOFiBfSTccuf9u-vrq-sXPAHOF3UMRiNZC3WJc-8CcUaLBTMHGeIvPAUUubUwkHBLzjxBGNORUGoEQpjAtNxdkqU6STsRH6QTRX8RXMf9NOgY0wQR1NKlZPG6R1IVtTRrXjpPv6_MyQ0jddWf2t-l5DhVmCCPnBX4yx9dtiJV6wUrgECBXg8iLeGMLfwpUAtW8uZSsffcYAlQS5L-rIKkcQr7VqCMM3xW8uZSsfAvqnt7VugAs&priceTId=2150408f17290008171965334e94e8&skuId=4614843324558&spm=a21bo.jianhua%2Fa.201876.d7.5af92a89lcO21M&utparam=%7B%22aplus_abtest%22%3A%22ece4fc8b197238c0d65ccc7b636cc294%22%7D&xxc=ad_ct")

# 用于定位购买按钮的文字根据，实际情况修改，可以是购买、立即购买、领券购买等等
buy = "立即购买"

# 用于定位提交订单的文字
commit = "提交订单"

while(True):
    # 获取当前时间
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print(now) # 打印当前时间测试
    # 判断当前时间是否到达了秒杀时间
    if(now>kill_time):
        try:
            # 点击购买按钮
            page.ele(buy).click()
            # 下单商品
            page.wait.ele_displayed(commit, timeout=60) # 等待提交订单按钮完全加载
            page.ele(commit).click()
            break
        except Exception as err:
            # 如果发生任何异常都进行捕捉，防止浏览器退出
            print("%s\n发生了错误，请手动完成后续步骤"%err+input())
    # 判断当前秒数是不是0，实现间隔一分钟刷新页面，防止掉登录
    if(datetime.datetime.now().second == 0):
        while(True):
            page.refresh() # DrissionPage的页面刷新方法，内置了wait.load_start()程序会自动等待加载结束
            try:
                # 等待购买加载
                page.wait.ele_displayed(buy)
                break # 按钮加载成功说明没有问题，跳出循环
            except:
                # 没有成功加载按钮说明出现了错误，无论什么错误都继续循环再次刷新页面
                continue

# 成功的信息输出和测试时的程序暂停
input('恭喜，抢购成功')
