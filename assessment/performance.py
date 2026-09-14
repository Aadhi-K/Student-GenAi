from database.test_result_collection import test_result_collection


class PerformanceAnalyzer:

    def get_student_performance(self, student_id):

        results = list(
            test_result_collection.find(
                {"student_id": student_id},
                {"_id": 0}
            )
        )

        if not results:
            return {
                "message": "No test history found"
            }

        scores = [
            result["percentage"]
            for result in results
        ]

        return {
            "student_id": student_id,
            "tests_taken": len(results),
            "average_score": round(sum(scores) / len(scores), 2),
            "best_score": max(scores),
            "lowest_score": min(scores)
        }