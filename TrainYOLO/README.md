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
  
  4. optimizer: Adam

     結合Momentum與RAMSprop的優點，加速收斂
  
  5. Learning Rate: 0.000526 (AUTO)
     先從高的learning rate開始訓練，因使用的模型是pretrain好的，可以直接調整參數warmup_epochs=0，讓一開始的learning rate比較大。

     如果loss function在訓練早期波動劇烈或無法收斂，可能需要減小Learning Rate。

     如果損失減少得非常緩慢，則可以慢慢增加Learning Rate。

## Train Result

|| Epoch | Precision | Recall |
|-------|-------|---------------|------------|
| Train | 30    | 0.94545       | 0.87700    |
| Val | 30    | 0.94552       | 0.87706    |


### Confusion_Matrix_normalized
![Confusion](https://github.com/Martinyeh81/RayAIModel/blob/main/TrainYOLO/Images/confusion_matrix_normalized.png)

### F1_curve
![F1](https://github.com/Martinyeh81/RayAIModel/blob/main/TrainYOLO/Images/F1_curve.png)

### Precision
![P](https://github.com/Martinyeh81/RayAIModel/blob/main/TrainYOLO/Images/P_curve.png)

### Recall
![R](https://github.com/Martinyeh81/RayAIModel/blob/main/TrainYOLO/Images/R_curve.png)

## Tune
微調Learning Rate，選取10個從0.00005~0.1之間的數值，查看最佳的準確度
![Tune](https://github.com/Martinyeh81/RayAIModel/blob/main/TrainYOLO/Images/YOLOtune.png)

### 判斷 Overfitting:
  1. 如果trainset的 F1 score、recall 和 precision 高於 val set的值並且差距太大，代表Overfitting
  2. 觀察曲線如果train loss 持續下降但 val loss 在某個點開始上升，這也是Overfitting
### 解決 Overfitting 方法：
  1.Data Augmentation
  2.Dropout參數，讓Network避免fully connect
  3.Early Stopping
  4.增加train set的數量
  5.降低 learning rate

### 如果不是YOLO
  1.可以正則化 (Regularization)L1 or L2
  2.調整模型複雜度(Layer)




