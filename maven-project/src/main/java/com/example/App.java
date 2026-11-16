package com.example;

public class App {

    // Возвращает приветствие; вынесено отдельно для теста
    public static String greeting() {
        return "Hello, Maven!";
    }

    public static void main(String[] args) {
        System.out.println(greeting());
    }
}
