package main

import "fmt"

func main() {
	var maxLenConsecPrimes int = 0
	var coeffProduct int = 0
	for a := -999; a < 999; a++ {
		for b := -1000; b < 1000; b++ {
			var lenConsecPrimes int = get_len_consec_primes(a, b)
			if lenConsecPrimes > maxLenConsecPrimes {
				maxLenConsecPrimes = lenConsecPrimes
				coeffProduct = a * b
			}
		}
	}
	fmt.Println(coeffProduct)
}

func is_prime(n int) bool {
	if n <= 1 {
		return false
	}
	var i int = 2
	for i*i <= n {
		if n%i == 0 {
			return false
		}
		i += 1
	}
	return true
}

func get_len_consec_primes(a int, b int) int {
	var lenConsecPrimes, n int = 0, 0
	for true {
		if is_prime(n*n + a*n + b) {
			lenConsecPrimes += 1
			n += 1
		} else {
			break
		}
	}
	return lenConsecPrimes
}
