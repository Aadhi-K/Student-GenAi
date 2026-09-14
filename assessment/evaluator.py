from database.mock_test_collection import mock_test_collection
from bson import ObjectId


class TestEvaluator:

    def evaluate(self, test_id, student_answers):

        test = mock_test_collection.find_one(
            {"_id": ObjectId(test_id)}
        )

        if not test:
            return None

        questions = test["questions"]

        score = 0
        wrong_questions = []

        for i, question in enumerate(questions):

            if i < len(student_answers):

                student_answer = student_answers[i]

                if (
                    student_answer.strip().lower()
                    ==
                    question["correct_answer"].strip().lower()
                ):
                    score += 1

                else:

                    wrong_questions.append({
                        "question": question["question"],
                        "student_answer": student_answer,
                        "correct_answer": question["correct_answer"]
                    })

        total = len(questions)

        percentage = round(
            (score / total) * 100,
            2
        )

        return {
            "subject": test["subject"],
            "score": score,
            "total": total,
            "percentage": percentage,
            "wrong_questions": wrong_questions
        }