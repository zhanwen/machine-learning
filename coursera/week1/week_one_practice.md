# Introduction  

###### 一. A computer program is said to learn from experience E with respect to some task T and some performance measure P if its performance on T, as measured by P, improves with experience E.Suppose we feed a learning algorithm a lot of historical weather data, and have it learn to predict weather. In this setting, what is T?

  1. The process of the algorithm examining a large amount of historical weather data.  
  2. The weather prediction task.
  3. The probability of it correctly predicting a future date's weather. 
  4. None of these.

##### 选择第一个答案，T表示任务，在预测天气情况的时候为预测天气的算法。P表示对应的概率也就是该题中的第3个选项。E表示经验，在该题中表示以前的数据。

###### 二. Suppose you are working on weather prediction, and use a learning algorithm to predict tomorrow's temperature (in degrees Centigrade/Fahrenheit).Would you treat this as a classification or a regression problem?

   1. Regression
   2. Classification

##### 选择第一个答案，在预测明天的具体的天气温度，需要以前的数据来预测，并且要有具体的值返回所以是回归问题。


###### 三. Suppose you are working on stock market prediction, and you would like to predict the price of a particular stock tomorrow (measured in dollars). You want to use a learning algorithm for this. Would you treat this as a classification or a regression problem?

   1. Classification
   2. Regression

##### 选择第二个答案，预测明天股票的价格是多少，也是同样的道理，需要根据之前的数据来进行回归分析，并给出具体的预测值，属于回归问题。

###### 四. Some of the problems below are best addressed using a supervised learning algorithm, and the others with an unsupervised learning algorithm. Which of the following would you apply supervised learning to? (Select all that apply.) In each case, assume some appropriate dataset is available for your algorithm to learn from.

1. Examine the statistics of two football teams, and predict which team will win tomorrow's match (given historical data of teams' wins/losses to learn from).
2. Examine a large collection of emails that are known to be spam email, to discover if there are sub-types of spam mail.
3. Given genetic (DNA) data from a person, predict the odds of him/her developing diabetes over the next 10 years.
4. Take a collection of 1000 essays written on the US Economy, and find a way to automatically group these essays into a small number of groups of essays that are somehow "similar" or “related".

##### 选择第一个和第三个答案。监督学习简单理解就是要（correct answer），在该题中第一个选项输入预测哪个球队将会赢得比赛，预测比赛结果要根据每个球队的人员数据来进行预测，并给出结果，这也属于回归问题，第三个选项是根据个人的DNA信息来预测这个人未来10年是否会得糖尿病，要预测是否会得该病，就需要根据这个人的DNA信息和之前的数据进行预测来得出是否会得该病，所以也属于回归问题。无监督学习：第二个选项是一个垃圾邮件的集合，找出这个子邮件是否垃圾邮件，属于分类的问题（即true or false）。第四个选项给出1000篇文章，对这些文章进行分组，给出哪些是“similar” 哪些是”related“，也是属于分类的问题，同时属于无监督学习。

###### 五. Which of these is a reasonable definition of machine learning?
1. Machine learning is the field of study that gives computers the ability to learn without being explicitly programmed.
2. Machine learning learns from labeled data.
3. Machine learning is the science of programming computers.
4. Machine learning is the field of allowing robots to act intelligently.

##### 选择第一个选项，机器学习的定义，让计算机自己去学习。

