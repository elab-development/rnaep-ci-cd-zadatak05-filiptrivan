"""Integration test: prava interakcija sa Redis-om."""


def test_redis_set_and_get():
    from database import redis

    redis.set("integration:test", "ok")
    assert redis.get("integration:test") == "ok"
    redis.delete("integration:test")
