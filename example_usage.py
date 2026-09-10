from client import SagaOrchestrator

def main():
    print("=== Testing Saga Pattern Orchestrator ===")
    saga = SagaOrchestrator()
    ctx = {"balance": 100, "hotel_booked": False}

    def pay(c):
        c["balance"] -= 50
        return True
    def refund(c):
        c["balance"] += 50
    def book_hotel(c):
        return False # simulate network error

    saga.add_step("Payment", pay, refund)
    saga.add_step("Hotel", book_hotel, lambda c: None)

    ok, msg = saga.execute(ctx)
    print("Saga execution result:", ok, msg)
    assert not ok
    assert ctx["balance"] == 100
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
