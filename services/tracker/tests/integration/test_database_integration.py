class TestDatabaseIntegration:
    def test_create_tables(self):
        """
        Test that the session.py file creates the database and tables when ran

        Test Cases:
        - When the session.py file is ran, the tracker.db file is created where expected
        - More than one table is created in the tracker.db file
        """
        ...

    def test_database_integrity(self):
        """
        Test the relationships between the tables and ensure that they are correctly being built

        Test Cases:
            - Benchmark table is created and a row can be pushed to the database
            - Task table is created and a row can be pushed to the database
            - EvaluationResult table is created and a row can be pushed to the database
        """
        ...

    def test_end_to_end(self):
        """
        Test the end to end flow when using database with a benchmark service

        Test Cases:
            - Create a benchmark row to initiate a benchmark
            - Apply concurrency to tasks and ensure that the tasks are correctly being added to the database
            - As evaluation results come in, ensure that we are correclty adding them to the database
        """
        ...
