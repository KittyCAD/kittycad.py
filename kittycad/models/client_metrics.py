from typing import Optional

from .base import KittyCadBaseModel


class ClientMetrics(KittyCadBaseModel):
    """ClientMetrics contains information regarding the state of the peer."""

    rtc_frame_height: Optional[int] = None

    rtc_frame_width: Optional[int] = None

    rtc_frames_decoded: Optional[int] = None

    rtc_frames_dropped: Optional[int] = None

    rtc_frames_per_second: Optional[int] = None

    rtc_frames_received: Optional[int] = None

    rtc_freeze_count: Optional[int] = None

    rtc_jitter_sec: Optional[float] = None

    rtc_keyframes_decoded: Optional[int] = None

    rtc_packets_lost: Optional[int] = None

    rtc_pause_count: Optional[int] = None

    rtc_pli_count: Optional[int] = None

    rtc_stun_rtt_sec: Optional[float] = None

    rtc_total_freezes_duration_sec: Optional[float] = None

    rtc_total_pauses_duration_sec: Optional[float] = None
