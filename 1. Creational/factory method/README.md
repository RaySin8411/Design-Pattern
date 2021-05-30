# 工廠方法 Factory Method
在父類中提供一個創建對象的方法， 允許子類決定實例化對象的類型。

## Architecture

![](https://refactoringguru.cn/images/patterns/diagrams/factory-method/structure.png?id=4cba0803f42517cfe854)

1. 產品(Product)

    將會對接口進行聲明。對於所有由創建者及其子類構建的對象，這些接口都是通用的。

2. 具體產品(Concrete Products)
    
    是產品接口的不同實現。

3. 創建者(Creator)

    包含一些與產品相關的核心業務邏輯
    
4. 具體創建者(Concrete Creators)
    
    會重寫基礎工廠方法，使其返回不同類型的產品。