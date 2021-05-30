# 單例模式 Singleton

## 優缺點
### 優點
1. 保證一個類只有一個實例

    最常見的原因是控制某些共享資源（例如數據庫或文件）的訪問權限。
    
2. 為該實例提供一個全局訪問節點

### 缺點
違反了單一職責原則(Single Responsibility Principle)

## 實現方式
下列兩個步驟
* 將默認構造函數設為私有， 防止其他對象使用單例類的運算符 new
* 新建一個靜態構建方法作為構造函數。 該函數會 “偷偷” 調用私有構造函數來創建對象， 並將其保存在一個靜態成員變量中。 此後所有對於該函數的調用都將返回這一緩存對象。

## Code
### Old
1. Standard
    
    類似 Java 的標準 singleton 模式，
    有一個表示私有的類別變數 _instance 儲存 singleton 模式的物件，
    並用一個靜態方法 get_instance() 來負責物件的取得與物件實體化
    
2. Module

    利用 python 模組全域特性

3. Meta

    使用 metaclass 改變類別定義行為

### New
關鍵就是利用 __ new __ 來去改變物件的建構行為

## Reference
* [python 實現 singleton 模式](https://mark1002.github.io/2018/07/31/python-%E5%AF%A6%E7%8F%BE-singleton-%E6%A8%A1%E5%BC%8F/)
    