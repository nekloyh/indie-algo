//go:build ignore

package main

import "fmt"

func numSteps(s string) int {
	res, reminder := 0, 0

	for i := len(s) - 1; i > 0; i-- {
		bit := int(s[i] - '0') + reminder

		if bit == 1 {
			res += 2
			reminder = 1
		} else {
			res += 1
		}
	}

	return res + reminder
}

func main() {
	s := "1101"
	fmt.Print(numSteps(s))
}