package main

import (
	"fmt"
	"io"
	"net/http"
)

func getHello(w http.ResponseWriter, r *http.Request) {
	fmt.Println("GET Received")
	io.WriteString(w, "Hello again, Gefyra!")
}

func main() {
	http.HandleFunc("/", getHello)

	err := http.ListenAndServe(":3333", nil)
	if err != nil {
		panic(err)
	}
}
