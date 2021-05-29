# 單例模式 Singleton

## Old
1. Standard
    
    類似 Java 的標準 singleton 模式，
    有一個表示私有的類別變數 _instance 儲存 singleton 模式的物件，
    並用一個靜態方法 get_instance() 來負責物件的取得與物件實體化
    
2. Module

    利用 python 模組全域特性

3. Meta

    使用 metaclass 改變類別定義行為

## New
關鍵就是利用 __ new __ 來去改變物件的建構行為

## Reference
* [python 實現 singleton 模式](https://mark1002.github.io/2018/07/31/python-%E5%AF%A6%E7%8F%BE-singleton-%E6%A8%A1%E5%BC%8F/)
    