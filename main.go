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

	//creating a variable that can read the encoded file resulting from opening a csv file
	codes := csv.NewReader(words)

	// creating a map from the processed csv
	for{
		//reading each csv entry
		record, err := codes.Read() // because codes is an instance of csv.Newreader
		// check if the program has finished reading
		if err == io.EOF{
			break
		}
		// checking to see if the data has been read 
		if err != nil{
			log.Fatal(err)
		}
		// printing the output
		fmt.Printf("case: %s letter%s\n", record[1], record[2]) 
		// started with index 1 instead of 0 because 0 is the indexing column
	}
	
}

// func translate(x){

// }