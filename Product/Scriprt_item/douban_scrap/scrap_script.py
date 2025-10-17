from bs4 import BeautifulSoup
import requests
import csv
import time

# 获取网页内容
def get_movies(movies_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/115.0 Safari/537.36"
    }
    response = requests.get(movies_url, headers=headers)
    response.encoding = "utf-8"
    return response


# 解析网页内容
def analysis_movies(web_response):
    soup = BeautifulSoup(web_response.text, "html.parser")

    # 猫眼首页电影结构不同，用下面这行能抓到榜单部分
    movies = soup.select("div.board-item-content")

    movies_information = []
    for movie in movies:
        title_tag = movie.select_one("p.name a")
        score_tag = movie.select_one("p.score i")
        time.sleep(0.5)

        if title_tag:
            movie_name = title_tag.text.strip()
            movie_link = "https://www.maoyan.com" + title_tag["href"]
            movie_score = score_tag.text if score_tag else "暂无评分"
            movies_information.append((movie_name, movie_score, movie_link))
    return movies_information


# 保存为 CSV 文件
def save_movies_information(movies_information):
    with open(r"D:\Mashall&&SiaoPul\WOT\maoyan.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["电影名", "评分", "链接"])
        for item in movies_information:
            writer.writerow(item)


# 主流程
def main():
    url = "https://www.maoyan.com/board/4"  # 猫眼TOP100页面
    response = get_movies(url)
    data = analysis_movies(response)
    save_movies_information(data)

    for movie_name, movie_score, movie_link in data:
        print(f"{movie_name} 🎬 {movie_score} 分 -> {movie_link}")


if __name__ == "__main__":
    main()