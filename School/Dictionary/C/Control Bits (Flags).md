Each flag corresponds to 1-bit information. The most commonly used flags are **SYN, URG, ACK, PSH, FIN, and RST**. SYN bit is used in the initial three-way handshake where both parties generate the initial sequence numbers.


///


In [[TCP]] connection, flags are used to indicate a particular state of connection or to provide some additional useful information like troubleshooting purposes or to handle a control of a particular connection. Most commonly used flags are **“SYN”, “ACK” and “FIN”**. Each flag corresponds to 1 bit information. 

**Types of Flags:**   
 

- **Synchronization (SYN) –** It is used in first step of [[connection establishment]] phase or 3-way [[handshake]] process between the two hosts. Only the first packet from sender as well as receiver should have this flag set. This is used for [[synchronizing sequence number]] i.e. to tell the other end which sequence number they should accept.
- **Acknowledgement (ACK) –** It is used to acknowledge packets which are successful received by the host. The flag is set if the acknowledgement number field contains a valid acknowledgement number.   
    In given below diagram, the receiver sends an ACK = 1 as well as SYN = 1 in the second step of connection establishment to tell sender that it received its initial [[packet]].   
     
- **Finish (FIN) –** It is used to request for [[connection termination]] i.e. when there is no more data from the sender, it requests for connection termination. This is the last packet sent by sender. It frees the reserved resources and gracefully terminate the connection.   
     
- **Reset (RST) –** It is used to terminate the connection if the RST sender feels something is wrong with the TCP connection or that the conversation should not exist. It can get send from receiver side when packet is send to particular host that was not expecting it. 
- **Urgent (URG) –** It is used to indicate that the data contained in the packet should be prioritized and handled urgently by the receiver. This flag is used in combination with the Urgent Pointer field to identify the location of the urgent data in the packet.
- **Push (PSH) –** It is used to request immediate data delivery to the receiving host, without waiting for additional data to be buffered on the sender’s side. This flag is commonly used in applications such as real-time audio or video streaming.
- **Window (WND) –** It is used to communicate the size of the receive window to the sender. The window size is the amount of data that the receiving host is capable of accepting at any given time. The sender should limit the amount of data it sends based on the size of the window advertised by the receiver.
- **Checksum (CHK) –** It is used to verify the integrity of the TCP segment during transmission. The checksum is computed over the entire segment, including the header and data fields, and is recalculated at each hop along the network path.
- **Sequence Number (SEQ) –** It is a unique number assigned to each segment by the sender to identify the order in which packets should be received by the receiver. The sequence number is used in conjunction with the acknowledgement number to ensure reliable data transfer and to prevent duplicate packets.
- **Acknowledgement Number (ACK) –** It is used to acknowledge the receipt of a TCP segment and to communicate the next expected sequence number to the sender. The acknowledgement number field contains the sequence number of the next expected segment, rather than the number of the last received segment.