

# Outlines

1. What is the problem?

2. What is the project goal?

3. Analysis procedures

4. Identify key metrics

5. Insights from hypotheses and validation

6. Conclusion


# What is the problem?

- The revenue of our product after launching is lower than the A-class products.

<img src="https://user-images.githubusercontent.com/113814545/224621196-236ca839-4ed1-45d3-acb1-3a2488170f14.png" width="550">

- According to the formula, revenue can be decomposed to: 
$$Revenue = AU \times ARPU$$
- $AU$ is the number of active user. For the $n$ th day after launching: 

$$AU_n = \Sigma_{i,j}^{n}DAU_i\times R_{ij} $$ 

$$ i,j ∈ \lbrace 0, 1, 2, ..., n\rbrace $$ 
- $R_{ij}$ is the retention rate in $j$ th day where the users frist engage in $i$ th day.
- $DAU$ is related with onboarding processand advertisment strategies, which will not be covered in this project.

## Problem identification on retention rate or ARPU

- Following picture is the comparsion of retention rate and ARPU between our product and A-class products.

<img src="https://user-images.githubusercontent.com/113814545/224629594-2db7c745-de3d-458c-a9a9-598dffccb1e3.png" width="1000">



- The retention rate of our product is way **lower** than competitors.
- However, the difference of ARPU between our proudct and competitors is not that much.

- Moreover, the retention rate in Day1(called R1) decreases the most compare with other days.


<img src="https://user-images.githubusercontent.com/113814545/223676733-2bd96b3f-7926-4ed2-a07b-d67d7155d194.png" width="550">


- So the problem that result in lower revenue would be the low R1.


# What is the project goal?

- This project analyze the user behavior pattern in the first engagment day to find out the possible driver that can improve the retention.




# Analysis procedures

1. identify key metrics for defining user performance

2. identify out behavior patterns that related with good performance

4. develop insight from the behaivor patterns

5. propose A/B test





# Identify key metrics

- First the users is segamented into two groups:
    - churned: users leaved in their first engaged day
    - retained: users back in the second engaged day


- For games, following metrics can represent the user performance
    - character level
    - time spent
    - money spent
    - dungeon times 



## Character level


 <img src="https://user-images.githubusercontent.com/113814545/224939335-0e5773a9-f771-4cd6-9e73-6d9f4ce7c4e8.png" width="750">


- Data processing:
    - raw data: user leveling data
    - processing: 
        - select the final character level record of each user in first-engaged day
        - tag user with 'churn' if they didn't come back in the next day
        - tag user with 'retained' if they came back in the next day
- Visualize the distributioin of user number by each character level with bar chart.
- Insight:
    - Most of the churn user stopped playing before level 7.
    - The final level of most retained user is exceed level 27.
    - This would be a suitable metric for evaluating user performance.




## Time spent

<img src="https://user-images.githubusercontent.com/113814545/224939511-ef5d89b6-8284-4879-88b3-c9954d65243e.png" width="750">



- Data processing:
    - raw data: user online time data
    - processing:
        - sum over the online time by each user in first-engaged day
        - group the total play time by 10 mins
        - set more than 60mins as '>60'
        - tag user with 'churn' if they didn't come back in the next day
        - tag user with 'retained' if they came back in the next day
- Visualize the user number by each time group with bar chart.

- Insights:
    - Churn players tend to play less than 20 mins.
    - Retained players tend to play more, most of them exceed 50 mins.
    - It's good to be metric, but the trend is similar to final level distribution.




## Money spent

<img src="https://user-images.githubusercontent.com/113814545/224939019-3e6a9c75-445d-4cd9-a253-5f5cf292122e.png" width="450">


- Based on previous feedback, churn users nearly won't pay, so check the portion of paid at first
- Data processing:
    - raw data: user payment data & user login data
    - processing: 
        - sum over the payment by each user, named as 'paid_amount', in first-engaged day
        - left join the login data with 'paid_amount' data
        - fill NA with 0
        - if paid_amount equals to 0, label the user with 'no paid'
        - if paid_amount more than 0, label the user with 'paid'
        - tag user with 'churn' if they didn't come back in the next day
        - tag user with 'retained' if they came back in the next day
- Visualize the portion of paid and no paid with pie chart.
- Insights:
    - As we expected, almost all churn users didn't pay.
    - However, most of retained users didn't pay, too.
    - This metric is not good to stand for the user performance.





## Dungeon times

<img src="https://user-images.githubusercontent.com/113814545/224926798-397efb2d-b453-4141-83e1-d66abce3b2f5.png" width="500">


