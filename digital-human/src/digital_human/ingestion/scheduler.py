from __future__ import annotations

from typing import Callable


class IngestionScheduler:
    def __init__(self) -> None:
        self._scheduler = None

    def start(self, interval_minutes: int, job: Callable[[], None]) -> None:
        from apscheduler.schedulers.background import BackgroundScheduler

        self._scheduler = BackgroundScheduler()
        self._scheduler.add_job(job, "interval", minutes=interval_minutes)
        self._scheduler.start()

    def shutdown(self) -> None:
        if self._scheduler:
            self._scheduler.shutdown(wait=False)
