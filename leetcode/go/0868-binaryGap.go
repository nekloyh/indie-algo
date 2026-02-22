//go:build ignore

package main

import "fmt"

func binaryGap(n int) int {
    ans, last := 0, -1
	for i := 0; n > 0; i++ {
		if n & 1 == 1 {
			if last != -1 { ans = max(ans, i - last) }
			last = i
		}
		n >>= 1
	}
	return ans
}

func main() {
	// 13 = 1011
	fmt.Print(binaryGap(13))
}