- Since dungeon is the main content in early stage, it has potential to be metric.
- Data processing:
    - raw data: user dungeon-play data
    - preprocessing:
        - calculate the dungeon times by each user in first-engaged day
        - tag user with 'churn' if they didn't come back in the next day
        - tag user with 'retained' if they came back in the next day
- Visualize the user number in each dugeon times group with bar chart.
- Insights:
    - Most churn player didn't play dungeon before leaving.
    - Retained player reach a high dungeon times(upper limit in first day).
    - This makes sense because the dungeons are unavoidable during leveling.
    - This would be a suitable metric.


## Metric selection

- In here, the better metric would be character level and dungeon times
- The performance of retained user in those metrics are:
    - character level >= 26
    - dungeon times >= 7
    
- This criterion is named as <span style='color:red'> "retained status" </span>


### Check whether the metric match our target(higher retention rate)

(data)


# Identify behavior patterns that related with good performance

- In this project, the good performance is defined with level >=26 and dungeon times >= 7
 
- The behavior that related with the performance is found by implementing correlation analysis

- Data processing:
    - raw data: 
        - user leveling data and user dungeon data in first-engaged day
        - other user behaivor data in first-engaged day
    - extract the max level and sum over the dungeon times by each charater, then merge together
    - create a column called 'retained_status': if the max level equals to 26 and dugeon times equals to 7, then assigned 'True'. Else assigned 'False'

- Correlation anaalysis: Point-biserial correlation(since one variable is binary)

- Result is following:

![image](https://user-images.githubusercontent.com/113814545/225570453-298b95cc-b922-41fa-8cde-d2f4ecc14ed9.png)



- The behavior highly correlated with retained status is 'system_A_strengthen_1


# Hypothesis、Validation

## Hypothesis
- Players who strength more in system A would be more likely to reach the retained status

## Validation

- The contingency table of reaching retained status and system A strengthen is following:
    - recalled reatined status is: (max_level = 26) and (dungeon_times = 7) in first-engaged day
    - be caution the data only reflects the trend since confidential rule

|             | Reach retained status  | No reach retained status |
|-------------|:-----------:|:--------------:|
| Low strength. in system A |    67     |     2529      |
| High strength. in system A|   158     |     166      |



- where p-value = 1.867e-188 < 0.05, the null hypothesis is rejected
=> system_A_strengthen is significant associated with reaching retained status



## Summaries

- strengthen in system A is highly related with reaching the retained status.
- Hoever, we can not conclude that the strengthen on system A is the reason for coming back in next day.


# Investigate the reason

- Since the metric ,dungeon play times, reflects how strong a chararcter is, it is a good guessing that the system A may contribute to character's ability.

- Following pie chart shows that system A is the major contribution before level 28.


<img src="https://user-images.githubusercontent.com/113814545/225538450-ad1b69cb-4a6f-440c-aae5-6a947bcafb92.png" width="300">


- An explanation is that system A contributes to character ability the most, users may got better feedback when playing dungeons.


## Check the dugeon performance with system A strengthen

- Whether the strengthen in system A result in difference performance in dungeon feedback?
    - the metric for dungeion feedback: average dungeon time spent


- Following scatter plot shows the relationship between average dungeon time spent and the amount of strengthen in system A:
    - Users who strengthen more in system A has less dungeon time spent, which means they have better feedback when playing.

![image](https://user-images.githubusercontent.com/113814545/225576933-ddc1d7a2-f23d-4a1f-b939-0280e1193ea3.png)








## What's the probelm in strengthing in system A?

- I want to know:
    1. how many users who can access to system A knows the system
    2. how many users reach the strengthen part of system A


- Following is the result:
    1. 69% of all users know the system A
    2. 14% of them reach the strengthen part.
        - there are several funnels, here I only list the major one
    
<img src="https://user-images.githubusercontent.com/113814545/225564161-7783a7dd-4531-4a63-aa72-7c54ba27c396.png" width="750">



# Insights:
- The strengthen in system A give good feedback in game feedback
- Layout design result in only fewer users strengthing in system A.








# A/B test

## System A strengthen test
- For testing the influence of strengthen on system A:
    - Control group: keep the original setting
    - Treatment group: reduce the resource for system A by half

- If the retention
    - decrease: system A is important
    - same: system A is nothing to do with retention
    - increase: system A affects the retention negatively



# Conclusion

1. The strengthen in system A is important for users to keep playing.
2. The strengthen will give good feedback on dungeon playing in return.
3. The layout design would be the major problem for users to find out the strengthen part of system A.
