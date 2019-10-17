from abc import ABCMeta
from abc import abstractmethod
from . import const,constDef,constTest
from selenium import webdriver
import os,time,re,subprocess

## テスト実施クラス
class unitTest(metaclass = ABCMeta):

  # コンストラクタ
  def __init__(self ,testNo):
  
    # プライベート変数
    self.chromeBrowser = ""
    self.opt = ""
    self.chromeDriver = const.chromeDriver
    self.targetSiteUrl = const.targetSiteUrl
    self.uriInfo = ""
    self.testSuccessStatus = False
    self.testNumber = int(testNo)
    self.time = time
    self.re = re
    #self.request = request
    
    # テスト対象サイトOpen
    self.openTestSite()

  # テスト対象サイトOpen
  def openTestSite(self):
    # driverSET
    self.opt = webdriver.ChromeOptions()
    if const.viewDisable:
      self.opt.add_argument('--headless')
    self.opt.add_argument('--disable-gpu')
    self.chromeBrowser = webdriver.Chrome(options=self.opt, executable_path=self.chromeDriver)
    
    # memoサイト
    self.chromeBrowser.get(self.targetSiteUrl)
  
  # テストメソッド
  @abstractmethod
  def test(self):
    pass
  
  # 終了処理
  def quit(self):
    self.chromeBrowser.quit()
  
  # スクリーンショット取得関数
  def screenShotFull(self, driver, filename, timeout=30):
    '''フルページ スクリーンショット'''
    # url取得
    url = driver.current_url
    
    # ページサイズ取得
    w = driver.execute_script("return document.body.scrollWidth;")
    h = driver.execute_script("return document.body.scrollHeight;")
    
    # コマンド作成
    cmd = 'gtimeout ' + str(timeout)  \
        + ' "/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary"' \
        + ' --headless' \
        + ' --hide-scrollbars' \
        + ' --incognito' \
        + ' --screenshot=' + filename + '.png' \
        + ' --window-size=' + str(w) + ',' + str(h) \
        + ' ' + url
    
    # コマンド実行
    subprocess.Popen(cmd, shell=True,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT)