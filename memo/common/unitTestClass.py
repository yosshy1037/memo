from . import const,constDef,constTest
from selenium import webdriver
import os,time,re

## テスト実施クラス
class unitTest():

  # コンストラクタ
  def __init__(self):
  
    # プライベート変数
    self.__chromeBrowser = ""
    self.__opt = ""
    self.__chromeDriver = const.chromeDriver
    self.__targetSiteUrl = const.targetSiteUrl
    self.__uriInfo = ""
    self.__testSuccessStatus = False
    
    # テスト対象サイトOpen
    self.__openTestSite()

  # テスト対象サイトOpen
  def __openTestSite(self):
    # driverSET
    self.__opt = webdriver.ChromeOptions()
    if const.viewDisable:
      self.__opt.add_argument('--headless')
    self.__opt.add_argument('--disable-gpu')
    self.__chromeBrowser = webdriver.Chrome(options=self.__opt, executable_path=self.__chromeDriver)
    
    # memoサイト
    self.__chromeBrowser.get(self.__targetSiteUrl)
  
  # ログイン実施テスト
  def loginTest(self):
  
    # user/passSET
    eleUser = self.__chromeBrowser.find_element_by_name('loginUser').send_keys("Ykanai")
    elePass = self.__chromeBrowser.find_element_by_name('loginPassword').send_keys("Ykanai01")
    
    # ログイン押下
    self.__chromeBrowser.find_element_by_class_name('login').click()
    
    # URLチェック
    if re.search("memoSearch\/", self.__chromeBrowser.current_url) != None:
      self.__testSuccessStatus = True
    print(self.__testSuccessStatus)
    
    # 時間待ち
    time.sleep(5)
    
    # 終了処理
    self.__quit();
  
  # 終了処理
  def __quit(self):
    self.__chromeBrowser.quit()

  # リクエスト
  @property
  def request(self):
    return self.__request

  @request.setter
  def request(self,request):
    self.__request = request