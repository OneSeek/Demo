from selenium import webdriver


def get_html(url_):

    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        browser = webdriver.Chrome(executable_path='D:\Downloads\chromedriver_win32\chromedriver.exe'
                                   , options=chrome_options)

        # Get local session of firefox
        browser.get(url_)
        # Load page
        # print(browser.page_source)
        html_ = browser.page_source

    except Exception as e:
        print('获取源代码失败：%s' % e)

    return html_


if __name__ == '__main__':

    movie_title_list = []
    starring_list = []
    type_list = []
    region_list = []
    years_list = []
    movie_description_list = []
    imageUrl_list = []

    for i in range(1, 3):  # range(1, 68) 1到67页

        url = "http://v.duba.com/movie/list/filter-true+" \
                  "complete-%E6%AD%A3%E7%89%87+order-pubtime+pn-" + str(i) + "+channel-movie"
        html = get_html(url)


