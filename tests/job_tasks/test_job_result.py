import unittest

from svg_concat.job_tasks.job_result import JobResult


class JobResultTests(unittest.TestCase):
    def setUp(self):
        self.test_result = JobResult()


class AddMessageTests(JobResultTests):
    def test_added_message_is_in_list(self):
        # Arrange
        expected_result = ("Testing",)

        # Act
        self.test_result.add_message("Testing")

        # Assert
        self.assertEqual(expected_result, self.test_result.messages)

    def test_result_is_still_success(self):
        # Act
        self.test_result.add_message("Testing")

        # Assert
        self.assertTrue(self.test_result.is_success)

    def test_result_is_not_fatal(self):
        # Act
        self.test_result.add_message("Testing")

        # Assert
        self.assertFalse(self.test_result.is_fatal)


class FailTests(JobResultTests):
    def test_added_message_is_in_list(self):
        # Arrange
        expected_result = ("Testing",)

        # Act
        self.test_result.fail("Testing")

        # Assert
        self.assertEqual(expected_result, self.test_result.messages)

    def test_result_is_not_success(self):
        # Act
        self.test_result.fail("Testing")

        # Assert
        self.assertFalse(self.test_result.is_success)

    def test_result_is_not_fatal(self):
        # Act
        self.test_result.fail("Testing")

        # Assert
        self.assertFalse(self.test_result.is_fatal)


class FatalTests(JobResultTests):
    def test_added_message_is_in_list(self):
        # Arrange
        expected_result = ("Testing",)

        # Act
        self.test_result.fatal_fail("Testing")

        # Assert
        self.assertEqual(expected_result, self.test_result.messages)

    def test_result_is_not_success(self):
        # Act
        self.test_result.fatal_fail("Testing")

        # Assert
        self.assertFalse(self.test_result.is_success)

    def test_result_is_fatal(self):
        # Act
        self.test_result.fatal_fail("Testing")

        # Assert
        self.assertTrue(self.test_result.is_fatal)


if __name__ == '__main__':
    unittest.main()
