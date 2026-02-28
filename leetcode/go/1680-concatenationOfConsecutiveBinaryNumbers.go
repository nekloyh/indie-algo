//go:build ignore

package main

import "fmt"

func countBits(n int) int {
	count := 0
	for n > 0 {
		count++
		n >>= 1
	}
	return count
}

func concatenatedBinary(n int) int {
	res := 0
    MOD := 1000000007
	for i := 1; i <= n; i++ {
		res = (res << countBits(i)) | i
		res = res % MOD
	}
	return res
}

func main() {
	number := 3
	fmt.Print(concatenatedBinary(number))
}