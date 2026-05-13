# Chapter 4.1.2: Datasets, Features, and Labels

Once we say a system learns from data, the next question is:

> what exactly is the data?

Machine learning usually starts with a **dataset**.

But not all data looks the same. Understanding how to structure and prepare data is crucial for successful learning.

---

## 1. The Dataset: Your Learning Foundation

A dataset is a collection of examples that the machine learns from.

In supervised learning, it often looks like:

`D = {(x₁, y₁), (x₂, y₂), ..., (xₙ, yₙ)}`

Each pair contains:
- `xᵢ` = input (what we observe)
- `yᵢ` = target (what we want to predict)

**Real Example:**
Predicting house prices:
- `x₁ = [120, 3, 10, 5]` (size, rooms, age, distance to city)
- `y₁ = 250000` (price in dollars)

So the dataset is a record of past cases where we know both the question and the answer.

---

## 2. Features: The Language of Data

A **feature** is a measurable property of an example.

Features are how we describe the world to the machine.

### House Price Example
For predicting house prices, features might include:
- **Size:** 120 square meters
- **Rooms:** 3 bedrooms
- **Age:** 10 years old
- **Location:** 5 km from city center
- **Garage:** Yes/No
- **School rating:** 8/10

So one house becomes: `x = [120, 3, 10, 5, 1, 8]`

### Types of Features

**Numerical Features:**
- Continuous: height, weight, temperature
- Discrete: number of children, age in years

**Categorical Features:**
- Nominal: color (red, blue, green)
- Ordinal: education level (high school < college < graduate)

**Binary Features:**
- Yes/No questions: has_garage, is_married
- Often encoded as 0/1

---

## 3. Labels: What We Want to Learn

A **label** is the answer we want the model to predict.

Labels define the learning task:

### Classification Labels
Predicting categories:
- **Email spam detection:** spam or not spam
- **Medical diagnosis:** healthy, flu, pneumonia
- **Image recognition:** cat, dog, bird

### Regression Labels
Predicting numbers:
- **House prices:** $250,000
- **Temperature:** 23.5°C
- **Stock prices:** $45.67

### Multi-label Tasks
Predicting multiple things at once:
- **Movie genres:** comedy AND romance
- **Medical symptoms:** fever AND cough AND headache

---

## 4. Real-World Example: Student Performance

Let's build a complete dataset for predicting student exam scores:

| Study Hours | Attendance % | Previous GPA | Sleep Hours | Final Score |
|-------------|--------------|--------------|-------------|-------------|
| 10          | 95           | 3.2          | 7           | 85          |
| 5           | 80           | 2.8          | 6           | 72          |
| 15          | 98           | 3.8          | 8           | 92          |
| 2           | 60           | 2.1          | 5           | 58          |
| 12          | 90           | 3.5          | 7           | 88          |

**Features:** Study Hours, Attendance %, Previous GPA, Sleep Hours
**Label:** Final Score

---

## 5. The Feature Engineering Challenge

Raw data rarely comes in perfect form. We often need to create better features.

### Example: Text Analysis
**Raw text:** "This movie is absolutely amazing!"

**Possible features:**
- Word count: 5
- Exclamation marks: 1
- Positive words: 2 ("amazing", "absolutely")
- Average word length: 5.2
- Contains "amazing": 1

### Example: Time Series
**Raw data:** Daily temperatures

**Engineered features:**
- 7-day moving average
- Temperature change from yesterday
- Day of week
- Season (spring, summer, fall, winter)

---

## 6. Structured vs Unstructured Data

### Structured Data
Data that fits nicely into rows and columns:
- **Database records:** customer info, sales data
- **Spreadsheets:** financial data, survey results
- **Sensor readings:** temperature, pressure, speed

**Advantage:** Features are already clear

### Unstructured Data
Data that doesn't fit into neat tables:
- **Images:** pixels, but what features matter?
- **Text:** words, but how to represent meaning?
- **Audio:** sound waves, but how to capture patterns?
- **Video:** moving images with sound

**Challenge:** Must extract meaningful features first

---

## 7. Data Quality Issues

### Missing Values
What if some information is missing?

| Name | Age | Income | Education |
|------|-----|--------|-----------|
| John | 25  | 50000  | College   |
| Mary | ?   | 60000  | Graduate  |
| Bob  | 35  | ?      | High School|

**Solutions:**
- Remove incomplete examples
- Fill with average/most common value
- Use special "missing" category

### Outliers
Extreme values that don't fit the pattern:
- House price: $100,000, $120,000, $110,000, $5,000,000
- The $5M house might be an error or special case

### Inconsistent Data
- Same thing written differently: "USA", "United States", "US"
- Different units: meters vs feet, Celsius vs Fahrenheit

---

## 8. Training, Validation, and Test Sets

We don't use all data the same way:

### Training Set (60-70%)
Used to teach the model
- Model sees these examples during learning
- Adjusts weights based on these examples

### Validation Set (15-20%)
Used to tune model settings
- Test different hyperparameters
- Choose best model configuration
- Model doesn't learn from these, but we use them to make decisions

### Test Set (15-20%)
Used for final honest evaluation
- Model never sees these during development
- Gives unbiased estimate of real-world performance
- Only use once at the very end

**Why split?** If we test on training data, we might fool ourselves into thinking the model is better than it really is.

---

## 9. Data Size Matters

### Small Data (< 1,000 examples)
- Simple models work better
- Risk of overfitting
- Every example is precious

### Medium Data (1,000 - 100,000 examples)
- Most classical ML algorithms work well
- Can try more complex models
- Good balance of bias and variance

### Big Data (> 100,000 examples)
- Complex models become viable
- Deep learning becomes possible
- Computational efficiency matters more

---

## 10. Connection to the Lineage

Data preparation connects to everything:

**From Statistics (Chapter 3):**
- Samples represent populations
- Features are random variables
- Labels follow probability distributions

**To Model Training:**
- Quality of features limits model performance
- "Garbage in, garbage out"
- Good features can make simple models work well

**Key Insight:** Often, 80% of machine learning work is data preparation, not algorithm selection.

---

## 11. What Comes Next

Once we have clean data with good features and labels, the next question is:

> how does the model actually learn from this data?

That leads us to **loss functions, training, and optimization** - the mathematical engine that makes learning possible.
