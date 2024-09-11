package main

import (
    "fmt"
    "net/http"
)

func healthHandler(w http.ResponseWriter, r *http.Request) {
    w.WriteHeader(http.StatusOK)
}

func main() {
    http.HandleFunc("/health/", healthHandler)
    fmt.Println("Server is starting on port 8899...")
    if err := http.ListenAndServe(":8899", nil); err != nil {
        fmt.Printf("Error starting server: %s\n", err)
    }
}
