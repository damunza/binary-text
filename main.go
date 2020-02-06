package main

import(
	"fmt"
	"io"
	"os"
	"log"
	"encoding/csv"
)

func main(){
	// opening the csv file
	words, err := os.Open("letters.csv")
	// if it fails to open create a new error message put in brackets
	if err != nil{
		log.Fatalln("couldn't open csv file")
	}
	
}

func translate(x){

}