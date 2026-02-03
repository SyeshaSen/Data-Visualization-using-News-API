# SUMMARY

## Ethics and Privacy

Please fill out this table about API keys used in code. (Some parts are already answered for you, and you may look at previous labs for help):

| Question | Answer |
| -------- | ------ |
| What type of information is shared? | API key |
| Who is the subject of the information? | The programmer / code that's making API calls |
| Who is the sender of the information? | The programmer |

| Who are the potential recipients of the information? | Intended recipient: the API server<br />Unintended recipient(s): YOUR ANSWER HERE | 
In case of accidentally pushing the API key to github, it can lead to other people who are not meant to view the key to see it.

| What principles govern the collection and transmission of the information? | YOUR ANSWER HERE |
Ensuring privacy and security are main motifs when transferring information. We must make sure that transferring private data such as API keys should not lead to unintended recipients receiving the data.


You may go back and edit your answers in the table as you answer these questions:
1. As we saw in Lab 5, large language models (LLMs) are trained on large parts of the internet. Are any popular LLMs trained on open source code like GitHub?
- Code Llama, StarCoder2 and DeepSeek-Coder are all designed for programming tasks and they use open source code like GitHub to better logic and syntax.

2. If a programmer accidentally pushes their API key to GitHub, who are at least two potential unintended recipients of this data?
- Open AI models that train based on open source data. 
- Anywone who can view a public repository

3. How might we design our code to minimize the number of unintended recipients of that information? How might we redesign APIs to minimize the number of unintended recipients?
- ensuring the proper use of gitignore can definetly help to prevent information that is not wanted to be shared from being shared.

---

## Citations

### Who did you work with and how?  
*Discussing the assignment with people not on your team is fine as long as you don't share code.*  
*Please include any people or other sources who helped you, and any students whom you helped.*  
*For each source, make sure to include how they helped you (or how you helped them).*  

* *Example: "I discussed the urgency ranking approach with classmate Alice Smith and clarified different ways to think about public safety priorities."*  
* *Example: "I showed Bob Lee my approach to filtering above-average cases and he suggested a more efficient pandas method."*  
* *If you did not talk to anybody about the assignment, please state that.*

*Answer:*

- N/A
---

### What resources did you use?  
*Please give specific URLs (not "Stack Overflow" or "Google") and state which ones were particularly helpful.*  

* *Example: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html – for understanding neighborhood aggregation methods*  
* *If you did not consult any external resources, please state that.*

*Answer:*

https://docs.python.org/3/library/unittest.mock.html
This helped me understand unit testing functions, specifically the MagicMock function

---

## Logistics

### Did you successfully implement everything that was requested?  
*Answer "Yes", or state here which parts did not work or which tests did not pass.*  

*Answer:*
no,

article repr 0/3
Tests passed: 0 / 1

❌ test_article.TestArticleReprS-20251023014255.test_repr
Traceback (most recent call last):
  File "/home/runner/_work/f25-hw4-SyeshaSen/f25-hw4-SyeshaSen/pawtograder-grading/tests/test_article.py", line 124, in test_repr
    self.assertEqual(repr(article), expected_repr)
AssertionError: "Article(title='Example Title', author='J[67 chars]Z' )" != 'Article(title=Example Title, author=John[58 chars]00Z)'
- Article(title='Example Title', author='John Doe', source='Example Source', publishedAt='2023-10-01T12:00:00Z' )
?               -             -         -        -         -              -              -                    --
+ Article(title=Example Title, author=John Doe, source=Example Source, publishedAt=2023-10-01T12:00:00Z)



### How long did the assignment take?  
*Rather than giving a range, if you are unsure, give the average of the range.*  

*Answer:*
This took me 5.5 hours

---

## Reflections  
*Give **one or more paragraphs** reflecting on your experience with the assignment, including answers to all of these questions:*  
* What was the most difficult part of the assignment?  
* What was the most rewarding part of the assignment?  
* What did you learn doing the assignment?  
* How did this assignment change your thinking about data analysis and social equity?
* Constructive and actionable suggestions for improving assignments, office hours, and lecture are always welcome.  

*Answer:*

I feel that the most difficult part of this assignment was writing test classes. I was not sure how to work with APIs properly, and although I was able to understand how to use them for the class implementations, testing them was a big challenge. The most rewarding aspect of the assignment was that I learned more about APIs, because I previously had not had much experience with this. I was able to learn more about what exactly API keys are, and why they are necessary to access the wanted information. Before this assignment, I did not really think about the importance of gitignore, but now I understand how important it is to make sure that certain things should not be committed. I think it is really important ethically to prevent private data, including API keys to be shared. To improve assigments/lectures, I would love if we had more homework assignments, but less lengthy and difficult ones. I think if we could have homework assignments after each lecture, going from very simple to a bit more complicated questions regarding the topics covered in lecture, it would help in creating a stronger foundation for all of the topics.
