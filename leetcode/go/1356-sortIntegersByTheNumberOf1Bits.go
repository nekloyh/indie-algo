//go:build ignore

package main

import (
	"fmt"
	"sort"
)

func countBits(num int) int {
	cnt := 0
	for num > 0 {
		cnt += num & 1
		num >>= 1
	}
	return cnt
}

func sortByBits(arr []int) []int {
	sort.Slice(arr, func(i, j int) bool {
		aBits := countBits(arr[i])
		bBits := countBits(arr[j])

		if aBits == bBits {
			return arr[i] < arr[j]
		}
		return aBits < bBits
	})
	return arr
}

func main() {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8}
	fmt.Print(sortByBits(arr))
}