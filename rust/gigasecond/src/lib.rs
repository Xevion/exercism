use time::PrimitiveDateTime as DateTime;

const GIGASECOND_IN_SECONDS: i64 = 1_000_000_000;

// Returns a DateTime one billion seconds after start.
pub fn after(start: DateTime) -> DateTime {
    start + time::Duration::seconds(GIGASECOND_IN_SECONDS)
}
