import javax.jms.Connection;
import javax.jms.ConnectionFactory;
import javax.jms.Destination;
import javax.jms.JMSException;
import javax.jms.MessageProducer;
import javax.jms.Session;
import javax.jms.TextMessage;

import org.apache.activemq.ActiveMQConnectionFactory;

public class ProducerMsging {
    private static String url = "failover://tcp://172.20.10.2:63636";  // Địa chỉ máy cài ActiveMQ 
    private static String subject = "thuc hanh 5";  // Tên queue

    public static void main(String[] args) throws JMSException {
        // Kết nối đến ActiveMQ
        ConnectionFactory connectionFactory = new ActiveMQConnectionFactory(url);
        Connection connection = connectionFactory.createConnection();
        connection.start();

        // Tạo session
        Session session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);

        // Tạo hàng đợi và producer
        Destination destination = session.createQueue(subject);
        MessageProducer producer = session.createProducer(destination);

        try {
            int msgTemp = 0;
            int i = msgTemp;  // Biến đếm số tin nhắn đã gửi
            while (msgTemp < 10) {  // 
                msgTemp++;
                String msg = "TextMessage-" + msgTemp;
                TextMessage message = session.createTextMessage(msg);
                producer.send(message);  // Gửi tin nhắn
                System.out.println("Producer sent: " + msg);  // In ra tin nhắn đã gửi
                i++;  // 
                Thread.sleep(1000);  // Gửi 1s/lần
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            connection.close();
        }
    }
}
