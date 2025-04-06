using System;
using System.Collections.Generic;

class Program {
    static List<string> tarefas = new List<string>();

    static void Main() {
        Console.WriteLine("Aplicativo de Lista de Tarefas");
        tarefas.Add("Estudar C#");
        tarefas.Add("Finalizar projeto");

        foreach (string tarefa in tarefas)
            Console.WriteLine("- " + tarefa);
    }
}
