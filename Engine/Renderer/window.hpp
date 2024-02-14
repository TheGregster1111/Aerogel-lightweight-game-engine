#include <iostream>
#include <fstream>
#include <string>
#include <gtk/gtk.h>

#define Log(x) logFile << x << "\n\n"

gboolean main_update(gpointer data);

namespace Window
{
    #ifdef _WIN32

    #else

    void on_window_destroy(GtkWidget *widget, gpointer data)
    {
        gtk_main_quit();
    }

    void Init (int height, int width, char* title, std::ofstream &logFile, int fps)
    {
        if (!gtk_init_check(0, NULL))
        {
            Log("Failed to initialize window");
            return;
        }

        // Create the main window
        GtkWidget *window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
        gtk_window_set_title(GTK_WINDOW(window), title);
        gtk_window_set_default_size(GTK_WINDOW(window), width, height);

        // Connect the "destroy" signal to the callback function
        g_signal_connect(window, "destroy", G_CALLBACK(on_window_destroy), NULL);

        // Start main loop
        guint threadID = g_idle_add(main_update, NULL);

        // Show the main window
        gtk_widget_show_all(window);

        // Run the GTK main loop
        gtk_main();

        g_source_remove(threadID);
    }

    void Update ()
    {

    }
    #endif
}