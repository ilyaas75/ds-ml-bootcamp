Practical Assignment: Data Foundations for Machine Learning
Research Paper – Student Daily Study Habits Dataset
1. Title & Collection Method

Title:
Analysis of Student Daily Study Habits for Machine Learning Prediction

Collection Method:
Dataset-kan waxaa laga ururiyey arday jaamacadeed iyadoo la isticmaalayo:

Survey & questionnaire (Google Form iyo su’aalo toos ah).

Ardaydu waxay bixiyeen xog ku saabsan:

Da’dooda

Saacadaha ay maalin kasta wax bartaan

Isticmaalka internet-ka

Hurdo

Darajada imtixaanka

Waxaa la ururiyey 60 arday, taasoo ka badan shuruudda 50 samples.

2. Description of Features & Labels
Input Variables (Features X)
Feature	Description
Age	Da’da ardayga (years)
Study_Hours	Saacadaha waxbarasho maalintii
Sleep_Hours	Saacadaha hurdo
Internet_Hours	Saacadaha internet-ka
Attendance	Heerka imaanshaha fasalka (%)
Output Variable (Label y)
Label	Description
Exam_Score	Dhibcaha imtixaanka (%)

Goal ML:
In la saadaaliyo Exam_Score iyadoo la isticmaalayo features-ka kore.

3. Dataset Structure

Number of rows: 60 arday

Number of columns: 6 (5 features + 1 label)

Sample Data (10 rows)
Age	Study_Hours	Sleep_Hours	Internet_Hours	Attendance	Exam_Score
20	3	7	4	80	65
22	5	6	3	90	78
19	2	8	5	70	60
21	6	6	2	95	85
23	4	7	3	88	75
20	1	5	6	60	50
22	7	7	2	96	90
19	3	6	4	75	68
24	5	8	3	85	80
21	4	7	5	82	72
4. Quality Issues in the Dataset

Dataset-kan wuxuu leeyahay dhibaatooyin real-world ah:

Missing values:
Arday qaar ma sheegin saacadaha hurdo ama internet.

Inconsistent data:
Qaar waxay qoreen “five hours” halkii ay ka qori lahaayeen 5.

Outliers:
Arday sheegay 0 saacadood hurdo ama 15 saacadood internet, taas oo aan caadi ahayn.

Imbalance:
Ardayda leh scores sare ayaa ka badan kuwa hoose.

Dhibaatooyinkan waxaa lagu xallin doonaa Lesson 3 preprocessing:

Filling missing values

Encoding text to numbers

Scaling features

Removing outliers

5. Use Case in Machine Learning

Dataset-kan waxaa loo isticmaali karaa dhowr nooc ML:

1. Regression

Goal: In la saadaaliyo Exam_Score.

Models: Linear Regression, Random Forest Regressor.

Benefit: Fahamka sida study hours iyo hurdo u saameeyaan dhibcaha.

2. Classification

Exam score waxaa loo qaybin karaa:

Pass (≥60)

Fail (<60)

Model-ku wuxuu saadaalin karaa ardaygu wuu gudbi doonaa mise maya.

3. Clustering

Ardayda waxaa loo kala saari karaa:

Hard-working

Average

Low-effort

Tani waxay caawin kartaa macallimiinta iyo jaamacadaha si ay u taageeraan ardayda u baahan caawimaad.

Conclusion

Research-kan wuxuu muujinayaa:

Sida real-world dataset loo ururiyo.

Dhibaatooyinka xogta dhabta ah.

Sida dataset-ku ugu diyaarsan yahay Machine Learning preprocessing iyo modeling.

Dataset-kani wuxuu noqon karaa tallaabada ugu horreysa ee dhismaha student performance prediction system.