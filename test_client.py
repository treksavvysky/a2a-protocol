from client_server import A2AClient

client_b = A2AClient(base_url="http://localhost:8000", agent_id="agentB")
client_a = A2AClient(base_url="http://localhost:8000", agent_id="agentA")

print("Sending message from A to B...")
sent_msg = client_a.send(to="agentB", type="command", payload={"task": "do_something"})
print(f"Sent message: {sent_msg}")

print("\nFetching messages for B...")
messages = client_b.fetch()
print(f"Fetched messages: {messages}")

assert len(messages) == 1
assert messages[0].sender == "agentA"
assert messages[0].payload == {"task": "do_something"}

print("\nFetching messages for B again...")
messages_again = client_b.fetch()
print(f"Fetched messages again: {messages_again}")

assert len(messages_again) == 0

print("\nTest passed!")
