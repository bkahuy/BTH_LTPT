import javax.jms.Connection;
import javax.jms.ConnectionFactory;
import javax.jms.Destination;
import javax.jms.JMSException;
import javax.jms.Message;
import javax.jms.MessageConsumer;
import javax.jms.Session;
import javax.jms.TextMessage;

import org.apache.activemq.ActiveMQConnectionFactory;

public class ConsumerMsging {
    private static String url = "failover://tcp://172.20.10.7:63636";  // Địa chỉ máy cài ActiveMQ
    private static String subject = "Thuchanh5";  // Tên queue

    public static void main(String[] args) throws JMSException {
        // Kết nối đến ActiveMQ
        ConnectionFactory connectionFactory = new ActiveMQConnectionFactory(url);
        Connection connection = connectionFactory.createConnection();
        connection.start();

        // Tạo session
        Session session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);

        // Lấy thông tin queue
        Destination destination = session.createQueue(subject);
        
        // Tạo consumer để nhận tin nhắn
        MessageConsumer consumer = session.createConsumer(destination);

        try {
            while (true) {
                Message message = consumer.receive();  // Nhận tin nhắn
                if (message instanceof TextMessage) {
                    TextMessage textMessage = (TextMessage) message;
                    System.out.println("Consumer received: " + textMessage.getText());  // Hiển thị tin nhắn đã nhận
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            connection.close();
        }
    }
}
