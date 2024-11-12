# Question 3 and 4 

|Packages|Version|
|---|---|
|Python|3.11.9|
|Ray|2.20.0|
|ultralytics|8.3.27|
  
## Data
  1. The data is from Kaggle(https://www.kaggle.com/code/pkdarabi/traffic-signs-detection-using-yolov8)
  2. 總共15種Labels
  3. 圖片為416 x 416 pixels x 3 channels
     ![Sign](https://github.com/Martinyeh81/RayAIModel/blob/main/TrainYOLO/Images/SignExample.png)
  5. 使用labelImg(https://github.com/HumanSignal/labelImg?fbclid=IwY2xjawGe_fFleHRuA2FlbQIxMAABHS9x4cSMEli4qSIB_AObBBZEo5meAJX_K5yjCMdmhMspUnwcgqpUmeNtOg_aem_gRo9maKcgYEnivzIhATJaw) 畫BoundingBox並產生出yolo format(COCO format)
     ![Labelimg](https://github.com/Martinyeh81/RayAIModel/blob/main/TrainYOLO/Images/Labelimg.png)
  
## Number of calsses
  因label數量不平均，因此可以使用Image Augumentation or Generate Image
  ![Sample](https://github.com/Martinyeh81/RayAIModel/blob/main/TrainYOLO/Images/labels.jpg)
  1. Image Augumentation: 使用opencv or pytorch調整圖像，例如顏色修改，左右顛倒，讓圖片數量增加
  2. 生成圖像模型: 使用AIGC或是GAN技術增加圖片，例如DALL-E2
     ![AIGCSSample](https://github.com/Martinyeh81/RayAIModel/blob/main/TrainYOLO/Images/AIGCSSample.png)
  
## Traning
### 分割資料
  因數據總共只有4969分，因此拆分成以下:
  
  trainset's shape is (3530, 640*640) 70%
  
  Valset's shape is (801, 640*640) 17%
  
  testset's shape is (638, 640*640) 13%
### 超參數調整
  1. Epoch: 30

     數值越大準確度越高，但如過大於某個界線可能會Overfitting
  
  3. batch size: 16

     數值越低運算能力快，收斂慢，在一定的時間下會找到極值，在做gradient descent時候容易會Global minimum，但小batch size 的噪聲可能導致訓練不穩定，並可能需要更小的學習率。

     數值越高運算能力慢，收斂快，但會找不到到極值，在做gradient descent時候容易會Local minimum
  
  5. optimizer: Adam
     結合Momentum與RAMSprop的優點
  6. Learning Rate:
     如果損失函數在訓練早期波動劇烈或無法收斂，可能需要減小學習率。
     如果損失減少得非常緩慢，則可以考慮逐步增大學習率。

## 結果
### confusion_matrix_normalized
![AIGCSSample](https://github.com/Martinyeh81/RayAIModel/blob/main/TrainYOLO/Images/AIGCSSample.png)



