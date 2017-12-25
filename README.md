# Human-Computer-Interface

## HW5題目
利用背景相減(background subtraction)原理,設計出以手擺動選擇指令項目之介面。

## 環境
系統：macOSX 10.11.6
程式語言：python2.7.13
使用套件：opencv-python

## 執行方法
在terminal上執行指令：`python2 backgroundSubtraction.py`

## 執行結果
會開啟攝像頭並顯示視窗。視窗左邊有一個小方框，透過背景相減(background subtraction)的原理，當偵測到物體移動量 > threshold，便會進行倒數3秒(畫面上會顯示數字)，然後會拍照。在倒數期間，並不會偵測物體的移動。

拍照完的結果會存在`backgroundSubtraction.py`所在的資料夾，檔名是`photo-數字.jpg`。每次將程式重新啟動時，數字會重新從1開始計算，當資料夾已經存有相同檔名的檔案時，新的檔案會直接蓋掉舊的檔案。
