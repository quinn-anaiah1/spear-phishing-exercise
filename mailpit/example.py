email_data = {
    "subject": "Entry-Level Software Developer Interview Guide",
    "body": """
**Introduction**

This guide provides suggested interview questions and potential answer perspectives for the Entry-Level Software Developer position. The goal is to assess both the candidate's behavioral attributes and technical skills. Remember to adapt these questions based on the specific candidate and the requirements of the role.

**I. Behavioral Questions (4 Questions)**

These questions aim to evaluate the candidate's soft skills, work ethic, and cultural fit.

1.  **Question:** "Tell me about a time you faced a challenging technical problem. How did you approach it, and what was the outcome?"
    * **Purpose:** Assesses problem-solving skills, resilience, and ability to learn.
    * **Desired Response:**
        * Clear articulation of the problem.
        * Structured approach (e.g., breaking down the problem, researching solutions, seeking help if needed).
        * Focus on the learning process, even if the initial solution wasn't successful.
        * Positive outcome or a clear understanding of what could have been done differently.
        * Example: "In my project [Project Name], I encountered [Specific Problem]. I started by [Action 1, e.g., isolating the issue]. Then, I [Action 2, e.g., researched similar problems online]. I also [Action 3, e.g., consulted with my mentor/professor]. Eventually, [Outcome, e.g., I resolved it by... / I learned that...]."

2.  **Question:** "Describe a situation where you had to work as part of a team. What was your role, and how did you contribute to the team's success?"
    * **Purpose:** Evaluates teamwork, communication, and collaboration skills.
    * **Desired Response:**
        * Specific example of a team project (academic or personal).
        * Clear description of their role and responsibilities.
        * Emphasis on positive contributions (e.g., sharing knowledge, meeting deadlines, helping others).
        * Ability to discuss challenges and how the team overcame them.
        * Example: "In my group project for [Course Name], we were tasked with [Project Goal]. My role was [Specific Role]. I contributed by [Contribution 1, e.g., developing the database schema], [Contribution 2, e.g., communicating regularly with the team], and [Contribution 3, e.g., helping a teammate with a difficult concept]. We successfully [Team Achievement] because [Reason for Success]."

3.  **Question:** "Why are you interested in software development, and what excites you about this field?"
    * **Purpose:** Assesses passion, motivation, and long-term interest in software development.
    * **Desired Response:**
        * Genuine enthusiasm for technology and software.
        * Specific aspects of software development that they find exciting (e.g., problem-solving, creativity, building things, continuous learning).
        * Alignment of their interests with the company's mission or the specific role.
        * Example: "I've always been fascinated by how software can [Impact, e.g., solve problems, improve lives]. I'm particularly excited about [Specific Area, e.g., the potential of AI, the challenges of distributed systems] because [Reason]. I'm drawn to this field because of [Reason 1, e.g., the constant learning] and [Reason 2, e.g., the opportunity to build things that people use]."

4.  **Question:** "Where do you see yourself in five years?"
    * **Purpose:** Gauges career goals, ambition, and commitment to growth.
    * **Desired Response:**
        * Realistic and ambitious goals related to software development.
        * Desire to grow technically and professionally.
        * Interest in contributing to the company's success.
        * Example: "In five years, I hope to have developed a strong foundation as a software developer, contributing to meaningful projects at a company like this one. I'm eager to expand my skills in [Specific Technology/Area] and take on increasing responsibilities. I'd also like to be involved in mentoring junior developers or contributing to team leadership in some way."

**II. Technical Questions (5 Questions)**

These questions assess the candidate's fundamental programming knowledge, problem-solving abilities, and understanding of software development concepts.

1.  **Question:** "Explain the difference between a 'stack' and a 'queue' data structure. Provide a real-world example of each."
    * **Purpose:** Evaluates understanding of basic data structures.
    * **Desired Response:**
        * Clear definitions of stack (LIFO - Last In, First Out) and queue (FIFO - First In, First Out).
        * Accurate real-world examples.
        * Example: "A stack is like a stack of plates; the last plate you put on is the first one you take off. A real-world example is the undo function in a text editor. A queue is like a line at a ticket counter; the first person in line is the first one served. A real-world example is a print queue."

2.  **Question:** "What is Object-Oriented Programming (OOP)? Explain the four main principles of OOP."
    * **Purpose:** Assesses knowledge of OOP concepts.
    * **Desired Response:**
        * Correct definition of OOP.
        * Explanation of the four principles:
            * Encapsulation: Bundling data and methods that operate on that data.
            * Inheritance: Creating new classes from existing classes.
            * Polymorphism: The ability of an object to take on many forms.
            * Abstraction: Simplifying complex reality by modeling classes appropriate to the problem.
        * Example: "OOP is a programming paradigm based on the concept of 'objects' that contain data and code. The four main principles are: Encapsulation, which hides the internal state of an object; Inheritance, which allows classes to inherit properties and behaviors from parent classes; Polymorphism, which allows objects of different classes to be treated as objects of a common type; and Abstraction, which focuses on essential features and hides unnecessary details."

3.  **Question:** "Write a function (in the language of their choice, e.g., Python, Java, JavaScript) to reverse a string."
    * **Purpose:** Evaluates coding skills and problem-solving ability.
    * **Desired Response:**
        * Correct and efficient code.
        * Clear explanation of the code.
        * Ability to handle edge cases (e.g., empty string).
        * Example (Python):
            ```python
            def reverse_string(s):
                \"\"\"Reverses a string.

                Args:
                    s: The input string.

                Returns:
                    The reversed string.
                \"\"\"
                if not s:  # Handle empty string
                    return \"\"
                return s[::-1]  # Efficient string slicing
            ```
            or
            ```python
            def reverse_string(s):
                if not s:
                    return \"\"
                reversed_string = \"\"
                for i in range(len(s) - 1, -1, -1):
                    reversed_string += s[i]
                return reversed_string
            ```

4.  **Question:** "Explain the difference between '==' and '===' in JavaScript (or the equivalent comparison operators in another language)."
    * **Purpose:** Tests understanding of language-specific concepts and nuances.
    * **Desired Response:**
        * Clear explanation of the difference between loose equality (`==`) and strict equality (`===`).
        * Understanding of type coercion.
        * Example (JavaScript): "In JavaScript, `==` compares values after type coercion, meaning it might convert the types of the operands before comparing them. `===` compares values without type coercion; it checks if both the values and the types are the same. For example, `5 == '5'` is true, but `5 === '5'` is false."

5.  **Question:** "What is a database index, and why is it important?"
    * **Purpose:** Assesses knowledge of database concepts.
    * **Desired Response:**
        * Correct definition of a database index.
        * Explanation of how it improves query performance.
        * Understanding of the trade-offs (e.g., increased storage space, slower writes).
        * Example: "A database index is a data structure that improves the speed of data retrieval operations on a database table. It's like an index in a book; it allows the database to quickly locate specific rows without having to search the entire table. Indexes are important for improving query performance, especially for large tables, but they can increase storage space and slow down data modification operations (inserts, updates, deletes)."
    """
}