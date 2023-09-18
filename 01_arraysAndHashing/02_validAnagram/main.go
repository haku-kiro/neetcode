// main
package main

import "fmt"

func createHashMap(s string) map[string]int {
	result := make(map[string]int)
	for _, c := range s {
		sc := string(c)
		_, exists := result[sc]
		if exists {
			result[sc]++
		} else {
			result[sc] = 1
		}
	}

	return result
}

func isAnagram(s, t string) bool {
	if len(s) != len(t) {
		return false
	}

	sHash := createHashMap(s)
	tHash := createHashMap(t)

	for char, count := range sHash {
		_, existsInT := tHash[char]
		if !existsInT {
			return false
		}

		if tHash[char] != count {
			return false
		}
	}

	return true
}

func main() {
	s := "anagram"
	t := "anagram"

	fmt.Printf("string s: %q and string t: %q make an anagram: %v\n", s, t, isAnagram(s, t))
}
