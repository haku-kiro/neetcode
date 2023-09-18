// main
package main

import "fmt"

// O(n) time complexity, O(n) space complexity
func containsDuplicates(numbers []int) bool {
	hashset := make(map[int]int)
	for _, n := range numbers {
		_, exists := hashset[n]
		if exists {
			return true
		}

		hashset[n] = n
	}

	return false
}

// O(n^2) time complexity, O(1) space complexity
func containsDuplicateWorse(numbers []int) bool {
  for ix, x := range numbers {
    for iy, y := range numbers {
      // don't check same index
      if ix == iy {
        continue
      }
      if x == y {
        return true
      }
    }
  }
  return false
}

func main() {
	exampleData := []int{1, 2, 3, 4, 5, 6, 1}
	fmt.Println(containsDuplicates(exampleData))
	fmt.Println(containsDuplicateWorse(exampleData))
}
