# OPTIMIZATION-MODEL

**COMPANY NAME**: CODTECH IT SOLUTIONS

**NAME**: AMIT GAJANAN PADMAN

**INTERN ID**:CT08JVQ

**DOMAIN NAME**:DATA SCIENCE

**BATCH DURATION**:JANUARY 5th,2025 TO FEBRUARY 5th,2025

**MENTOR NAME**:NEELA SANTHOSH

# DESCRIPTION

**TOOLS USED**: google colab, VScode, pulp package , python language ,  etc

problem: Production Optimization for a factory.

A factory produces two products: A and B.
Each product requires a certain amount of time in two machines: Machine 1 and Machine 2.
The profit per unit for products A and B is $40 and $50, respectively.
The available machine time is as follows:
Machine 1: 100 hours
Machine 2: 80 hours
Each unit of product A requires:
2 hours on Machine 1
1 hour on Machine 2
Each unit of product B requires:
1 hour on Machine 1
2 hours on Machine 2
Objective: Maximize profit while adhering to the machine time constraints.

formula:
1) Decision Variables:
    let x1 and x2 be the number of units produed of products A and B, respectively
2) Objective Function:
    Maximize profit Z:
       Z = 40x1 + 50x2
3) Constraints:
   Machine 1 : 2x1 + x2 < 100
   Machine 2 : x1 + 2x2 < 80
   Non-negative : x1,x2 > 0  

​
