# Exercises — HTTP Methods And Status Codes

Lesson `m01l02` · [Watch](https://learnsome.tech/courses/apis-course/watch?lesson=m01l02)

## Exercise 1: Break it, then fix it yourself

1. Apply the fault: patch -p1 < breakages/01-missing-404/break.patch
2. Restart the server and confirm that GET /tasks/999 answers 200 with {}
3. Repair app.py by hand so a missing task is a 404 problem document
4. Grade it: python3 contract_test.py -k NotFound

> **Hint**: The route reads the row first. The only question is what it returns when there is no row.


---

© LearnSome.tech · support@iwantto.learnsome.tech
