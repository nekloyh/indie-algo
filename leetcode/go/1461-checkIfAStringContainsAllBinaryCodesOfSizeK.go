//go:build ignore

package main

import "fmt"

func hasAllCodes(s string, k int) bool {
	n, total := len(s), 1 << k

	if n - k + 1 < total { return false }

	set := make(map[string]struct{})

	for i := 0; i <= n - k; i++ {
		sub := s[i : i + k]
		set[sub] = struct{}{}

		if len(set) == total { return true }
	}

	return false
}

func main() {
	fmt.Print(hasAllCodes("00110110", 2))
}
