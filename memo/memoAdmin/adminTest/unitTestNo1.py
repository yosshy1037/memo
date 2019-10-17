from ...common import const,constDef,constTest,unitTestClass

## ログイン画面クラス
class loginTest(unitTestClass.unitTest):
  
  # コンストラクタ
  def __init__(self, testNo):
    super().__init__(testNo)
    
  # ログイン実施テスト
  def test(self):
    
    # user/passSET
    eleUser = self.chromeBrowser.find_element_by_name('loginUser').send_keys("Ykanai")
    elePass = self.chromeBrowser.find_element_by_name('loginPassword').send_keys("Ykanai01")
    
    # ログイン押下
    self.chromeBrowser.find_element_by_class_name('login').click()
    
    # URLチェック
    if self.re.search("memoSearch\/", self.chromeBrowser.current_url) != None:
      self.testSuccessStatus = True
    
    # スナップショット取得
    self.screenShotFull(self.chromeBrowser, 'C:\Work\python\chapt')
    
    # 時間待ち
    self.time.sleep(5)
    
    # 終了処理
    self.quit();