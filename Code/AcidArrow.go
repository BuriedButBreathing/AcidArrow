package main

import (
	"io/ioutil"
	"log"
	"net/http"
	"os"
)

func main() {
	res, err := http.Get("https://raw.githubusercontent.com/BuriedButBreathing/AcidArrow/master/Assets/Test.bmp")
	if err != nil {
		log.fatal(err)
	}

	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)

	if err != nil {
		log.Fata(err)
	}

	_, err = os.Stdout.Write(body)

	if err != nil {
		log.Fatal(err)
	}
}
