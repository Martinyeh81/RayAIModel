# Question 2

|Packages|Version|
|---|---|
|Python|3.11.9|
|Ray|2.20.0|
  
## Environment
  於地端環境以K8S建立Ray Cluster(3 Nodes)環境
  ![RayclusterIP](https://github.com/Martinyeh81/RayAIModel/blob/main/RayXSquare/Images/RayIP.png)
  ![RayDashboardIP](https://github.com/Martinyeh81/RayAIModel/blob/main/RayXSquare/Images/RayDashboardIP.png)
## 執行
  執行RayRetry.py，總共for迴圈整個流程，但讓unstable_task function有50%的機率失敗，並且最多重複三次，超過就停止
  ![Task1](https://github.com/Martinyeh81/RayAIModel/blob/main/UnstableTask/Images/question2task.png)
  ![Task2](https://github.com/Martinyeh81/RayAIModel/blob/main/UnstableTask/Images/question2answer.png)
## 答案
  ![Answer2](https://github.com/Martinyeh81/RayAIModel/blob/main/UnstableTask/Images/question2finalanswer.png)
