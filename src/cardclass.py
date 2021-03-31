class Card:
    def __init__(self, url):
        global driver
        self.url = url
        self.author = None
        self.date = None
        self.title = None
        self. content = None
        self.publisher = None

        #Send article into search and hit enter
        search = driver.find_element_by_id("source")
        search.send_keys(self.url)
        search.send_keys(Keys.RETURN)


    def find_author(self):
        global driver
        try:
            author = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "author")))
            author_raw = author[0].text
            self.author = author_raw.split()[1]
        except:
            author_raw = "NA"
            self.author = "[No Author Detected]"
        return self.author, author_raw


    def find_date(self):
        global driver
        try:
            date = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "date")))
            date_raw = date[0].text
            self.date = date_raw.split()[2][-2] + date_raw.split()[2][-1]
        except:
            date_raw = "NA"
            self.date = "[No Date Detected]"
        return self.date, date_raw


    def find_title(self):
        global driver
        try:
            title = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, 'html/body/outline-app/outline-article/div[2]/div/div[2]/h1')))
            self.title = title[0].text
        except:
            self.title = "Change Title"
        return self.title


    def find_content(self):
        global driver
        try:
            content = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '/html/body/outline-app/outline-article/div[2]/div/raw')))
            self.content = content[0].text
        except:
            self.content = "Evidence Not Found"
        return self.content

    def publisher(self):
        global driver
        try:
            publisher = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'soft-link')))
            self.publisher = publisher[0].text
        except:
            self.publisher = "Publisher Not Found"
        return self.publisher

print("done")
c1 = Card(search_url)
c1author, author_raw = c1.find_author()
