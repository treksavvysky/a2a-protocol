# Internal Agent-to-Agent (A2A) Protocol

This document describes our in-house A2A protocol, built incrementally from simple foundations to advanced features. Follow each section in order to understand and implement the protocol.

---

## 1. Introduction

Our A2A protocol enables autonomous agents to exchange structured messages. We start with the minimal viable design and layer in security, scalability, and observability as needed.

---

## 2. Core Messaging

### 2.1 Basic Message Schema

Every message is JSON with the following fields:

```json
{
  "sender":   "agentA",
  "recipient": "agentB",
  "timestamp": "2025-05-30T12:00:00Z",
  "type":     "command|response|status",
  "payload":  { /* custom data */ }
}
```

### 2.2 Transport (Synchronous HTTP)

* **POST /messages**: Send a message. Body is the JSON schema above.
* **GET /messages?recipient={agentId}**: Retrieve pending messages.

This simple request-response model lets agents interact directly with minimal dependencies.

---

## 3. Security (Optional Add-on)

When ready to secure channels:

1. **Mutual TLS (mTLS)** for endpoint authentication.
2. **JWTs** for agent identity and permissions.

These features can be enabled in configuration without changing the core schema or endpoints.

---

## 4. Asynchronous Delivery

To decouple sender and receiver:

1. Integrate a message broker (e.g., RabbitMQ, Kafka).
2. Use **`publish(topic, message)`** and **`subscribe(topic)`** instead of HTTP calls.
3. Attach a **`correlation_id`** header to track request-response cycles.

---

## 5. Message Prioritization & Reliability

Add headers for:

* **`X-Priority`**: integer (1=highest).
* **Retry policies**: configurable retries and exponential backoff.
* **Dead-letter queue**: capture undeliverable messages.

---

## 6. Versioning & Compatibility

1. Tag each message with **`schema_version`**.
2. Agents negotiate supported versions at startup.
3. Maintain backward compatibility by supporting previous schema handlers.

---

## 7. Service Discovery & Health

Agents may expose:

* **`/health`**: returns status `{ "status": "ok" }`.
* **`/discover`**: lists available agents and capabilities.

Use a lightweight registry or DNS-based discovery.

---

## 8. Error Handling & Observability

Standard error response:

```json
{
  "error_code": "INVALID_SCHEMA",
  "message":    "Description of issue"
}
```

Integrate with tracing (e.g., OpenTelemetry) for end-to-end visibility.

---

## 9. Quick Start

1. **Install**

   ```bash
   pip install internal-a2a
   ```
2. **Configure**

   ```yaml
   transport: http   # or "broker"
   security: none    # or "mtls", "jwt"
   broker_url:       # if using broker
   ```
3. **Run Agent**

   ```bash
   a2a-agent serve --config a2a_config.yaml
   ```

---

## 10. Example Usage

```python
from internal_a2a import A2AClient
client = A2AClient(agent_id="agentA")
resp = client.send(
    to="agentB",
    type="command",
    payload={"task": "analyze_data"}
)
print(resp.payload)
```

---

## Contributing

Follow our contribution guide. Add new features by layering on top of existing sections. Ensure unit tests cover all new behaviors.

---

## License

MIT License. See [LICENSE](LICENSE).
