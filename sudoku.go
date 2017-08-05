package main

import (
	"fmt"
	"math/rand"
	"os"
	"os/exec"
	"strconv"
	"time"
)

var list = make([]string, 0) // make(map[int]string)
var m = make(map[string]string)
var mapByRow [9][9]string
var mapByCol [9][9]string

func printTable() {
	for a := 0; a < 9; a++ {
		for i := 0; i < 9; i++ {
			index := mapByRow[a][i]
			fmt.Print(" " + m[index])
			if i == 2 || i == 5 {
				fmt.Print("  ")
			}
		}
		fmt.Println("")
		if a == 2 || a == 5 {
			fmt.Println("")
		}
	}
}

func clearTable() {
	for s := 1; s <= 9; s++ {
		section := "s" + strconv.Itoa(s)
		list = append(list, strconv.Itoa(s))
		for p := 1; p <= 9; p++ {
			position := section + "p" + strconv.Itoa(p)
			m[position] = "0" // strconv.Itoa(p)
		}
	}
}

func resetNumbers() {
	list = list[:0]
	for s := 1; s <= 9; s++ {
		list = append(list, strconv.Itoa(s))
	}
}

func delNumber(value string) {
	for i, v := range list {
		if v == value {
			list = append(list[:i], list[i+1:]...)
		}
	}
}

func getNumber() string {
	index := "error"
	var randNumber int
	size := len(list)
	if size > 0 {
		if size == 0 {
			randNumber = 0
		} else {
			randNumber = rand.Intn(size)
		}
		if len(list[randNumber]) == 1 {
			index = list[randNumber]
		}
	}
	return index
}

func runChecks(list [9]string, value string) bool {
	valid := true
	for _, element := range list {
		currentValue := m[element]
		if currentValue == value {
			valid = false
		}
	}
	return valid
}

func checkSection(point string, value string) bool {
	section := point[0:2]
	list := [9]string{section + "p1", section + "p2", section + "p3", section + "p4", section + "p5", section + "p6", section + "p7", section + "p8", section + "p9"}
	return runChecks(list, value)
}

func checkRow(point, value string) bool {
	index := 0
	for i := 0; i < 9; i++ {
		for a := 0; a < 9; a++ {
			if mapByRow[i][a] == point {
				index = i
			}
		}
	}
	return runChecks(mapByRow[index], value)
}

func checkCol(point, value string) bool {
	index := 0
	for i := 0; i < 9; i++ {
		for a := 0; a < 9; a++ {
			if mapByCol[i][a] == point {
				index = i
			}
		}
	}
	return runChecks(mapByCol[index], value)
}

func checkRules(point, value string) bool {
	section := checkSection(point, value)
	row := checkRow(point, value)
	col := checkCol(point, value)
	return col && row && section
}

func travel() {
	for point := range m {
		valid := true
		for valid {
			randNumber := getNumber()
			if randNumber == "error" {
				break
			} else if checkRules(point, randNumber) {
				m[point] = randNumber
				valid = false
				resetNumbers()
			} else {
				delNumber(randNumber)
			}
		}
	}
}

func initVars() {
	rand.Seed(time.Now().UnixNano())
	mapByRow[0] = [9]string{"s1p1", "s1p2", "s1p3", "s2p1", "s2p2", "s2p3", "s3p1", "s3p2", "s3p3"}
	mapByRow[1] = [9]string{"s1p4", "s1p5", "s1p6", "s2p4", "s2p5", "s2p6", "s3p4", "s3p5", "s3p6"}
	mapByRow[2] = [9]string{"s1p7", "s1p8", "s1p9", "s2p7", "s2p8", "s2p9", "s3p7", "s3p8", "s3p9"}
	mapByRow[3] = [9]string{"s4p1", "s4p2", "s4p3", "s5p1", "s5p2", "s5p3", "s6p1", "s6p2", "s6p3"}
	mapByRow[4] = [9]string{"s4p4", "s4p5", "s4p6", "s5p4", "s5p5", "s5p6", "s6p4", "s6p5", "s6p6"}
	mapByRow[5] = [9]string{"s4p7", "s4p8", "s4p9", "s5p7", "s5p8", "s5p9", "s6p7", "s6p8", "s6p9"}
	mapByRow[6] = [9]string{"s7p1", "s7p2", "s7p3", "s8p1", "s8p2", "s8p3", "s9p1", "s9p2", "s9p3"}
	mapByRow[7] = [9]string{"s7p4", "s7p5", "s7p6", "s8p4", "s8p5", "s8p6", "s9p4", "s9p5", "s9p6"}
	mapByRow[8] = [9]string{"s7p7", "s7p8", "s7p9", "s8p7", "s8p8", "s8p9", "s9p7", "s9p8", "s9p9"}
	mapByCol[0] = [9]string{"s1p1", "s1p4", "s1p7", "s4p1", "s4p4", "s4p7", "s7p1", "s7p4", "s7p7"}
	mapByCol[1] = [9]string{"s1p2", "s1p5", "s1p8", "s4p2", "s4p5", "s4p8", "s7p2", "s7p5", "s7p8"}
	mapByCol[2] = [9]string{"s1p3", "s1p6", "s1p9", "s4p3", "s4p6", "s4p9", "s7p3", "s7p6", "s7p9"}
	mapByCol[3] = [9]string{"s2p1", "s2p4", "s2p7", "s5p1", "s5p4", "s5p7", "s8p1", "s8p4", "s8p7"}
	mapByCol[4] = [9]string{"s2p2", "s2p5", "s2p8", "s5p2", "s5p5", "s5p8", "s8p2", "s8p5", "s8p8"}
	mapByCol[5] = [9]string{"s2p3", "s2p6", "s2p9", "s5p3", "s5p6", "s5p9", "s8p3", "s8p6", "s8p9"}
	mapByCol[6] = [9]string{"s3p1", "s3p4", "s3p7", "s6p1", "s6p4", "s6p7", "s9p1", "s9p4", "s9p7"}
	mapByCol[7] = [9]string{"s3p2", "s3p5", "s3p8", "s6p2", "s6p5", "s6p8", "s9p2", "s9p5", "s9p8"}
	mapByCol[8] = [9]string{"s3p3", "s3p6", "s3p9", "s6p3", "s6p6", "s6p9", "s9p3", "s9p6", "s9p9"}
}

func main() {
	initVars()
	out, _ := exec.Command("/usr/bin/clear").Output()
	os.Stdout.Write(out)

	clearTable()
	travel()
	printTable()
}
