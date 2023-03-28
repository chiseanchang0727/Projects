
# Improve Business Performance by Analyzing In-game User Behavior


# Outlines

1. Assess Product Performance
    - Compare revenue performance to industry benchmarks

2. Identify Key Metrics
    - Determine which metric(s) are impacting low revenue
3. Determine Retention-related In-Game Metrics by EDA
    - Identify relevant in-game metrics that contribute to retention performance

4. Identify Behavioral Patterns
    - Analyze user behavior data to identify patterns associated with good in-game performance
    
5. Generate Insights from Hypotheses and Validation
    - Identify the reason of good in-game performance with the insights from hypothesis

6. A/B Tests Proposal
    - Propose A/B tests to validate hypotheses 

6. Conclusions 
    - Summarize key findings and recommendations for future strategies


# Assess Product Performance



- **The revenue of our product after launching is lower than the average revenue of industry benchmarks.**

    <img src="https://user-images.githubusercontent.com/113814545/226541296-5bd1df40-9ab6-4e01-88ee-0e845710fd03.png" width="550">


# Identify Key Metrics


To investigate the reason for low revenue, I will analyze the metrics to determine which one may be contributing to the low revenue.

   
- Revenue can be decomposed to: 
$$Revenue = ARPU \times AU$$



- $AU$ is the number of active user, the formula is: 

$$AU = DNU\times R $$ 


- $R$ is called retention rate, which is the percentage of user who returns after their initial login.


- $DNU$ is daily new user, which is related with onboarding process and advertisment strategies.



## ARPU v.s. AU
From the following picture we can see:
   - ARPU nearly equls to the average ARPU of industry benchmarks.
   - AU is way lower than the average AU of industry benchmarks.
   - So AU would be the major problem of low revenue.
  


<img src="https://user-images.githubusercontent.com/113814545/226541661-a428cab7-3061-4f69-a647-11a17eb2f4c4.png" width="800">



## DNU v.s. Rentention


As we can see from following picture:

- The retention rate of our product is **lower** than benchmarks, especially in $R1$ (35%).
- However, there is no big difference between our proudct and benchmarks in DNU.
- So the problem of low AU comes from low Retention, especially in the first day, $R1$.



<img src="https://user-images.githubusercontent.com/113814545/227104697-e6ff818c-da5c-4951-bcfc-68490b7bbd86.png" width="900">



'0' means the launch date.

'1' 1 days after launching.

R1 = 35% means there is 35% of user returns in the second day.

R2 = 25% means there is 25% of user returns in the third day relative to the launch date.


## Summary:

Retention, especially $R1$, is the problem of low revenue.
    

# Determine Retention-related In-Game Metrics by EDA

To identify which user behavior metrics are related to retention, I will analyze several metrics and determine which of them have a correlation with retention

- The users is segamented into two groups:
    - churn: users leave in their first-engaged day
    - retained: users back in the second-engaged day


- For games, following metrics indicate the performance 
    - character final level
    - time spent
    - money spent
    - dungeon play times 



## Character final level

- The final level shows where do users stop playing.
- Insight:
    - Most of the churn user stop playing before level 7.
    - The median final level of retained user is level 26.
    - This would be a suitable metric for evaluating user performance.




<img src="https://user-images.githubusercontent.com/113814545/227104859-2de0f509-85d8-48cc-a90a-33b018bed8ee.png" width="750">







## Time spent

- following picture is the time spent distribution of users in the first-engaged day.
- Insights:
    - Churn players tend to play less than 20 mins.
    - Retained players tend to play more, most of them exceed 50 mins.
    - It's good to be metric, but the trend is similar to final level distribution.


<img src="https://user-images.githubusercontent.com/113814545/224939511-ef5d89b6-8284-4879-88b3-c9954d65243e.png" width="750">







## Money spent

- Compare the percentage of paid users in each group.
- Insights:
    - As we expected, almost all churn users didn't pay.
    - However, most of retained users didn't pay, too.
    - This metric is not good for the user performance.


<img src="https://user-images.githubusercontent.com/113814545/226516805-b1ee51a7-f1fe-4de9-9ffa-9bc048b796b6.png    " width="450">


## Dungeon play times

- Dungeon play times has the potential since it is the main content in early stage.
- Insights:
    - The median dungeon play times of churn users is 2 times.
    - The median dungeon play times of retained player is 7.
    - Retained player reach a high dungeon times(upper limit in first day).
    - This would be a suitable metric.

<img src="https://user-images.githubusercontent.com/113814545/227105434-fe0d9530-55fb-4336-813c-47f96f19b122.png" width="500">





## Metric selection

- The better metric would be character final level and dungeon times.
- Time spent and final level has similar trend, but level is highly connected with user journey.
- The performance of retained user in those metrics are:
    - character level >= 26
    - dungeon times >= 7
    
