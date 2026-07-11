"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging
import unittest


def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    # Створення та налаштування логера
    logging.basicConfig(
        filename="login_system.log",
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
    )
    logger = logging.getLogger("log_event")

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)


# tests перший варіант, теоретично можна покращити та прибрати дублювання коду


class TestLog(unittest.TestCase):
    def test_log_success(self):
        with self.assertLogs("log_event", level="INFO") as logs:
            log_event("dara", "success")

        self.assertEqual(logs.records[0].levelname, "INFO")
        self.assertEqual(
            logs.records[0].getMessage(),
            "Login event - Username: dara, Status: success",
        )

    def test_log_expired(self):
        with self.assertLogs("log_event", level="WARNING") as logs:
            log_event("dara", "expired")
        self.assertEqual(logs.records[0].levelname, "WARNING")
        self.assertEqual(
            logs.records[0].getMessage(),
            "Login event - Username: dara, Status: expired",
        )

    def test_log_failed(self):
        with self.assertLogs("log_event", level="ERROR") as logs:
            log_event("dara", "failed")
        self.assertEqual(logs.records[0].levelname, "ERROR")
        self.assertEqual(
            logs.records[0].getMessage(), "Login event - Username: dara, Status: failed"
        )

    def test_log_unknown_status_as_error(self):
        with self.assertLogs("log_event", level="ERROR") as logs:
            log_event("dara", "unknown")
        self.assertEqual(logs.records[0].levelname, "ERROR")
        self.assertEqual(
            logs.records[0].getMessage(),
            "Login event - Username: dara, Status: unknown",
        )


if __name__ == "__main__":
    unittest.main()
