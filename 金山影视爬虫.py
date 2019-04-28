import  requests
import json
from requests.exceptions import RequestException


def get_page(pagenum):
    url = "http://v.duba.com/commonapi/movie2level/?" \
        "filter=flase&" \
        "type=&area=&" \
        "actor=&" \
        "start=&" \
        "complete=%E6%AD%A3%E7%89%87" \
        "&order=pubtime" \
        "&pn="+str(pagenum)+"&rating=&prop=&channel=movie"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print("请求出错")
        return None


def parse_page(pagenum):
    html = get_page(pagenum)
    data = json.loads(html)
    items = data['videoshow']['videos']
    for item in items:
        id = item['id']
        title = item['title']
        try:
            extrd = item['extRd']
        except Exception:
            pass
        type = item['type']
        date = item['date']
        intro = item['intro']
        img_url = item['imgh_url']
        main_actor = []
        movie_type = []
        print("序号：{}，电影名称:{}, 电影描述:{}，上映时间:{}, 电影图片路径:{}".format(id, title, intro, date, img_url), end=" ")
        print("主演：", end="")
        for it in extrd:
            main_actor.append(it['name'])
            print(it['name'], end=" ")
        print("类型：", end="")
        for it in type:
            movie_type.append(it['name'])
            print(it['name'], end=" ")
        print("")
        yield {
            "序号": id,
            "电影名称": title,
            "电影描述": intro,
            "上映时间": date,
            "电影图片路径": img_url,
            "主演": main_actor,
            "类型": movie_type
        }


def write_to_file(content):
   with open('result.txt', 'a', encoding='utf-8') as f:
           f.write(json.dumps(content, ensure_ascii=False)+"\n")
           f.close()


def get_result(start, end):
    for i in range(start, end):
        for item in parse_page(i):
           write_to_file(item)


def main():
    start = eval(input("请输入起始页："+"\n"))
    end = eval(input("请输入终止页：" + "\n"))
    get_result(start, end+1)


if __name__ == '__main__':
    main()
