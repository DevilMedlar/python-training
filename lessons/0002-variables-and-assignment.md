# Record 0002: variables and assignment

| Field | Recorded value |
| --- | --- |
| Recorded date | 2026-09-09 |
| Entry type | Lesson issued with the accompanying tutor response |
| Prerequisite | Record 0001: first script and Git checkpoint complete |
| Lesson status | Introduced and assigned; awaiting learner submission |
| Exercise file | variables.py, to be created by the learner in the repository root |
| Assessment status | No variable-related strength or weakness inferred before reviewing the submission |

**Learning targets.**

- Assign integer values to descriptive names.
- Read a variable in an expression or a print call.
- Follow assignment and reassignment in execution order.
- Explain when a stored total is calculated and when it must be recalculated.
- Use lowercase names, underscores between words, and spaces around assignment and addition.

A variable is a name that refers to a Python object. For these examples the objects are integer values. In a simple assignment such as apples = 4, Python evaluates the expression on the right and binds the name on the left to the resulting object.

An assignment does not print a result. A print call is used to display a value in the script.

Read this worked example:

```python
apples = 4
oranges = 3
fruit_count = apples + oranges
apples = 10

print(apples)
print(fruit_count)
```

Expected output:

```text
10
7
```

fruit_count is calculated when its assignment runs, using apples equal to 4 and oranges equal to 3. Later, apples is reassigned to 10. fruit_count still refers to the previously calculated value, 7. To calculate an updated total, execute fruit_count = apples + oranges again; at that point it produces 13.

print(apples) reads the current value associated with the name. print("apples") prints the literal word. Python's [assignment reference](https://docs.python.org/3.14/reference/simple_stmts.html#assignment-statements) and [introductory tutorial](https://docs.python.org/3.14/tutorial/introduction.html#numbers) support this lesson.

Use descriptive lowercase names such as fruit_count. Underscores separate words in that naming style. Python names are case-sensitive, so apples and Apples are different names. Put a space on each side of = and + in these examples. See [PEP 8 naming and spacing](https://peps.python.org/pep-0008/).

**Learner assignment.**

After bringing the lesson records into the Codespace with the explained pull command, create variables.py in the project root and implement these steps yourself:

1. Assign 6 to pencils.
2. Assign 4 to pens.
3. Calculate item_count by adding those two variables, then print item_count.
4. Reassign pencils to 9.
5. Print pencils, then print item_count, each using its own print call.
6. Recalculate item_count using the current values of pencils and pens, then print item_count again.

Before running, predict the four output lines. Save the file and run:

```bash
python3 variables.py
```

Submit the code, the predicted output, the actual output, and a short explanation of why the stored total stays the same until its assignment runs again. The tutor supplies the worked fruit example, not the solution to this exercise.

**Review criteria and next decision.**

| Criterion | What the next review must establish |
| --- | --- |
| Assignment | Values are assigned before the names are read |
| Reassignment | pencils is updated at the required point in execution |
| Expressions | item_count is calculated from variable names |
| Order and output | Four print calls appear in the required order |
| Reasoning | Learner explains the earlier total and the recalculated total |
| Style | Descriptive names, spaces around operators, appropriate top-level alignment |

Compare the learner's prediction with actual behavior; do not equate correct output alone with understanding. If assignment timing is unclear, explain it again and assign a small different example. If it is clear, continue with variable updates, naming, and basic debugging, then expand numeric and text operations. Update the assessment in a new numbered record, preserving this one.

The next small exercise does not automatically require a commit or push. Review pasted work and choose the next meaningful Git checkpoint after seeing progress.
