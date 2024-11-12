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
  


## 答案
  ![Answer2](https://github.com/Martinyeh81/RayAIModel/blob/main/UnstableTask/Images/question2finalanswer.png)