- This criterion is named as <span style='color:red'> "**retained status**" </span>
- The users reached this status in the first day called "retained-status users"


## Check whether the metric match our goal(higher retention rate)

Following picture shows that the retained status users perform better than the benchmark.

<img src="https://user-images.githubusercontent.com/113814545/226520687-e920cef1-b672-4d9d-89be-d9b645973bf2.png" width="500">



# Identify Behavioral Patterns

- In this project, the good in-game performance is defined with final level >=26 and dungeon times >= 7
 
- The behavior that related with the performance is found by implementing correlation analysis.


- Correlation anaalysis: Point-biserial correlation(since one variable is binary)

- Result is following:

![image](https://user-images.githubusercontent.com/113814545/225570453-298b95cc-b922-41fa-8cde-d2f4ecc14ed9.png)



- The behavior highly correlated with retained status is 'system_A_strengthen'


# Generate Insights from Hypotheses and Validation

## Hypothesis
- Players who strength more in system A would be more likely to reach the retained status

## Validation

- The contingency table of reaching retained status and system A strengthen is following:
    - recalled reatined status is: (final_level = 26) and (dungeon_times = 7) in first-engaged day
    - be caution the data only reflects the trend since confidential rule

- $H_0$: Reach retained status is nothing related with the strengthen in system A

|             | Reach retained status  | No reach retained status |
|-------------|:-----------:|:--------------:|
| Low strength. in system A |    67     |     2529      |
| High strength. in system A|   158     |     166      |



- p-value = 1.867e-188 < 0.05, the null hypothesis is rejected
- That is, system_A_strengthen is significant associated with reaching retained status



## Generate insights

- Since the metric ,dungeon play times, reflects how strong a chararcter is, it is a good guessing that the system A may contribute to character's ability.

- Following pie chart shows that system A is the major contribution before level 28 of the retained-status users.


<img src="https://user-images.githubusercontent.com/113814545/225538450-ad1b69cb-4a6f-440c-aae5-6a947bcafb92.png" width="300">


- An explanation is that system A contributes to character ability the most, users may got better feedback when playing dungeons.



- So, whether the strengthen in system A result in difference performance in dungeon feedback?
    - the metric for dungeion feedback: average dungeon time spent


- Following scatter plot shows the relationship between average dungeon time spent and the amount of strengthen in system A:
    - Users who strengthen more in system A has less dungeon time spent, which means they have better feedback when playing.

![image](https://user-images.githubusercontent.com/113814545/225576933-ddc1d7a2-f23d-4a1f-b939-0280e1193ea3.png)








### What's the probelm in strengthening the system A?

- I want to know:
    1. how many users who can access to system A knows it
    2. how many users who know system A reach the strengthen part of system A


- Following is the result:
    1. 69% of all users know the system A
    2. 14% of them reach the strengthen part.
        - there are several funnels, here I only list the major one
    
<img src="https://user-images.githubusercontent.com/113814545/227106003-05eca188-6f47-4b32-aacc-1e89508d10ac.png" width="750">




## Insights:

- strengthen in system A is highly related with reaching the retained status.
- The correlation coefficient is positve, which means strengthen more on system A will be more likely to reach retained status.
- However, we can not conclude that the strengthen on system A is the reason of good retention.

- Users who churned had negative feedback about playing dungeons compared to retained users.
- Positive feedback about playing dungeons is closely tied to the strength of system A.
- The layout design is hindering some users from discovering the strengthen aspect of system A.






# A/B Tests Proposal

Here is some proposal for checking the results we have, and testing even further to understand the underlying reason of users churn.

## Whether layout design is the problem of low retention
- For checking the reason of low revenue comes from fewer users knowing how to strengthen system A
    - Controal group: keep the original setting
    - Treatment group: increase the visibility by adjust the layout, such as elinimate layout_3

- If the retention
    - decrease: strengthen system A is not the reason
    - same: users strengthen system A is not the reason
    - increase: strengthen system A is the reason

## Whether strengthen system A bring good retention
- For testing the influence of strengthening system A:
    - Control group: keep the original setting
    - Treatment group: reduce the resource for system A by half

- If the retention
    - decrease: system A is important to retention
    - same: system A is nothing to do with retention
    - increase: system A affects the retention negatively


## Whether the retention relies on the feedback specific from system A
- For testing whether other system can replace system A if it can bring good feedback:
    - Control group: keep the original setting
    - Treatment group: replace the ability contribution of system A by system B
        - also adjust the user journey for sytem B

- If the retention
    - decrease: system A is special for users to keep playing
    - same: users are chasing good feedback no matter which system is
    - increase: system B may provide better feedback then system A




# Conclusions

The conlusion here do not cover the A/B test result, just summary the analysis results.

1. The layout design would be the major problem for users to find out the strengthen part of system A.
2. Users can get good feedback when playing dungeons by strengthening system A.
3. For understanding the reason of low retention, A/B test is necessary.
