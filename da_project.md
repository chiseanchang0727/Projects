# Increasing the retention rate by analyzing user behavior

## Outlines

## What is the problem?

- The revenue of our product after launching is lower than the A-class products

<img src="https://user-images.githubusercontent.com/113814545/224621196-236ca839-4ed1-45d3-acb1-3a2488170f14.png" width="550">

- According to the formula, revenue can be decomposed to: 
$$Revenue = AU \times ARPU$$
- $AU$ is the number of active user. For the $n$ th day after launching: 

$$AU_n = \Sigma_{i,j}^{n}DAU_i\times R_j $$ 

$$ i,j ∈ \lbrace 0, 1, 2, ..., n\rbrace $$


- The retention rate of our product is **lower** than the average retention rate of A-class products in the market.
- The ARPU of our proudct is slightly lower than other A-class products.

<img src="https://user-images.githubusercontent.com/113814545/224620775-22a7dee3-973b-4314-abb5-168a031c15d7.png" width="1000">




- The retention rate in Day1(called R1) decreases the most compare with other days.


<img src="https://user-images.githubusercontent.com/113814545/223676733-2bd96b3f-7926-4ed2-a07b-d67d7155d194.png" width="550">




## What is retention rate?
- the percentage of new users who remain active after a given period.
- retention formula : 
$$Retention \space Rate =\Sigma_{i,j}^n \frac{AU_j}{DAU_i} \times 100\\% $$
- $DAU_i$ : daily new user numbers in ith day after product launching.
- $AU_j$ : active user numbers in jth day relative the each $DAU_i.





## What is the project goal?

- Increasing the retention rate in Day1(R1) by analyzing the user behavior.


### How to define success for this project?

- Figure out what user behavior would lead higher retention rate.
- Figure out the insight from the user behavior.
- Provide suggestion that stakeholder can accept.
- Run a A/B test to show difference.

## Analysis procedures

- Identify the user status by key metrics that relevant to R1.
- Segment the users into groups by the metrics.
- Idenitfy significant difference in retention rate between groups.
- Look for user behavior patterns that associated with the user status.
- Hypothesis 1:(Players who invent more in the specific system would be more likely to reach the user status)
- Validae the hypothesis 1
- Hypothesis 2:(Players who have good feedback in dungeon playing during the first 30mins of first engagement would be more likely to reach the user status)
- Validate the hypothesis 2:(define the experience metric, define the good experience, it turns out 30mins is not main point but most users leaves in 30mins)
- Conclusion:(If players get good feedback in dungeon playing, they would be more likely to be back in the next day. This feedback would be better happened in the first 30mins of first engagement.)


#### The key metrics


## What is the key user behavior




### What is the pattern of those players at their 1st day

- data visualization

### Which behavior highly correlated with this pattern


### Why is that behavior
- it's the major contribution of character ability
- players who invest more behave better than those who don't(they also know that system)


## A/B test

- show how many steps to get into 


