class AnalysisAgent:
    def calculate_exposure_change(self, yesterday_pct: float, today_pct: float):
        delta = today_pct - yesterday_pct
        direction = "up" if delta > 0 else "down"
        return f"{today_pct:.1f}% of AUM, {direction} from {yesterday_pct:.1f}%"
