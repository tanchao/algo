package com.tanchao;

import lombok.AllArgsConstructor;
import lombok.Getter;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;
import java.util.List;

public class SocketServer {
    public static final int PORT = 9527;
    private static final List<ClientHandler> clientHandlers = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        ServerSocket serverSocket = new ServerSocket(PORT);
        while (true) {
            Socket clientSocket = null;
            try {
                clientSocket = serverSocket.accept();
                PrintWriter out =
                        new PrintWriter(clientSocket.getOutputStream(), true);
                BufferedReader in = new BufferedReader(
                        new InputStreamReader(clientSocket.getInputStream()));

                ClientHandler clientHandler = new ClientHandler(in, out, clientSocket, clientHandlers);
                clientHandlers.add(clientHandler);
                clientHandler.start();
            } catch (IOException e) {
                System.out.println("Exception caught when trying to listen on port "
                        + PORT + " or listening for a connection");
                System.out.println(e.getMessage());
                serverSocket.close();
                clientSocket.close();
            }
        }

    }
}

@AllArgsConstructor
@Getter
class ClientHandler extends Thread {
    private final BufferedReader in;
    private final PrintWriter out;
    private final Socket socket;
    private final List<ClientHandler> clientHandlers;

    synchronized public void publish(String message) {
        for (ClientHandler clientHandler : clientHandlers) {
            if (!this.equals(clientHandler)) {
                clientHandler.getOut().println(message);
            }
        }
    }

    @Override
    public void run() {
        String inputLine, outputLine;

        // Initiate conversation with client
        // KnockKnockProtocol kkp = new KnockKnockProtocol();
        //outputLine = "test"; //kkp.processInput(null);
        //out.println(outputLine);

        while (true) {
            try {
                if ((inputLine = in.readLine()) == null) {
                    break;
                }
                outputLine = inputLine;
                //out.println(outputLine);
                publish(outputLine);
                if (outputLine.equals("Bye.")) {
                    break;
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

        // cleanup
        try {
            this.in.close();
            this.out.close();
            clientHandlers.remove(this);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
