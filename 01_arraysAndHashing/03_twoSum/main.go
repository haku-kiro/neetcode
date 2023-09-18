// main
package main

import "fmt"

func twoSum(numbers []int, target int) (posA, posB int) {
	prev := make(map[int]int)
	for idx, v := range numbers {
		diff := target - v
		prevIdx, exists := prev[diff]
		if exists {
			return prevIdx, idx
		}
		prev[v] = idx
	}
	return -1, -1
}

func main() {
	numbers := []int{2, 7, 9, 11, 5, 1}
  target := 20
  fmt.Println(twoSum(numbers, target))
}
