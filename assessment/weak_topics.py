from database.test_result_collection import (
    test_result_collection
)


class WeakTopicsAnalyzer:

    def get_weak_topics(self, student_id):

        results = list(
            test_result_collection.find(
                {"student_id": student_id},
                {"_id": 0}
            )
        )

        if not results:
            return {
                "student_id": student_id,
                "weak_topics": []
            }

        weak_topics = []

        for result in results:

            topics = result.get(
                "weak_topics",
                []
            )

            weak_topics.extend(topics)

        weak_topics = list(
            set(weak_topics)
        )

        return {
            "student_id": student_id,
            "weak_topics": weak_topics
        }