import os
import requests

start = int(input(">>"))
end = int(input(">>"))

# 定义请求标头
headers = {
    "dnt": "1",
    "referer": "https://noy1.top/",
    "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
}

for i in range(start, end):
    print(f"{i} [start]")
    a = 1
    
    # 定义文件夹路径
    folder_name = f"bookid_{i}"
    current_directory = os.getcwd()
    folder_path = os.path.join(current_directory, folder_name)
    
    # 检查文件夹是否存在，如果不存在则创建
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    while True:
        img_url = f"https://img.noy.asia/{i}/{a}.webp" 
        try:
            # 发送GET请求，并添加自定义标头
            response = requests.get(img_url, headers=headers)
            
            if response.status_code == 200:
                img_data = response.content
                if len(img_data) > 1024:  # 检查图片是否大于1KB
                    with open(os.path.join(folder_path, f"{a}.webp"), "wb") as img_file:
                        img_file.write(img_data)
                    print(f"图片 {a}.webp 已保存.")
                else:
                    print(f"{i} 号文件夹下载完成，[end]")
                    break
            else:
                print(f"下载图片时发生错误，状态码: {response.status_code}")
                break
        except requests.RequestException as e:
            print(f"请求时发生错误: {e}")
            break
        a += 1
