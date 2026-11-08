"""Tests hors ligne de la logique de lecture (aucun appel à Twitch).

Lancer : python -m unittest test_twitch_points -v
"""
import json
import unittest
from datetime import datetime, timezone

import twitch_points as tp


def message(kind, message_id, payload=None, timestamp="2026-11-02T18:00:00.123456789Z"):
    return json.dumps({
        "metadata": {"message_id": message_id, "message_type": kind,
                     "message_timestamp": timestamp},
        "payload": payload or {},
    })


class ParseTimestamp(unittest.TestCase):
    def test_nine_digit_fraction(self):
        self.assertEqual(
            tp.parse_ts("2026-11-02T18:00:00.123456789Z"),
            datetime(2026, 11, 2, 18, 0, 0, 123456, tzinfo=timezone.utc),
        )

    def test_no_fraction(self):
        self.assertEqual(
            tp.parse_ts("2026-11-02T18:00:00Z"),
            datetime(2026, 11, 2, 18, 0, 0, tzinfo=timezone.utc),
        )

    def test_empty(self):
        self.assertIsNone(tp.parse_ts(None))

    def test_delay(self):
        now = datetime(2026, 11, 2, 18, 0, 1, tzinfo=timezone.utc)
        self.assertAlmostEqual(tp.delay_ms("2026-11-02T18:00:00Z", now), 1000.0)


class ParseMessage(unittest.TestCase):
    def test_duplicate_detection(self):
        seen = set()
        first = tp.parse_message(message("notification", "abc"), seen)
        second = tp.parse_message(message("notification", "abc"), seen)
        self.assertFalse(first["duplicate"])
        self.assertTrue(second["duplicate"])

    def test_types_and_payload(self):
        seen = set()
        welcome = tp.parse_message(
            message("session_welcome", "w1", {"session": {"id": "S1"}}), seen)
        self.assertEqual(welcome["type"], "session_welcome")
        self.assertEqual(welcome["payload"]["session"]["id"], "S1")

    def test_missing_metadata(self):
        parsed = tp.parse_message("{}", set())
        self.assertEqual(parsed["type"], "unknown")
        self.assertFalse(parsed["duplicate"])


class Parser(unittest.TestCase):
    def test_boolean_options(self):
        args = tp.build_parser().parse_args(["reward-update", "R1", "--paused", "true"])
        self.assertIs(args.paused, True)
        self.assertIsNone(args.enabled)

    def test_skip_queue_flag(self):
        args = tp.build_parser().parse_args(
            ["reward-create", "--title", "t", "--skip-queue"])
        self.assertTrue(args.skip_queue)

    def test_mask_never_returns_full_token(self):
        self.assertEqual(tp.mask("abcdefghij"), "abcd…")


if __name__ == "__main__":
    unittest.main()
