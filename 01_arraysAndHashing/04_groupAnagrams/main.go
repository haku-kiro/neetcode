// main
package main

import "fmt"

// this only works with words that are from a-z

func groupAnagrams(words []string) [][]string {
	resultMap := make(map[[26]int][]string)
	for _, w := range words {
		key := [26]int{}
		for _, c := range w {
			idx := int(c) - int('a')
			key[idx]++
		}
		resultMap[key] = append(resultMap[key], w)
	}

	// There's no "values" method on a dict, have to generate that manually
	result := [][]string{}
	for _, v := range resultMap {
		result = append(result, v)
	}

	return result
}

func main() {
	data := []string{"tea", "eat", "fun", "nuf", "ufn", "god", "dog", "asdfasdf", "asd"}
	fmt.Println(groupAnagrams(data))
}
