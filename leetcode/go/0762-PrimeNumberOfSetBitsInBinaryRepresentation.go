//go:build ignore

package main

import (
	"fmt"
	"math/bits"
)

func countPrimeSetBits(left int, right int) int {
    cnt := 0
    prime := map[int]bool{
        2: true, 
		3: true, 
		5: true, 
		7: true,
        11: true, 
		13: true, 
		17: true, 
		19: true,
    }

    for i := left; i <= right; i++ {
        if prime[bits.OnesCount(uint(i))] {
            cnt++
        }
    }

    return cnt
}

func main() {
	left, right := 6, 10
	fmt.Print(countPrimeSetBits(left, right))
}