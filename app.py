import os
import logging

from pyvirtualdisplay import Display
from selenium import webdriver
from flask import Flask, jsonify, make_response, request

logging.getLogger().setLevel(logging.INFO)

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

class Scraper:
  def __init__(self, url, driver):
    self.url = url
    self.driver = driver
    if self.driver == 'PhantomJS':
      self.browser = self.init_PhantomJS()
    else:
      self.browser = self.init_Chrome()

  def init_Chrome(self):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('headless')
    return webdriver.Chrome(chrome_options=chrome_options)

  def init_PhantomJS(self):
    browser = webdriver.PhantomJS()
    browser.set_window_size(1024, 768) # optional
    return browser

  def get_htm(self):
      display = Display(visible=0, size=(800, 600))
      display.start()
      status = True
      html = ''

      try:
          self.browser.get(self.url)
          html = self.browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
          #logging.info(html)
          if len(html.split(' '))<10:
              status = False
      except:
          status = False

      self.browser.quit()
      display.stop()
      return status, html


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/get_page', methods=['GET'])
def page_source():
    if request.method == 'GET':
        url = request.args.get('url')
        driver = request.args.get('driver')

        sc = Scraper(url, driver)
        status, html = sc.get_htm()
        if html and status:
            return jsonify({'status_code': 200, 'html': html})
    return make_response(jsonify({'error':'error scraper', 'status_code':500}), 500)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False, port=5056)

