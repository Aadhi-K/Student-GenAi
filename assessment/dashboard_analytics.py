from database.test_result_collection import test_result_collection


class DashboardAnalytics:

    def get_dashboard_data(self, student_id):

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

        percentages = [
            r["percentage"]
            for r in results
        ]

        chart_data = []

        for index, result in enumerate(results, start=1):

            chart_data.append({
                "test": f"Test {index}",
                "percentage": result["percentage"]
            })

        return {
            "student_id": student_id,
            "tests_taken": len(results),
            "average_score": round(
                sum(percentages) / len(percentages),
                2
            ),
            "best_score": max(percentages),
            "lowest_score": min(percentages),
            "chart_data": chart_data
        }