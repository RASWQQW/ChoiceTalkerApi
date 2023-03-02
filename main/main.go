package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
)

func extracter(elIs interface{}) interface{} {
	keys, isOk := elIs.(map[string]interface{})
	fmt.Println(keys)
	if isOk {
		return extracter(keys)
	} else {
		return keys
	}
}

func main() {
	jsonfile, err := os.Open("oppa.json")

	if err != nil {
		fmt.Println(err)
	}
	fmt.Println("File opened succesfully")

	defer jsonfile.Close()
	byteValue, _ := ioutil.ReadAll(jsonfile)
	var result map[string]interface{}
	json.Unmarshal([]byte(byteValue), &result)

	fmt.Println("result succesfully filled", len(result))
	fmt.Println(result)
	for key, val := range result {
		fmt.Print("Key: ", key, " Value: ", val, "\n")
		// extracter(val)
	}
}
