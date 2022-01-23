# System Design: Messenger/Chat Servive

### Notes
- FB Messenger is different from Whatsapp/Signal
    - FB: server store all the messages and have access to them
    - Signal: server store messages that not read yet
- Key features/topics
    - 1to1 chatting
    - status update: person (online/offline); messages (sent/read)
    - message media types
    - database
    - security
    - search
- Key layers/components
    - client side (user, APIs)
        - HTTP protocol vs Websocket protocol vs BOSH vs Long Poll Http
        - Websocket keep reuse the same session and connection
        - Websocket don't automatically recover, so must impl on our own (client side handling is critical)
        - request-response vs event-driven (publish w. existing channel)
    - LB (router, API Gateway)
        - heath check --> deep health check of the server (blackhole)
    - Backend Server in Nodes or Cells
    - Database (Cassandra)
        - message to offline user
        - UserTable (user1, user2, conversationId, cryptoKey)
            - conversation established when user is online, cryptoKey dsitributed per conversation not persist for each user
        - ConversationTable (id, time, text, url) (from/toUser)
        - UnreadTable (from,to,time)
        - historical aggregation storage (date range to S3 etc.)
    - Redis Cache
        - heartbeat status update in Redis (user | server | lastHeartBeatTimestamp)



### references
- https://www.youtube.com/watch?v=zKPNUMkwOJE
- https://ably.com/topic/websockets-vs-http
- https://blog.cloudflare.com/http-3-vs-http-2/
- https://blog.nannan.cool/archives/32/
- https://building.lang.ai/our-journey-from-websockets-to-http-2-4d069c54effd
- https://docs.oracle.com/javase/tutorial/networking/sockets/index.html
    - https://docs.oracle.com/javase/tutorial/networking/sockets/examples/KnockKnockClient.java
    - https://docs.oracle.com/javase/tutorial/networking/sockets/examples/KnockKnockServer.java
    - https://docs.oracle.com/javase/tutorial/networking/sockets/examples/KnockKnockProtocol.java 
