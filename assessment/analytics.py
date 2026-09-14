from database.test_result_collection import (
    test_result_collection
)


class Analytics:

    def subject_wise_performance(
        self,
        student_id
    ):

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

        subjects = {}

        for result in results:

            subject = result["subject"]

            if subject not in subjects:
                subjects[subject] = []

            subjects[subject].append(
                result["percentage"]
            )

        analytics = {}

        for subject, scores in subjects.items():

            analytics[subject] = round(
                sum(scores) / len(scores),
                2
            )

        return analytics