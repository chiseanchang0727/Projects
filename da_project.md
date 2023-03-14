

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



 <img src="https://user-images.githubusercontent.com/113814545/224917759-9913a0d2-c11f-4b5d-af4a-1e48454d3199.png" width="750">


- Character level:
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
 

<img src="https://user-images.githubusercontent.com/113814545/224931576-d3e46326-f99e-4554-8d86-63a28a915396.png" width="750">




- Time spent(left panel):
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

- Money spent(right panel)
    - Based on previous experience, churn users nearly won't pay, so check the portion of paid at first
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


<img src="https://user-images.githubusercontent.com/113814545/224926798-397efb2d-b453-4141-83e1-d66abce3b2f5.png" width="500">


- Dungeon times:
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



# Identify behavior patterns that related with good performance

- In this project, the good performance is defined with level >=26 and dungeon times >= 7

- The behavior that related with the performance is found by implementing correlation analysis



- The highest behavior is the 'strengthen times in system A'


# Hypothesis 1: 
- Players who invent more in system A would be more likely to reach the retained status

(validate the hypothesis)


- Does the invention in system A result in difference performance in dungeon experience?
    - the metric for dungeion experience: death times, dungeion time spent



- As we can see: users who invent more in system A have better experience than users who do not.


- Moreover, the difference dungeon experience happends in the first 30mins after first engagement.

(show data that the most of entry time of those dugeon is lower than 30mins)

(show the ability contribution in terms of system A, B, C, where A is the major)

### Insights:
- The invention on system A will give good feedback in game experience
- Since the system A is the major contribution on character ability in early stage.


# Hypothesis 2:
- Players who have good experience in dungeon playing during the first 30mins would be more likely to reach retained status

- validate hypothesis 2:
    - segament the users who played over 30mins into groups: 
        - good experience in 30 mins
        - no good experience in 30 mins
            - good experience in 30+ mins
            - no good experience in 30+ mins
    - compare the ratio that reach retained status and retained in the next day

    - it turns out that:
        - good exp in 30 is the major user part
        - the ratio of reach retained status is the highest, then no good exp. in 30 but have good exp in 30+


### Insight: 
- If players got good experience in the frist 30mins would be more likey to keep playing.
- For now, the good experience relies on dungeion playing.
        





# A/B test

## System A invention test
- For testing the influence of invention on system A:
    - Control group: keep the original setting
    - Treatment group: reduce the resource for system A by half

- If the retention
    - decrease: system A is important
    - same: system A is nothing to do with retention
    - increase: system A affects the retention negatively


## Good experience in specific system test
- For understanding whether the system A is the key point result in good retention:
    - Control group: keep the original setting
    - Treatment grouop: 
        - replace the introduction of system A by system B
        - reduce the resource of system A, increase the resource of system B

- If the retention
    - decrease: good retetion relies on specific system
    - same: good retention doesn't relies on specific system
    - increase: good retetion relies on specific system



- However, the property of system A and system B are different, if most of the players like fighting related system they will prefer system A. This may affect the result.


## Good experience in first 30mins after engagement test

- For understanding if good experience should be set in the first 30mins:
    - Control group: keep the original setting
    - Treatment group:
        - postpone the introduction of system A after 30mins of first engagment

- If the retention
    - decrease: good experience in first 30mins is important for user to keep playing
    - same: 30mins is not crucial for users, good experience is
    - increase: good experience in first 30mins is negative influence to retention


# Conclusion
